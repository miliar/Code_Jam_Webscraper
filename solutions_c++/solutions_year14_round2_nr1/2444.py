#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<climits>

using namespace std;
#define ALL(i,n) for(i = 0; i < (n); i++)
#define FOR(i,a,b) for(i = (a); i < (b); i++)
#define SET(p) memset(p,-1,sizeof(p))
#define CLR(p) memset(p,0,sizeof(p))
#define S(n) scanf("%d",&n)
#define P(n) printf("%d\n",n)
#define Sl(n) scanf("%lld",&n)
#define Pl(n) printf("%lld\n",n)
#define Sf(n) scanf("%lf",&n)
#define Ss(n) scanf("%s",n)
#define LL long long
#define ULL unsigned long long
#define pb push_back
#define R(f) freopen(f,"r",stdin);
#define W(f) freopen(f,"w",stdout);

vector<string>v;
string s;
int main()
{
    R("2.in");
    W("2.out");
    int t,cas,n;
    S(t);

   cas=0;
    while(t--)
    {
        cas++;
        S(n);
        v.clear();
        for(int i=0;i<n;i++)
        {cin>>s;v.pb(s);}

        string g="",prev="";
        int cnt;
        char curchar;
        vector<int>acnt[1000];
        int f=0;
        for(int i=0;i<n;i++)
        {
            g=v[i][0];
            curchar=v[i][0];
            cnt=1;
        for(int j=1;j<=v[i].length();j++)
            {
                 if(j==v[i].length())
                   {acnt[i].pb(cnt);continue;}
            if(v[i][j]==curchar)
                {cnt++;continue;}

                    g+=v[i][j];
                    acnt[i].pb(cnt);
                    curchar=v[i][j];cnt=1;


            }


            if(i!=0 && g!=prev) {f=1;break;}
            else prev=g;
        }

        if(f)
        {printf("Case #%d: %s\n",cas,"Fegla Won");continue;}

            int ans=0;
            int charcnt=acnt[0].size();
            int k=0;
            int max1[1000],min1[1000];


            for(int i=0;i<charcnt;i++)
            {
              int max2=INT_MIN;
              for(int j=0;j<n;j++)
              max2=max(acnt[j][i],max2);
              max1[i]=max2;
            }

             for(int i=0;i<charcnt;i++)
            {
              int min2=INT_MAX;
              for(int j=0;j<n;j++)
              min2=min(acnt[j][i],min2);
              min1[i]=min2;
            }
            //for(int i=0;i<charcnt;i++)
              //printf("%d %d\n",min1[i],max1[i]);
            for(int i=0;i<charcnt;i++)
               ans+=(max1[i]-min1[i]);
            printf("Case #%d: %d\n",cas,ans);



    }return 0;
}
