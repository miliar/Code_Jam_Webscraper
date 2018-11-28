#include<stdio.h>
#include<bitset>
#define SIZE 10000000

std:: bitset <SIZE> pal;
long long square[SIZE];
int number[SIZE];
bool check(long long a)
{
    long long b=0,temp=a;
    while(temp)
    {
        b=b*10+temp%10;
        temp/=10;
    }
    if(a==b) return 1;
    else return 0;
}

int main()
{
    long long i,j,k;
    int count=0,c=1;
    for(i=1;i<SIZE;i++)
    {
        if(check(i)==1)
        {
            if(check(i*i)==1)
            {
                pal[i]=1;
                number[i-1]=++count;
            }
            else number[i-1]=count;
        }
        else number[i-1]=count;
        square[i]=i*i;
    }
    int t;long long a,b;
    scanf("%d",&t);
   // printf("%d\n",count);
    while(t--)
    {
       j=1;k=1;
        scanf("%lld %lld",&a,&b);
        while(j<SIZE&&square[j]<a)
            j++;
        k=j;
        while(k<SIZE&&square[k]<=b)
            k++;
        if(j==SIZE)
        {
                printf("Case #%d: 0\n",c);
                c++;
                continue;
        }
        if(check(square[j])==1&&check(j)==1) j--;


        if(j==0)printf("Case #%d: %d\n",c,number[k-2]);
        else    printf("Case #%d: %d\n",c,number[k-2]-number[j-1]);
        c++;
    }
    return 0;
}
