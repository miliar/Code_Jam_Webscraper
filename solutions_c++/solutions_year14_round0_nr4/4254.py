#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;

#define INF (int)1e9
#define MP make_pair
#define PB push_back
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int) (x).size())
#define iter(x) __typeof(x.begin())
#define REP(i,x) for(iter(x)i=x.begin();i!=x.end();i++)
#define MAXN 1010
int visited[MAXN];
int main() {
	int TestCases;
	cin>>TestCases;
	for(int t = 1;t<=TestCases;t++)
	{
		int N;
		cin>>N;
		vector<double> Naomi(N),Ken(N);
		for(int i = 0;i<N;i++)
			scanf("%lf",&Naomi[i]);
		for(int i = 0;i<N;i++)
			scanf("%lf",&Ken[i]);
		sort(ALL(Naomi));
		sort(ALL(Ken));
		memset(visited,false,sizeof(visited));
		int Score = 0;
		for(int i = 0;i<N;i++)
		{
			int val = Ken[i];
			for(int j = 0 ;j<N;j++)
			{
				if(visited[j])
					continue;
				if(Naomi[j]>Ken[i])
				{
					visited[j] = true;
					Score+=1;
					break;
				}
			}
		}
		cout<<"Case #"<<t<<": ";
		cout<<Score<<" ";
		//Case1 : The Straight Game
		Score = 0;
		memset(visited,false,sizeof(visited));
		for(int i = 0;i<N;i++)
		{
			int val = Naomi[i];
			for(int j = 0;j<N;j++)
			{
				if(visited[j])
					continue;
				if(Ken[j]>Naomi[i])
				{
					Score+=1;
					visited[j] = true;
					break;
				}

			}
		}
		//Case 2 : Deceitful Game
		cout<<N-Score<<endl;
	}
	return 0;
}
