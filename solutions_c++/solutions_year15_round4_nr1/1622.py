#include<bits/stdc++.h>
using namespace std;

typedef long long int LL;

#define inp_s     ios_base::sync_with_stdio(false)
#define DRT()     int test_case;cin>>test_case;while(test_case--)

#define VI        vector<int>
#define VS        vector<string>
#define VLL       vector<LL>
#define PII       pair<int,int>
#define all(c)    c.begin(),c.end()
#define sz(c)     c.size()
#define clr(c)    c.clear()
#define msi       map<string,int>
#define msit      map<string,int>::iterator
#define pb        push_back
#define mp        make_pair

#define GI(x)     scanf("%d",&x)

#define FOR(i,a,b)      for(int i=a;i<b;i++)
#define RFOR(i,a,b)     for(int i=b-1;i>=a;i--)

#define gcd(a,b)  __gcd(a,b)
#define MOD       1000000007
#define EPS       1E-10

#define PI  acos(-1)

#define endn	"\n"

#define CASE(x)   fout << "Case #" << x << ": ";

int visited[101][101];
char arr[101][101];
int r,c;

int laser_hai(int i,int j,int dx,int dy)
{
	int ret = 0;
	i += dx;
	j += dy;
	while(i >= 0 && i < r && j >= 0 && j < c)
	{
		if(arr[i][j] != '.') return 0;
		i += dx;
		j += dy;
	}
	return 10000000;
}

int main()
{
	ifstream fin("A.in");
	ofstream fout("out.txt");
	int t;
	fin >> t;
	for(int ii = 1; ii <= t; ii++)
	{
		fin >> r >> c;
		FOR(i,0,r) fin >> arr[i];
		FOR(i,0,r) FOR(j,0,c) visited[i][j] = 0;
		int ans = 0;
		FOR(i,0,r) FOR(j,0,c)
		{
			if(ans > 1000000) break;
			if(arr[i][j] != '.')
			{
				int ret = 10000000;
				ret = min(ret , laser_hai(i,j,0,1) + (arr[i][j] != '>'));
				ret = min(ret , laser_hai(i,j,0,-1) + (arr[i][j] != '<'));
				ret = min(ret , laser_hai(i,j,-1,0) + (arr[i][j] != '^'));
				ret = min(ret , laser_hai(i,j,1,0) + (arr[i][j] != 'v'));
				ans += ret;
			}
		}
		CASE(ii);
		if(ans > 1000000) fout << "IMPOSSIBLE" << endl;
		else fout << ans << endl;
	}
	return 0;
}