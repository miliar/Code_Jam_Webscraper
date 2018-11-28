#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

#define MAXS 205

int T, K, N;
int kstart[MAXS];
vector<int> chest[MAXS];
int arr[MAXS], visit[MAXS], q[MAXS];
bool flag;

int keys[MAXS];
bool ok[(1<<20)+5];

bool dfs(int n, int knum, int mask)
{
	if(flag)
		return true;
	if(n == N)
	{
		flag = true;
		return true;
	}
	if(knum == 0)
		return false;
	if(ok[mask] == false)
		return false;

	for(int i = 0; i < N && !flag; ++i)
	{
		if(visit[i])
			continue;
		if(keys[arr[i]])
		{
			visit[i] = 1;
			q[n] = i;
			int m = (mask | (1<<i));
			
			keys[arr[i]] -= 1; 
			for(int j = 0; j < chest[i].size(); ++j)
				keys[chest[i][j]]++;
			ok[m] = dfs(n+1, knum-1+chest[i].size(), m);
			for(int j = 0; j < chest[i].size(); ++j)
				keys[chest[i][j]]--;
			keys[arr[i]] += 1;
			
			visit[i] = 0;
		}
	}
	return false;
}



int main()
{
	freopen("F:\\download\\4_1.txt", "r", stdin);
	freopen("F:\\download\\4_1out.txt", "w", stdout);
	cin>>T;
	int id = 1;
	while(T--)
	{
		memset(chest, 0, sizeof(chest));
		memset(arr, 0, sizeof(arr));
		memset(visit, 0, sizeof(visit));
		memset(q, 0, sizeof(q));
		memset(keys, 0, sizeof(keys));
		memset(ok, true, sizeof(ok));
		flag = false;
		for(int i = 0; i < MAXS; ++i)
			chest[i].clear();
		cin>>K>>N;
		int ks;
		for(int i = 0; i < K; ++i)
		{
			cin>>ks;
			keys[ks]++;
		}
		int kt, nk;
		for(int i = 0; i < N; ++i)
		{
			cin>>kt>>nk;
			arr[i] = kt;
			for(int j = 0; j < nk; ++j)
			{
				int a;
				cin>>a;
				chest[i].push_back(a);
			}
		}
		
		dfs(0, K, 0);

		if(flag)
		{
			cout<<"Case #"<<id<<":";
			for(int i = 0; i < N; ++i)
				cout<<" "<<q[i]+1;
			cout<<endl;
		}
		else
		{
			cout<<"Case #"<<id<<": IMPOSSIBLE"<<endl;
		}
		id++;

	}
	return 0;
}