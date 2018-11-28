#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <malloc.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <stdint.h>
#include <unistd.h>
#include <ctime>
#include <climits>
using namespace std;

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()
#define T           top()
#define P           pop()
#define NL 			printf("\n")

/*typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vstr;
typedef long long LL;*/

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("salida.out","w",stdout);
	int t,n,vi,vl,k;
	double v;
	cin>>t;
	F(i,t)
	{
		vector<double> na;
		vector<double> ke;
		cin>>n;vi=0;vl=0;
		F(j,n){scanf("%lf",&v);na.PB(v);}sort(ALL(na));
		F(j,n){scanf("%lf",&v);ke.PB(v);}sort(ALL(ke));
		//F(j,n)cout<<na[j]<<" ";NL;
		//F(j,n)cout<<ke[j]<<" ";NL;
		k=0;
		F(j,na.S)
		{
			if(na[j]>ke[k])
			{
				vi++;
				k++;
			}
		}
		k=0;
		F(j,ke.S)
		{
			if(ke[j]>na[k])
			{
				vl++;
				k++;
			}
		}
		printf("Case #%d: %d %d\n", i+1,vi,ke.S-vl);	
	}
	
}
