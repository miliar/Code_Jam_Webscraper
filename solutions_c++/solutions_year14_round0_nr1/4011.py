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

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vstr;
typedef long long LL;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("salida.out","w",stdout);
	int t,n,v,c;
	cin>>t;	
	F(ii,t)
	{
		set<int> vv;
		vector<int> gg;
		F(k,2)
		{
			cin>>n;
			F(i,4)
			{
				F(j,4)
				{
					cin>>v;
					c=vv.S;
					if(i+1 == n)
					{
						vv.insert(v);
						if(c+1 != vv.S) gg.PB(v);
					}
				}
			}
		}
		if(8-vv.S > 1)printf("Case #%d: Bad magician!\n", ii+1);
		else if(8-vv.S < 1)printf("Case #%d: Volunteer cheated!\n", ii+1);
		else printf("Case #%d: %d\n", ii+1,gg[0]);
		
	}
}
