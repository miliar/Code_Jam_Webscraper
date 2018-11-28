#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <utility>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <climits>
#include <cassert>
using namespace std;
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long ll;
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define EACH(t,i,c) for(t::iterator i=(c).begin(); i!=(c).end(); ++i)
const double EPS = 1e-10;
const double PI  = acos(-1.0);

typedef multiset<int> si;
int dp[1<<20]={};
const int OK=1;
const int NG=2;
int keysYouOwn[1<<20][20];
vi validTrack;

int dfs(int mask,int n,vi &track,vi &keyRequired){
	if (dp[mask])
	{
		return dp[mask];
	}
	if (mask==(1<<n)-1)
	{
		validTrack=track;
		return OK;
	}
	int ret=NG;
	for (int i = 0; i < n; i++)
	{
		if((mask&(1<<i))==0&&keysYouOwn[mask][keyRequired[i]]){
			vi nTrack(track);
			nTrack.push_back(i);
			int d=dfs((mask|(1<<i)),n,nTrack,keyRequired);
			if(d==OK){
				ret=OK;
				break;
			}
		}
	}
	return dp[mask]=ret;
}

int main() {
	int t;
	cin>>t;
	for (int test = 1; test <= t; test++)
	{
		int k,n;
		cin>>k>>n;
		vi initialKeys(40);
		for (int i = 0; i < k; i++)
		{
			int key;
			cin>>key;
			key--;
			initialKeys[key]++;
		}

		vvi keysInChest(n,vi());
		vi keyRequired(n);
		for (int i = 0; i < n; i++)
		{
			int t,k;
			cin>>t>>k;
			t--;
			keyRequired[i]=t;
			for (int j = 0; j < k; j++)
			{
				int key;
				cin>>key;
				key--;
				keysInChest[i].push_back(key);
			}
		}

		validTrack=vi();
		for (int i = 0; i < (1<<n); i++)
		{
			dp[i]=0;
			for (int j = 0; j < 40; j++)
			{
				keysYouOwn[i][j]=initialKeys[j];
			}
			for (int j = 0; j < n; j++)
			{
				if ((i&(1<<j))!=0)
				{
					for (int k = 0; k < keysInChest[j].size(); k++)
					{
						keysYouOwn[i][keysInChest[j][k]]++;
					}
				}
			}
			for (int j = 0; j < n; j++)
			{
				if ((i&(1<<j))!=0)
				{
					if(keysYouOwn[i][keyRequired[j]]){
						keysYouOwn[i][keyRequired[j]]--;
					}
				}
			}
		}

		int res=dfs(0,n,vi(),keyRequired);
		cout<<"Case #"<<test<<": ";
		if(res==OK){
			for (int i = 0; i < validTrack.size(); i++)
			{
				cout<<validTrack[i]+1<<" ";
			}
			cout<<endl;
		}else{
			cout<<"IMPOSSIBLE"<<endl;
		}
	}
}