#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <cassert>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
typedef pair<int,P> P1;
typedef pair<P,P> P2;
#define pu push
#define pb push_back
#define mp make_pair
#define eps 1e-7
#define INF 1000000000
#define fi first
#define sc second
#define rep(i,x) for(int i=0;i<x;i++)
#define SORT(x) sort(x.begin(),x.end())
#define ERASE(x) x.erase(unique(x.begin(),x.end()),x.end())
#define POSL(x,v) (lower_bound(x.begin(),x.end(),v)-x.begin())
#define POSU(x,v) (upper_bound(x.begin(),x.end(),v)-x.begin())
int main()
{
	int t; cin >> t;
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		int r,c; cin >> r >> c;
		string f[105];
		for(int j=0;j<r;j++) cin >> f[j];
		int cnt = 0;
		for(int a=0;a<r;a++)
		{
			for(int b=0;b<c;b++)
			{
				if(f[a][b] == '.') continue;
				int gx,gy;
				if(f[a][b] == '^') gx=-1,gy=0;
				if(f[a][b] == '>') gx=0,gy=1;
				if(f[a][b] == '<') gx=0,gy=-1;
				if(f[a][b] == 'v') gx=1,gy=0;
				int cx=a+gx,cy=b+gy;
				while(0<=cx&&cx<r&&0<=cy&&cy<c)
				{
					if(f[cx][cy] != '.') goto OK;
					cx+=gx; cy+=gy;
				}
				cnt++;
				for(int x=0;x<c;x++)
				{
					if(x != b && f[a][x] != '.') goto OK;
				}
				for(int x=0;x<r;x++)
				{
					if(x != a && f[x][b] != '.') goto OK;
				}
				cout << "IMPOSSIBLE" << endl; goto end;
				OK:;
				//cout << a << " " << b << endl;
			}
		}
		cout << cnt << endl;
		end:;
	}
}