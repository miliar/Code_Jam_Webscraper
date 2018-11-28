#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
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
#define PB          push_back
#define MP          make_pair
#define MS(a, v)	memset(a, v, sizeof a)
#define ALL(x)      x.begin(), x.end()
#define UNIQUE(c)	(c).resize(unique(ALL(c)) - (c).begin())
#define NL 			printf("\n")
#define INF 		(1 << 28)
#define S           size()
#define T           top()
#define P           pop()
#define foreach(IT,C) for(typeof(C.begin())IT=C.begin();IT!=C.end();IT++)
#define length(x)	(sizeof(x)/sizeof(x[0]))

const double PI = acos(-1.0);
const double PI2 = 2 * acos(0.0);
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long   LL;

void busca(int c1[], int c2[], int r1, int r2,int turn){
int t1=r1*4;int t2=r2*4; vi v1,v2;
FOR(z,(t1-4),t1){
v1.push_back(c1[z]);
v2.push_back(c1[z]);
}
FOR(z,(t2-4),t2){
v1.push_back(c2[z]);
v2.push_back(c2[z]);
}
sort(ALL(v1)); UNIQUE(v1);
int ta=(int)v1.size();
if(8==ta){
printf("Case #%d: Volunteer cheated!\n",turn);
} else if(7==ta){
	sort(ALL(v2)); int p;
for(int w=0;w<(int)v2.size();w++){
	if(v2[w]==v2[w+1]){
		p=w;
		break;
	}
}
printf("Case #%d: %d\n", turn, v2[p]);
} else if(7>ta && 0<ta){
printf("Case #%d: Bad magician!\n",turn);
}

}

int main (){
	int a=0,t,r1,r2;
	int c1[16];
	int c2[16];
//freopen("inMagicTrick.txt","r",stdin);
scanf("%d", &t);
while(t--){
scanf("%d",&r1);
F(i,16){scanf("%d",&c1[i]);}
scanf("%d",&r2);
F(i,16){scanf("%d ",&c2[i]);}
busca(c1, c2, r1, r2, ++a);
}

}