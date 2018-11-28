#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <complex>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <functional>
#include <iostream>
#include <map>
#include <set>
using namespace std;
typedef pair<int,int> P;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
#define pu push
#define pb push_back
#define mp make_pair
#define eps 1e-9
#define INF 2000000000
#define sz(x) ((int)(x).size())
#define fi first
#define sec second
#define SORT(x) sort((x).begin(),(x).end())
#define all(x) (x).begin(),(x).end()
#define EQ(a,b) (abs((a)-(b))<EPS)
int f1[5][5],f2[5][5];
int main()
{
	int T;
	cin >> T;
	for(int t=0;t<T;t++)
	{
		int f,s;
		cin >> f;
		f--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin >> f1[i][j];
			}
		}
		cin >> s;
		s--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin >> f2[i][j];
			}
		}
		vector<int> v;
		for(int i=0;i<4;i++)v.pb(f1[f][i]);
		sort(v.begin(),v.end());
		bool ex=false;
		bool bad=false;
		int ans=0;
		for(int i=0;i<4;i++)
		{
			if(binary_search(v.begin(),v.end(),f2[s][i]))
			{
				if(ex)bad=true;
				else ex=true,ans=f2[s][i];
			}
		}
		if(!ex)
		{
			printf("Case #%d: Volunteer cheated!\n",t+1);
		}
		else if(bad)
		{
			printf("Case #%d: Bad magician!\n",t+1);
		}
		else
		{
			printf("Case #%d: %d\n",t+1,ans);
		}
	}
	return 0;
}

