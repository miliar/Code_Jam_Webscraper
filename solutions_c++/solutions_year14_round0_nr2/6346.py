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
int main()
{
	int t;
	cin >> t;
	for(int i=0;i<t;i++)
	{
		double c,f,x;
		cin  >> c >> f >> x;
		double ans=INF,res=0.0;
		double now=2.0;
		while(1)
		{
			if(res>ans)break;
			ans=min(ans,res+x/now);
			res+=c/now;
			now+=f;
		}
		printf("Case #%d: %lf\n",i+1,ans);
	}
	return 0;
}
