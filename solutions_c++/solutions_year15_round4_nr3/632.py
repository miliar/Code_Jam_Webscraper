#include <vector>
#include <map>
//#include <unordered_map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

#define sz(a) (int)(a.size())
#define len(a) (int)(a.length())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

map<string,int> my;
int has[11111][2];
const int INF=1<<29;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,cas=1;
	cin>>t;
	while(t--)
	{
		my.clear();
		cout<<"Case #"<<cas++<<": ";
		int n,cnt=0;
		cin>>n;
		string line;
		vector<string> lines;
		cin.ignore();
		for(int i=0;i<n;++i)
		{
			getline(cin,line);
			lines.pb(line);
		}
		vector<vector<int> > mod(n);
		for(int i=0;i<n;++i)
		{
			stringstream ss(lines[i]);
			string x;
			while(ss>>x)
			{
				if(!my.count(x)) my[x]=cnt++;
				mod[i].pb(my[x]);
			}
		}
		memset(has,0,sizeof(has));
		for(int i=0;i<sz(mod[0]);++i) has[mod[0][i]][0]=1;
		for(int i=0;i<sz(mod[1]);++i) has[mod[1][i]][1]=1;
		int already=0;
		for(int i=0;i<11111;++i) if(has[i][0]&&has[i][1]) ++already;
		int left=n-2;
		int answer=INF;
		for(int mask=0;mask<(1<<left);++mask)
		{
			int now_count=0;
			for(int j=0;j<left;++j)
			{
				int i=j+2;
				int mark=(mask&(1<<j))!=0?1:0;
				for(int k=0;k<sz(mod[i]);++k)
				{

					if(has[mod[i][k]][mark]==1||has[mod[i][k]][mark]==mask+2) continue;
					has[mod[i][k]][mark]=mask+2;
					if(has[mod[i][k]][mark^1]==1||has[mod[i][k]][mark^1]==mask+2) ++now_count;
				}
			}
			answer=min(answer,now_count+already);
		}
		cout<<answer<<'\n';

	}

	return 0;
}