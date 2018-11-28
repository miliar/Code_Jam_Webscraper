#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <climits>
#include <cstdio>
#include <set>
#include <unordered_map>
#include <iomanip>
using namespace std;
#define db(a) (cout << (#a) << " = " << (a) << endl)
typedef long long ll;

int N;/*
vector<vector<int>> lists;
vector<int> erg;
#define INF (INT_MAX/2)

int G[124][124];

bool foo(int d)
{
	if(d>=N) return true;
	int starta, startb;
	vector<int> index;
	bool missing = false;
	if(d == 0)
	{
		int minv = INF;
		for(size_t i=0;i<lists.size();i++)
		{
			auto l = lists[i];
			if(minv >= l[0])
			{
				minv = l[0];			
				index.push_back(i);
			}
		}
		if(index.size() < 2) missing = true;
		starta = startb = minv;
	}
	else
	{
		starta = G[0][d];
		startb = G[d][0];		
		for(size_t i=0;i<lists.size();i++)
		{
			auto l = lists[i];
			if(l[0] == starta || l[0] == startb) index.push_back(i);
		}
		if(starta == -1 || startb == -1)
		{
			int sea = lists[index[0]][d];
			for(size_t i=0;i<lists.size();i++)
			{
				auto l = lists[i];
				if(l[d] == sea && int(i) != index[0])
				{
					index.push_back(i);
				}
			}
		}
		if(index.size() < 2) missing = true;
	}
db(d);
db(missing);
db(starta);db(startb);
db(index[0]);
if(!missing)db(index[1]);
	
	bool fail = false;
	for(int i=0;i<N;i++) if(i<d && G[i][d] != -1 && G[i][d] != lists[index[0]][i]) {fail=true;break;}
	if(!missing) for(int i=0;i<N;i++) if(i<d && G[d][i] != -1 && G[d][i] != lists[index[1]][i]) {fail=true;break;}
	if(!fail)
	{
		for(int i=0;i<N;i++) G[i][d] = lists[index[0]][i];
		if(!missing) for(int i=0;i<N;i++) G[d][i] = lists[index[1]][i];
		else  for(int i=d+1;i<N;i++) G[d][i] = -1;
		if(foo(d+1))
		{
			if(missing) for(int i=0;i<N;i++) erg.push_back(G[d][i]);
			return true;
		}		
	}
	
	for(int i=0;i<N;i++) if(i<d && G[d][i] != -1 && G[d][i] != lists[index[0]][i]) {fail=true;break;}
	if(!missing) for(int i=0;i<N;i++) if(i<d && G[i][d] != -1 && G[i][d] != lists[index[1]][i]) {fail=true;break;}
	if(!fail)
	{
		for(int i=0;i<N;i++) G[d][i] = lists[index[0]][i];
		if(!missing) for(int i=0;i<N;i++) G[i][d] = lists[index[1]][i];
		else  for(int i=d+1;i<N;i++) G[i][d] = -1;
		if(foo(d+1))
		{
			if(missing) for(int i=0;i<N;i++) erg.push_back(G[i][d]);
			return true;
		}
	}
db("fail");	
	return false;	
}

int main()
{
  ios_base::sync_with_stdio(false);
	int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		lists.clear();		
		erg.clear();
		cin>>N;
		for(int i=0;i<2*N-1;i++)
		{
			vector<int> v;
			for(int j=0;j<N;j++) {int x;cin>>x;v.push_back(x);}
			lists.push_back(v);
		}
		
		foo(0);		
		
		cout << "Case #" << t+1 << ":";
		for(size_t i=0;i<erg.size();i++) cout << " " << erg[i];
		cout << "\n";
	}
  return 0;
}*/

int counter[3000];

int main()
{
  ios_base::sync_with_stdio(false);
	int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		cin>>N;
		for(int i=0;i<3000;i++) counter[i] = 0;		
		for(int i=0;i<2*N-1;i++) for(int j=0;j<N;j++) {int x;cin>>x;counter[x]++;}
		vector<int> erg;
		for(int i=0;i<3000;i++) if(counter[i]%2==1) erg.push_back(i);
		cout << "Case #" << t+1 << ":";
		for(size_t i=0;i<erg.size();i++) cout << " " << erg[i];
		cout << "\n";
	}
  return 0;
}
