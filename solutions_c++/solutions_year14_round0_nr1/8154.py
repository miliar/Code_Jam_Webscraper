#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <ctype.h>
#include <bitset>
#include <assert.h>
 
using namespace std;
 
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define IFOR(i, a, b) for(int i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(int i=(a); i<(b); i+=(c))
 
#define SS ({int x;scanf("%d", &x);x;})
#define SI(x) ((int)x.size())
#define PB(x) push_back(x)
#define MP(a,b) make_pair(a, b)
#define SORT(a) sort(a.begin(),a.end())
#define ITER(it,a) for(typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define ALL(a) a.begin(),a.end()
#define INF 1000000000
#define V vector
#define S string
#define FST first
#define SEC second
typedef V<int> VI;
typedef V<S> VS;
typedef long long LL;
typedef pair<int, int> PII;
int main(){
	int ite,n=1;
	int ar[4][4], ar1[4][4];
	scanf("%d",&ite);
	while(ite--){
		int r;
		scanf("%d",&r);
		for(int i=0;i<4;i++) for(int j=0;j<4;j++) scanf("%d",&ar[i][j]);
		int r1;
		scanf("%d",&r1);
		for(int i=0;i<4;i++) for(int j=0;j<4;j++) scanf("%d",&ar1[i][j]);
		int fl=0,k=0;
		r--;r1--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(ar[r][i]==ar1[r1][j]){
					fl++;
					k=ar[r][i];
				}
			}
		}
		if(fl==1){
			printf("Case #%d: %d\n",n++,k);
			continue;
		}
		if(fl>1){
			printf("Case #%d: Bad magician!\n",n++);
		}
		else
			printf("Case #%d: Volunteer cheated!\n",n++);	
	}
}

