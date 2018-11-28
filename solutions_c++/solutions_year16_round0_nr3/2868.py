#include<iostream>
#include<stdio.h>
#include <bitset>
#include<string.h>
#define mod 1000000007
#define MUL(a, b) ((long long int)(((a)*(b))))
using namespace std;

char binary[50];
long long int a[10];

int isPrime (long long int number) { 
    if (number < 2) return 1;
    if (number == 2) return 0;
    if (number % 2 == 0) return 1;
    for (long long int i=3; (i*i) <= number; i+=2) {
        if (number % i == 0 ) return 1;
    }
    return 0;
}
 
long long int pow_mod(long long int b, long long int e) {
    long long int r = 1;
    while(e) {
        if (e&1)
            r = MUL(r, b);
        e >>= 1;
        b = MUL(b, b);
    }
    return r;
}

void ConvertToBinary(long long int n, long long int dgt)
{
    long long int u=dgt-1;
    for( ; n!=0 ; )
    {
       binary[u]=(n%2)+'0'; 
     //  printf("u=%d and binary[%d]=%c\n",u,u,binary[u]);
       n/=2;
       u--;
    }
    binary[dgt]='\n';
   // printf("%s",binary);
}

long long int convertTobase(char binary[] , long long int base )
{
    long long int num,i,n,h=0;
    n=strlen(binary);
    num=0;
    for(i=n-2 ; i>=0 ; i--)
    {
        num=num+(long long int)(binary[i]-'0')*pow_mod(base,h);
        h++;
    }
    return num;
}


int numtoString(long long int num , long long int n)
{
    long long int k,i;
    if( isPrime(num)==0 )
        return 0;
    a[0]=num;
    //printf("2base num=%lld\n",num);
    //u=0;
    //binary = bitset<n>(num).to_string(); //to binary
    ConvertToBinary(num,n);
   // binary[u]='\n';
    //cout<<binary<<"\n";
    k=1;
    for(i=3 ; i<=10 ; i++)
    {
        
        num=convertTobase(binary,i);
       // printf("%lldbase=%lld\n",i,num);
        if( isPrime(num)==0 )
            return 0;
        a[k++]=num;    
     //   printf("here1\n");
    }
   // printf("here2\n");
    
    return 1;
    
    
}

void nontrivial()
{
    long long int j,i;
    
    for(i=0 ; i<=8 ; i++)
    {
        for(j=2 ; j<a[i] ; j++)
        {
            if(a[i]%j==0)
            {
                printf("%lld ",j);
                break;
            }
        }
    }
}

int main()
{
    //freopen("input.txt","r",stdin);
    int t,k=1;
    long long int n,j,count,num,end,i;
    scanf("%d",&t);
    while(k<=t)
    {
        scanf("%lld%lld",&n,&j);
        count=0;
        end=pow_mod(2,n);
        num=(end/2)+1;
        
        printf("Case #1:\n");
        
        for( ; num<=end ; num+=2)
        {   
            //printf("main num=%lld\n",num);
            
            if(numtoString(num,n))
            {
                //printf("%s ",binary);
                for(i=0 ; i<n ; i++)
                    printf("%c",binary[i]);
                printf(" ");    
                nontrivial();
                printf("\n");
                count++;
                
            }
            if(count==j)
            {
                
                //printf("%s ",binary);
                //nontrivial();
                //printf("\n");
                
                break;
            }
            
        }
        
        k++;
    }
    return 0;
}
