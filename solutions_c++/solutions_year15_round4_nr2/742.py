#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <complex>
#include <string>
#include <sstream>
#include <algorithm>
#include <numeric>
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
#define rep(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define repn(i,a,n) for(int (i)=(a);(i)<(int)(n);(i)++)
#define EQ(a,b) (abs((a)-(b))<eps)
int N;
double X,V;
double R[105],C[105];
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++)
	{
		cin >> N >> V >> X;
		double Cmax = 0.0;
		double Cmin = 150.0;
		for(int i=0;i<N;i++)
		{
			cin >> R[i] >> C[i];
			Cmax = max(Cmax,C[i]);
			Cmin = min(Cmin,C[i]);
		}
		if(Cmax < X || Cmin > X)
		{
			printf("Case #%d: IMPOSSIBLE\n",t+1);
			continue;
		}
		if(N==1)
		{
			printf("Case #%d: %.12f\n",t+1,V/R[0]);
			continue;
		}
		if(C[0]==C[1])
		{
			printf("Case #%d: %.12f\n",t+1,V/(R[0]+R[1]));
			continue;
		}
		double ans = 0.0;
		double x = (X-C[1])*V/(C[0]-C[1])/R[0];
		double y = (C[0]-X)*V/(C[0]-C[1])/R[1];
		//cout << x << ' ' << y << endl;
		ans = max(x,y);
		printf("Case #%d: %.12f\n",t+1,ans);
	}
	return 0;
}
