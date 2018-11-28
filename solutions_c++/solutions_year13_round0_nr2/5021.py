// B - Lawnmower
// wahyuoi
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <cmath>
using namespace std;
#define ll int
#define INF 1000000000
#define debug puts("DEBUUGG")
#define vi vector<ll>
#define pii pair<ll,ll>
#define vii vector<pii>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define rep(a,b,c) for(a=b;a<c;a++)
#define repe(a,b,c) for(a=b;a<=c;a++)
#define repd(a,b,c) for(a=b-1;a>=c;a--)
#define ALL(a) (a.begin(),a.end())
int a[111][111];
int n,m;
bool datar(int r){
	for (int i=0; i<m; ++i)
	{
		if (a[r][i]==2)
		{
			return false;
		}
	}
	return true;
}
bool turun(int c){
	for (int i=0;i<n ;++i )
	{
		if (a[i][c]==2)
		{
			return false;
		}
	}
	return true;
}
void solve(int tc){
	bool ret = true;
	scanf("%d %d\n",&n,&m);
	for (int i=0;i<n ;++i )
	{
		for (int j=0; j<m; ++j)
		{
			scanf("%d",&a[i][j]);
		}
	}
	for (int i=0;i<n ;++i )
	{
		for (int j=0; j<m; ++j)
		{
			if (a[i][j]==1)
			{
				ret &= (datar(i) || turun(j));
			}
		}
	}
	if (ret)
	{
		printf("Case #%d: YES\n",tc);
		fprintf(stderr,"Case #%d: YES\n",tc);
	} else {
		printf("Case #%d: NO\n",tc);
		fprintf(stderr,"Case #%d: NO\n",tc);		
	}
}
int main(){
	int nn;
	scanf("%d",&nn);
	for (int tc=1;tc<=nn ;++tc )
	{
		solve(tc);
	}
}
