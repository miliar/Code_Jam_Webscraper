#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <cstring>
#include <limits>

using namespace std;

#define FOR(I,A,B) for(int I= (A); I<(B); ++I)
#define REP(I,N) FOR(I,0,N)
#define S(N) scanf("%d", &N)
#define SL(N) scanf("%lld", &N)
#define PB push_back
#define MP make_pair
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define cell pair<int,int>
#define edge pair<int, cell>
typedef vector<string> vs;
typedef long long int LL;
typedef vector<int> vi;
typedef vector<LL> vii;
int main()
{
	int t;S(t);
	int s[5]={1,4,9,121,484};
	REP(c,t)
	{
		int d;
		printf("Case #%d: ",c+1);
		int a,b;S(a);S(b);
		int x,y;
		b++;
		for(x=0;x<5;x++)
			if(a<=s[x])break;
		for(y=0;y<5;y++)
			if(b<=s[y])break;
		printf("%d\n",y-x);
	}
	return 0;
}  
