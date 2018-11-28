#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<sstream>
using namespace std;
int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("output_2_large_final.txt", "w", stdout );
    int T,cases=0;
    long long sq[40]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
    scanf("%d",&T);
    while(T--)
    {
        long long int a,b,i,count=0;
        scanf("%lld %lld",&a,&b);
        for(i=0;i<39;i++)
        {
           if(sq[i]>=a && sq[i]<=b) count++;
        }
        printf("Case #%d: %lld\n",++cases,count);
    }
    return 0;
}
////////////////////////MAIN PROGRAM////////////////////
/*
#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<sstream>
using namespace std;
int main()
{
    freopen("b_large.txt","r",stdin);
    freopen("output_2_large_test.txt", "w", stdout );
    int T,cases=0;
    scanf("%d",&T);
    while(T--)
    {
        long long int a,b,i,count=0;
        scanf("%lld %lld",&a,&b);
        stringstream ss;
        long long a1=a,b2=b;
        a=sqrt(a); b=sqrt(b);
        for(i=a;i<=b;i++)
        {
            char s[20]={'\0'},s2[20]={'\0'};
            ss.clear();
            ss<<i;
            ss>>s;
            strcpy(s2,s);
            strrev(s);
            if(!strcmp(s,s2))
            {
                if(i*i>=a1 && i*i<=b2){
                long long i1=i*i;
                ss.clear();
                ss<<i1;
                ss>>s;
                 strcpy(s2,s);
                 strrev(s);
                  if(!strcmp(s,s2))
                 {
                  count++;
                  cout<<i*i<<",";
                 }
            }
            }
            s[0]='\0';
            s2[0]='\0';
            }
        printf("\nCase #%d: %lld\n",++cases,count);
    }
    return 0;
}
*////////////
