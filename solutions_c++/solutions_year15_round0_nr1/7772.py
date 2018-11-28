#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <time.h>
using namespace std;
#define Max(x,y)  ((x)>(y)?(x):(y))
#define Min(x,y)  ((x)<(y)?(x):(y))
#define Abs(x) 	  ((x)>0?(x):(-(x)))
#define Swap(x,y) (x+=y,y=x-y,x-=y)
#define sqr(x)	  ((x)*(x))
typedef long long LL;

const double Pi = acos(-1.0);
const double Eqs = 0.00000001;
const int Inf = 123456789;
const int maxn =  1000 + 10;
int a[maxn];
int g[maxn];

int solve(int n){
	int res = 0;
	for(int i=0;i<=n;i++){
		g[i] = 0;
	}
	for(int i=1;i<=n;i++){
		g[i] = g[i-1] + a[i-1];
		if(g[i] < i){
			res += i - g[i];
			g[i] = i;
		}
	}
	return res;
}

int main(){
    //freopen("alin.txt","r",stdin);
    //freopen("alout.txt","w",stdout);
    int T;
	cin>>T;
	for(int _t=1;_t<=T;_t++){
		int n;
		scanf("%d",&n);
		char ch[maxn + 10];
		scanf("%s",ch);
		for(int i=0;i<=n;i++){
			a[i] = ch[i] - '0';
		}
		printf("Case #%d: %d\n",_t,solve(n));
	}
    return 0;
}
