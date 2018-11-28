#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> PI;
typedef vector<int> VI;
typedef long long LL;

#define FOR(i,a,b) for(register int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define mod 1000000007
#define MP make_pair
#define INF mod
int main()
{
#ifndef ONLINE_JUDGE
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
#endif
    ios_base::sync_with_stdio(0);
    int t,n;
    cin>>t;
    FOR(T,1,t+1)
    {
        cout<<"Case #"<<T<<": ";
        cin>>n;
        string s[n];
        REP(i,n) cin>>s[i];
        vector<char> x,y;
        bool f=1;
        REP(i,s[0].length()) x.PB(s[0][i]);
        auto it=unique(x.begin(),x.end());
        x.resize(it-x.begin());
        int p[n][101];
        REP(i,n) REP(j,101) p[i][j]=1;
        REP(k,n){
        for(int i=1,j=0; i<s[k].length();)
        {
            while(i<s[k].length() and s[k][i]==s[k][i-1])
            {
                i++;
                p[k][j]++;
            }
            //p[k][j]++;
            i++;
            j++;
            //if(i>=s[k].length() and s[k].length()>1 and s[k][s[k].length()-1]==s[k][s[k].length()-2]) p[k][j-1]++;
        }
           // if(n>1 and s[k][n-1]==s[k][n-2]) p[k][]
        }
        FOR(j,1,n)
        {
            REP(i,s[j].length()) y.PB(s[j][i]);
            it=unique(y.begin(),y.end());
            y.resize(it-y.begin());
            if(x!=y)
            {
                f=0;
                break;
            }
            y.clear();
        }
        if(!f)
        {
            cout<<"Fegla Won\n";
            continue;
        }
        else
        {
            int ans=0;
            REP(j,x.size())
            {
                double S=0;
                //cout<<endl;REP(i,n) cout<<p[i][j]<<' ';
                REP(i,n) S+=p[i][j];
                S=S/n;
                int tmp=floor(S+0.5);
               // cout<<tmp<<' ';
                REP(i,n) ans+=abs(p[i][j]-tmp);
            }
            cout<<ans<<endl;
        }
    }
    return 0;
}
