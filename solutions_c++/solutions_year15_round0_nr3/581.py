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

#define N 10000

using namespace std;

const int op[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
char a[N+10];

int f(char x)
{
	switch(x){
		case '1': return 1;
		case 'i': return 2;
		case 'j': return 3;
		case 'k': return 4;
	}
}

int g(int x,int y)
{
	if(x*y>0) return op[abs(x)][abs(y)];
	return -op[abs(x)][abs(y)];
}

int divide(int x,long long n)
{
	if(n==1LL) return x;
	int t;
	t=divide(x,n/2LL);
	if(n%2LL) return g(x,g(t,t));
	return g(t,t);
}

int main()
{
	freopen("C-large.in","r",stdin); freopen("1.out","w",stdout);
	int T,n,i,j,r,t,k;
	int idx,id;
	long long x;
	scanf("%d",&T);
	FOR(r,1,T){
		scanf("%d %lld",&n,&x);
		scanf("%s",a);
		t=f(a[0]);
		FOR(i,1,n-1) t=g(t,f(a[i]));
		//k=divide(t,x);
		k=1;
		FOR(i,1,x%4) k=g(k,t);
		printf("Case #%d: ",r);
		if(k!=-1) printf("NO\n");
		else{
			t=1;
			if(x>=8){
				id=0; idx=0;
				FOR(i,1,4){
					FOR(j,0,n-1){
						t=g(t,f(a[j]));
						if(t==2) idx=1;
						if(g(t,4)==1) id=1;
					}
				}
				if(idx&&id) printf("YES\n");
				else printf("NO\n");
			}
			else{
				id=0; idx=0;
				FOR(i,1,x){
					FOR(j,0,n-1){
						t=g(t,f(a[j]));
						if(t==2){
							idx=x*n-1; break;
						}id++;
					}
					if(idx) break;
				}
				t=1;
				FOR(i,1,x){
					DEC(j,n-1,0){
						t=g(t,f(a[j]));
						if(g(t,4)==-1){
							if(idx-id>1) printf("YES\n");
							else printf("NO\n"); 
							id=-1; break;
						}idx--;
					}
					if(id==-1) break;
				}
				if(id!=-1) printf("NO\n");
			}
		}
	}
	return 0;
}