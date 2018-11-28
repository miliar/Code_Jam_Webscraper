#include<limits>
#include<queue>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<ctime>

#define LL long long
#define eps 1e-8
#define pi acos(-1)
#define INF 0x7fffffff
#define delta 0.98 //模拟退火递增变量
using namespace std;
int d[10];
void go(LL n){
	while(n){
		d[n%10]=1;
		n/=10;
	}
}
int ha(){
	int k=0;
	for (int i=0;i<10;i++)
		k+=d[i];
	if (k==10) return 1;
	return 0;
}
int main(){
	int T;
	LL n;
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for (int t=1;t<=T;t++){
		scanf("%lld",&n);
		printf("Case #%d: ",t);
		memset(d,0,sizeof(d));
		go(n);
		int flag=1;
		for (int i=2;i<=1000;i++){
			go(i*n);
			if (ha()){
				flag=0;
				printf("%lld\n",i*n);
				break;
			}
		}
		if (flag) printf("INSOMNIA\n");
	}
	return 0;
}

