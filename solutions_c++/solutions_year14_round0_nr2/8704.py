//coder: handa.vikalp
#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;

#define st          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())

int main(int argc, char const *argv[])
{
	FILE *input = freopen("B-large.in","r", stdin);
	FILE *output = freopen("B-large-0.out", "w", stdout);

	int T, flag=1;
	scanf("%d",&T);
	double C, F, X, minTime=0.0,rate=2,bag, projTime=0.0;
	for(int t = 1; t<=T; ++t)
	{
		bag = 0.0;
		minTime= 0.0;
		rate = 2.0;
		scanf("%lf%lf%lf", &C, &F, &X);
		while(bag!=X)
		{
			if(C>X)
			{
				bag = X;
				minTime += X/rate;
			}
			else
			{

				if( minTime+(X/rate) > minTime+(C/rate)+(X/(rate+F)))
				{
					minTime += C/rate;
					rate += F;
				}
				else
				{
					bag = X;
					minTime += X/rate;
				}

			}
		}
		printf("Case #%d: %.7f\n", t, minTime);
	}
	return 0;
}
