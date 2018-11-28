#include<bits/stdc++.h>
using namespace std;
#define cin(n) scanf("%d",&n)
#define cinl(n) scanf("%lld",&n)

int adj[12][12];
int pref[1000008],suf[1000008];
long long min(long long a,long long b)
{
    return a<=b?a:b;
}
int main()
{
    int t,m,n,i,j,k,l;
    int ct=1;
    cin(t);
    for(i=1;i<=4;i++)
        adj[1][i]=i;

            adj[2][1]=2;
            adj[2][2]=-1;
            adj[2][3]=4;
            adj[2][4]=-3;

            adj[3][1]=3;
            adj[3][2]=-4;
            adj[3][3]=-1;
            adj[3][4]=2;

            adj[4][1]=4;
            adj[4][2]=3;
            adj[4][3]=-2;
            adj[4][4]=-1;

    while(t--)
    {
        long long x;
        cin(n);cinl(x);
        string s,ss;
        cin>>ss;
        s="";
int ans=0;
        for(int z=1;z<=min(x,15);z++)
        {
            s+=ss;
            n=s.length();
            for(i=0;i<n;i++)
            {
                if(s[i]=='i')
                    s[i]='2';
                if(s[i]=='j')
                    s[i]='3';
                if(s[i]=='k')
                    s[i]='4';
            }



            int init=1,signi=0;
            int fg=0;
//cout<<n<<"\n";
            for(i=0;i<n;i++)
            {
                init=adj[init][s[i]-'0'];
                if(init<0)
                    signi^=1;
                init=abs(init);
                if(signi)
                    pref[i]=-init;
                else
                    pref[i]=init;

                if(pref[i]==2&&!fg)
                    fg=1;
                if(pref[i]==4&&fg==1)
                    fg++;

            }

            if(pref[n-1]!=-1)
                fg=0;
            if(fg>=2&&z%3==x%3)
                ans=1;




        }
        cout<<"Case #"<<ct++<<": ";
        if(ans==1)
        cout<<"YES\n";
else
cout<<"NO\n";
    }

    return 0;
}
