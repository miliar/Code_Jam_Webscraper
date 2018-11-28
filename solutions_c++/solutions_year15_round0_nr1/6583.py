#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{
    long long t,i,n,ans,sum,c=1;
    char a[100000];
    FILE *fp,*fo;
    fp=fopen("A-small-attempt0.in","r");
    fo=fopen("output.txt","w");
    fscanf(fp,"%lld",&t);
    while(t--)
    {
        ans=0;
        fscanf(fp,"%lld %s",&n,&a);
        sum=a[0]-48;
        for(i=1;i<=n;i++)
        {
        	if(a[i]!='0')
            {if((i)<=sum)
            sum+=a[i]-48;
            else
            {
                if((i)>sum)
                {
                    ans=ans+i-sum;
                    sum=sum+a[i]-48+ans;
                }
            }}
        }
        fprintf(fo,"Case #%lld: %lld\n",c++,ans);
        //printf("%lld %s\n",s,a);
    }
    return 0;
}
