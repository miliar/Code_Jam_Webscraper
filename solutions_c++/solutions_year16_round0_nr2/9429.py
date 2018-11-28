#pragma comment(linker,"/STACK:268435456")
#include <iostream>
#include <iomanip>
#include <fstream>
#include <set>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <climits>
#include <cstring>
#include <string>
#include <sstream>
#include <bitset>
#include <iterator>
#include <list>
#include <ctime>
#include <functional>
#include <numeric>
#include <cassert>


#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for((cont)::iterator (it)=(v).begin();(it)!=(v).end();++(it))
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define VCPRINT(v) for(int iii = 0;iii < (v).size();iii++) cout<<(v)[iii]<<" ";cout<<endl;
#define SETPRINT(v,cont) for((cont)::iterator iiit = (v).begin();iiit != (v).end();iiit++) cout<<*iiit<<" ";cout<<endl;

bool ascending (int i,int j) { return (i<j); }
bool descending (int i,int j) { return (i>j); }

typedef long long ll;
typedef unsigned long long ull;
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PULI pair<unsigned long long,int>
#define PIL pair<int,long long>
#define PSI pair<string,int>
#define PSS pair<string,string>
#define PDD pair<double,double>
#define PIB pair<int,bool>
typedef long double ld;
#define PLI pair<ll,int>

using namespace std;

bool visited[1<<11];

vector<int> G[1<<11];
int dp[1<<11];

int num(string s)
{
    int ret = 0;
    for(int i = s.size()-1;i>=0;i--)
    {
        ret <<= 1;
        ret += (s[i]=='-');
    }
    return ret;
}

string str(int num)
{
    string ret = "";
    while(num)
    {
        if(num%2==1) ret+='-';
        else ret += '+';
        num/=2;
    }
    return ret;
}

string rev(string & s,int i)
{
    string ret = s;
    reverse(ret.begin(),ret.begin()+i+1);
    FR(j,i+1)
    {
        if(ret[j]=='-') ret[j]='+';
        else ret[j]='-';
    }
    return ret;
}

void graph()
{
    dp[0]=0;
    FOR(v,1,1<<10) {
        string s = str(v);
        for(int i = 0;i < s.size();i++)
        {
            int u = num(rev(s,i));
            G[u].push_back(v);
            G[v].push_back(u);
        }
    }
}

void bfs()
{
    queue<int> q;
    FR(i,1<<11) dp[i]=1000*1000;
    dp[0]=0;
    visited[0]=true;
    q.push(0);
    while(q.size())
    {
        int v = q.front();q.pop();
        FR(i,G[v].size())
        {
            dp[G[v][i]] = min(dp[v]+1,dp[G[v][i]]);
            if(!visited[G[v][i]]) {
                visited[G[v][i]]=true;
                q.push(G[v][i]);
            }
        }
    }
}




int main()
{
    ifstream cin("a.in");
    ofstream cout("a.out");
    int T;cin>>T;
    graph();
    bfs();
    FOR(_,1,T+1)
    {
        CLR(visited,0);
        cout<<"Case #"<<_<<": ";
        string s;cin>>s;
        cout<<dp[num(s)]<<endl;
    }
}