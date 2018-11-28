#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>

#include <algorithm>
#include <iostream>
#include <string>
#include <utility>

#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>


#define FOR(i,a,b) for(i=a;i<=b;i++)
#define DEC(i,a,b) for(i=a;i>=b;i--)
#define NL printf("\n")
#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define QUAD(x) (x)*(x)
#define MOD(a,b) ((a)%(b)+b)%(b)

#define VI vector<int>
#define ST stack<int>
#define QI queue<int>
#define PQ priority_queue<int>
#define DQ deque<int>
#define SI set<int>
#define PII pair<int,int>
#define LL long long
#define DB double

#define RICHARD  printf("RICHARD\n")
#define GABRIEL printf("GABRIEL\n")

using namespace std;

int main()
{
	freopen("D-small-attempt1.in","r",stdin); freopen("1.out","w",stdout);
	int T,x,r,m,n,i;
	scanf("%d",&T);
	FOR(r,1,T){
		scanf("%d %d %d",&x,&m,&n);
		printf("Case #%d: ",r);
		if(m*n%x==0){
			if(x>6) RICHARD;
			else if(x<3) GABRIEL;
			else if(x==3){
				if(MIN(m,n)<2) RICHARD;
				else GABRIEL;
			}
			else if(x==4){
				if(MIN(m,n)<3) RICHARD;
				else GABRIEL;
			}
			else if(x==5){
				if(MIN(m,n)<3) RICHARD;
				else GABRIEL;
			}
			else if(x==6){
				if(MIN(m,n)<5) RICHARD;
				else GABRIEL;
			}
		}
		else RICHARD;
	}
	return 0;
}