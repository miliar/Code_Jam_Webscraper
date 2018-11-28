#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int N;
int r,p,s;
char ch1[100000],ch2[100000];

inline char beat(char c)
{
    if(c=='R')return 'S';
    if(c=='S')return 'P';
    if(c=='P')return 'R';
}

inline bool check1(int n)
{
    memset(ch1,' ',sizeof(ch1));
    ch1[1]='R';

    for(int i=1;i<=n;i++)
    {
        memset(ch2,' ',sizeof(ch2));

        for(int j=1;j<=(1<<i);j++)
            if(j&1)
                ch2[j]=ch1[(j+1)>>1];
            else
                ch2[j]=beat(ch1[(j+1)>>1]);

        for(int j=1;j<=(1<<i);j++)
            ch1[j]=ch2[j];
    }
    int r0=0,s0=0,p0=0;
    for(int i=1;i<=(1<<n);i++)
        if(ch1[i]=='R')
            r0++;
        else
            if(ch1[i]=='S')
                s0++;
            else
                p0++;

    return r0==r&&s0==s&&p0==p;
}
inline bool check2(int n)
{
    memset(ch1,' ',sizeof(ch1));
    ch1[1]='P';

    for(int i=1;i<=n;i++)
    {
        memset(ch2,' ',sizeof(ch2));

        for(int j=1;j<=(1<<i);j++)
            if(j&1)
                ch2[j]=ch1[(j+1)>>1];
            else
                ch2[j]=beat(ch1[(j+1)>>1]);

        for(int j=1;j<=(1<<i);j++)
            ch1[j]=ch2[j];
    }
    int r0=0,s0=0,p0=0;
    for(int i=1;i<=(1<<n);i++)
        if(ch1[i]=='R')
            r0++;
        else
            if(ch1[i]=='S')
                s0++;
            else
                p0++;

    return r0==r&&s0==s&&p0==p;
}
inline bool check3(int n)
{
    memset(ch1,' ',sizeof(ch1));
    ch1[1]='S';

    for(int i=1;i<=n;i++)
    {
        memset(ch2,' ',sizeof(ch2));

        for(int j=1;j<=(1<<i);j++)
            if(j&1)
                ch2[j]=ch1[(j+1)>>1];
            else
                ch2[j]=beat(ch1[(j+1)>>1]);

        for(int j=1;j<=(1<<i);j++)
            ch1[j]=ch2[j];
    }
    int r0=0,s0=0,p0=0;
    for(int i=1;i<=(1<<n);i++)
        if(ch1[i]=='R')
            r0++;
        else
            if(ch1[i]=='S')
                s0++;
            else
                p0++;

    return r0==r&&s0==s&&p0==p;
}

inline void change(int n)
{
    if(n>1)change(n-1);

    for(int i=1;i<=(1<<N)/(1<<(n));i++)
    {

        int j0=(i-1)*(1<<n)+1;
        int j1=j0+(1<<(n-1));

        bool flag=false;
        for(int j=1;j<=(1<<(n-1));j++)
        {
            if(ch1[j0+j-1]>ch1[j1+j-1])
            {
                flag=true;
                break;
            }
        }
        if(flag)
        {
            for(int j=1;j<=(1<<(n-1));j++)
                swap(ch1[j0+j-1],ch1[j1+j-1]);
        }
    }
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        int n;
        scanf("%d%d%d%d",&n,&r,&p,&s);
        N=n;
        printf("Case #%d: ",t);
        if(check1(n))
        {
            change(n);
            for(int i=1;i<=(1<<n);i++)
                printf("%c",ch1[i]);
            printf("\n");
        }
        else
            if(check2(n))
            {
                change(n);
                for(int i=1;i<=(1<<n);i++)
                    printf("%c",ch1[i]);
                printf("\n");
            }
            else
                if(check3(n))
                {
                    change(n);
                    for(int i=1;i<=(1<<n);i++)
                        printf("%c",ch1[i]);
                    printf("\n");
                }
                else
                    printf("IMPOSSIBLE\n");
    }
}
