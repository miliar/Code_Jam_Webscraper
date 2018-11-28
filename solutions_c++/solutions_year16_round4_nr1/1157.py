#include<bits/stdc++.h>
#define ll long long
#define pii pair<int,int>
#define piii pair<int,pair<int,int> >
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define SIZE 10000002
using namespace std;

inline ll getnum()
{
    char c = getchar();
    ll num,sign=1;
    for(;c<'0'||c>'9';c=getchar())if(c=='-')sign=-1;
    for(num=0;c>='0'&&c<='9';)
    {
        c-='0';
        num = num*10+c;
        c=getchar();
    }
    return num*sign;
}

char S[14][100004],temp[100003];

void dosort(int l,int r,int pos)
{
    if(l==r)return;

    int x=(l+r)/2;
    dosort(l,x,pos);
    dosort(x+1,r,pos);

    int cmp=0;

    for(int i=l,j=x+1;i<=x;i++,j++)
    {
        if(S[pos][i]<S[pos][j]){cmp=1;break;}
        if(S[pos][i]>S[pos][j]){cmp=-1;break;}
    }

    if(cmp==-1)
    {
        for(int i=l;i<=x;i++)temp[i]=S[pos][i];
        for(int i=x+1,j=l;i<=r;i++,j++)S[pos][j]=S[pos][i];
        for(int i=l,j=x+1;i<=x;i++,j++)S[pos][j]=temp[i];
    }
}

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    char A[4]={0,'R','P','S'};

    int tests=getnum();

    for(int cases=1;cases<=tests;cases++)
    {
        printf("Case #%d: ",cases);

        int n=getnum(),r=getnum(),p=getnum(),s=getnum(),done=0;

        for(int win=1;win<=3;win++)
        {
            int rr=r,pp=p,ss=s;

            S[1][1]=A[win];
            if(win==1)rr--;
            if(win==2)pp--;
            if(win==3)ss--;

            for(int i=1,len=1;i<=n;i++,len*=2)
            {
                int ind=0;
                for(int j=1;j<=len;j++)
                {
                    if(S[i][j]=='R')S[i+1][++ind]='R',S[i+1][++ind]='S',ss--;
                    if(S[i][j]=='P')S[i+1][++ind]='P',S[i+1][++ind]='R',rr--;
                    if(S[i][j]=='S')S[i+1][++ind]='P',S[i+1][++ind]='S',pp--;
                }
                S[i+1][++ind]=0;
            }

            if(rr==0&&pp==0&&ss==0)
            {
                dosort(1,1<<n,n+1);
                puts(S[n+1]+1);
                done=1;
            }
            if(done)break;
        }
        if(!done)puts("IMPOSSIBLE");
    }
}
