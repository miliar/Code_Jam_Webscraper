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
	freopen("A-large.in","r",stdin);
	freopen("salida.out","w",stdout);
	int t,n,m;
	long long s, sl;
	cin>>t;
	F(i,t)
	{
		cin>>n;
		if(n == 0) {
			printf("Case #%d: INSOMNIA\n",i+1);
		} else {
			sl = 0;
			string num = "0123456789";
			for(int j=1; ;j++) {
				stringstream ss;
				s = n * j;
				sl = s;
				ss << s;
				string st;
				st = ss.str();
				F(k,st.S) {
					int r = num.find(st[k]);
					if(r != -1) num.erase (num.begin()+r);
				}
				if( num.S == 0) break;
			}
			printf("Case #%d: %lld\n",i+1, sl);
		}
		
	}
}
