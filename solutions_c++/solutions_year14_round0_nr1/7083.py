#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <sstream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <set>
#include <map>
#include <queue> 

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define pb push_back
#define mp make_pair
#define sz size()
#define ln length()
#define forr(i,a,b)                 for(int i=a;i<b;i++)
#define rep(i,n)                    forr(i,0,n) 
#define all(v)                      v.begin(),v.end()    
#define uniq(v)                     sort(all(v));v.erase(unique(all(v)),v.end())
#define clr(a)                      memset(a,0,sizeof a)
    
#define debug                       if(1)
#define debugoff                    if(0)    

#define print(x)                 cerr << x << " ";    
#define pn()                     cerr << endl;
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;

#define MAX 100010
#define MOD 1000000007
map<int,int> m;
vector<int> v;
int main()
{
    ios::sync_with_stdio(false);
    int t,n,size,var,cases = 0;;
    cin>>t;
    while(t--)
    {
        cases++;
        m.clear();
        v.clear();
        cin>>n;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                cin>>var;
                if(i == n)
                    m[var] = 1;
            }
        }
        cin>>n;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                cin>>var;
                if(i == n)
                {
                    if(m[var])
                        v.pb(var);
                }
            }
        }

        size = v.size();
        if(size == 0)
            cout<<"Case #"<<cases<<": Volunteer cheated!"<<endl;
        else if(size >1)
            cout<<"Case #"<<cases<<": Bad magician!"<<endl;
        else if(size == 1)
            cout<<"Case #"<<cases<<": "<<v[0]<<endl;

    }
    return 0; 
}
