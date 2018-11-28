#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<map>
#include<set>
#include<cmath>
#include<deque>

using namespace std;

#define mp make_pair
#define pb push_back
#define forn(i,n) for(int i=0;i<(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

vector<string> get(string x)
{
    vector<string>ans;
    forn(i,x.size()+1)
    {
        ans.pb(x.substr(0,i));
    }
    return ans;
}

int main()
{
    int T;
    cin>>T;
    forn(t,T)
    {
        int m,n;
        cin>>m>>n;
        vector<string>s(m);
        forn(i,m)cin>>s[i];
        int c=pow(n,m);
        int ma=-1;
        int cm=0;
        forn(i,c)
        {
            int u=i;
            vector<set<string> >p(n);
            //cout<<"--------------------"<<endl;
            forn(j,m)
            {
                vector<string>r=get(s[j]);
                //cout<<u%n<<" "<<s[j]<<endl;
                forn(k,r.size())p[u%n].insert(r[k]);
                u/=n;
            }
            int cc=0;
            forn(j,n)cc+=p[j].size();
            //cout<<cc<<endl;
            if(cc==ma)cm+=1;
            if(cc>ma)
            {
                ma=cc;
                cm=1;
            }
        }
        cout<<"Case #"<<t+1<<": "<<ma<<" "<<cm<<endl;
    }
}
