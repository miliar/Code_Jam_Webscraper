#include <iostream>
#include<cstdio>
#include<cstring>
using namespace std;
FILE *fout;
void prn(long long n)
{
    if(n) prn(n>>1);
    else return;
    fprintf(fout,"%d",(n&1));
}
long long xch(long long n,int t)
{
    if(n) return xch(n>>1,t)*t+(n&1);
    else return 0;
}
bool isp[100000010];
long long f[20];
int p[25000000];
int main()
{
    fout=fopen("output.txt","w");
    long long n=16,jj=50;
    long long first=1<<(n-1),last=1<<n;
    first++;last--;
    memset(isp,0,sizeof(isp));
    int op=0;
    for(int i=2;i<=100000000;i++)
    {
        if(!isp[i])
            p[op++]=i;
        for(int j=0;j<op && i*p[j]<=100000000;j++)
        {
            isp[i*p[j]]=1;
            if(!(i%p[j]))
                break;
        }
    }
    fprintf(fout,"Case #1:\n");
    while(jj>0)
    {
        bool flag=true;
        for(int i=2;i<=10;i++)
        {
            long long tmp=xch(first,i);
            f[i]=-1;
            for(int j=0;1LL*p[j]*p[j]<=tmp;j++)
                if(tmp%p[j]==0)
                {
                    f[i]=p[j];
                    break;
                }
            if(f[i]==-1)
            {
                flag=false;
                break;
            }
        }
        if(flag)
        {
            prn(first);
            for(int i=2;i<=10;i++) fprintf(fout," %I64d",f[i]);
            fprintf(fout,"\n");
            jj--;
        }
        first+=2;
        if(first%3000==0) printf("%d\n",first);
    }
    return 0;
}
