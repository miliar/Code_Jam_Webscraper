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
int D;
int P[1010];
bool C(int X)
{
	for(int i=1;i<=X;i++)
	{
		int sum = 0;
		for(int j=0;j<D;j++)sum += (P[j]-1)/i;
		if(sum<=X-i)return true;
	}
	return false;
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++)
	{
		memset(P,0,sizeof(P));
		scanf("%d",&D);
		for(int i=0;i<D;i++)scanf("%d",&P[i]);
		int l = 0,r = 1000005;
		while(r-l>1)
		{
			int mid = (l+r)/2;
			if(C(mid))r=mid;
			else l = mid;
		}
		printf("Case #%d: %d\n",t+1,r);
	}
	return 0;
}
