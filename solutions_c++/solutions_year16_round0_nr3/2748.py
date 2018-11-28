#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std ;
int m[510][40];
int len[510];
int fact[510][100];
bool isprime(long long num,int now,int base)
{
    bool f=true;
    for (long long fac=2; fac<=sqrt(num); fac=fac+1)
    {
        if (num%fac==0)
        {
            f=false;
            fact[now][base]=fac;
            break;
        }
    }
    if (f) return true;
    else return false;
}
int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);

    int turn;
    int n,J;
    scanf("%d",&turn);
    for (int tt=1; tt<=turn; tt++)
    {
        scanf("%d%d",&n,&J);
        long long s=1,t=1;
        for (int kk=1; kk<=n; kk++)
        {
            s=s*2;
            t=t*2;
        }
        s=s/2+1;
        t=t-1;
        int cou=-1;
        //cout<<s<<t<<endl;
        for (long long i=s; i<=t; i=i+2)
        {
            cou++;
            // cout<<i<<endl;
            if (isprime(i,cou,2))
            {
                cou--;
                continue;
            }
            long long tmp=i;
            int p=-1;
            while(tmp>0)
            {
                m[cou][++p]=tmp%2;
                tmp=tmp/2;
            }
            len[cou]=p;
            //bool f=true;
            for (int j=10; j>=3; j--)
            {
                long long tmp=i;


                /* printf("cou:%d\n",cou);
                 for (int k=p;k>=0;k--)
                     printf("%d ",m[cou][k]);
                     printf("\n");*/
                tmp=0;

                for (int k=len[cou]; k>=0; k--)
                    tmp=tmp*j+m[cou][k];
                // printf("cou:%d\n",cou);
                // printf("%d\n",tmp);
                 if (isprime(tmp,cou,j))
                 {
                    // cout<<"tmp:"<<tmp<<"base:"<<j<<" is prime"<<endl<<endl<<endl<<endl;
                     cou--;
                     break;
                 }
                // else cout<<"tmp:"<<tmp<<"base:"<<j<<" isnot prime"<<endl;*/
            }
            if (cou==J-1) break;
        }
        printf("Case #%d:\n",tt);
        for (int k=0; k<=J-1; k++)
        {
            for (int i=len[k]; i>=0; i--)
                printf("%d",m[k][i]);
            printf(" ");
            for (int i=2; i<=9; i++)
                printf("%d ",fact[k][i]);
            printf("%d\n",fact[k][10]);
        }
    }
    return 0;
}
