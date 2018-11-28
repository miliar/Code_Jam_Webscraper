#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <queue>
#include <memory.h>

using namespace::std;

long long N,p,q,r,s;
long long a[1000005];
long long sum[1000005];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ca=1;ca<=t;ca++){
		scanf("%lld %lld %lld %lld %lld",&N,&p,&q,&r,&s);
		for(int i=1;i<=N;i++){
			a[i]=((i-1)*p+q)%r+s;
			sum[i]=sum[i-1]+a[i];
		}
		sum[N+1]=sum[N]*3;
		int a=1,b=1;
		long long ans=0;
		for(int b=1;b<=N;b++){
			while(sum[b]-sum[a+1]>=sum[a+1])
				a++;
			long long op=max(sum[a],sum[b]-sum[a]);
			op=max(op,sum[N]-sum[b]);
			ans=max(ans,sum[N]-op);
			if(a!=1){
			a--;
			op=max(sum[a],sum[b]-sum[a]);
			op=max(op,sum[N]-sum[b]);
			ans=max(ans,sum[N]-op);
			a++;
			}
			if(a!=b){
			a++;
			op=max(sum[a],sum[b]-sum[a]);
			op=max(op,sum[N]-sum[b]);
			ans=max(ans,sum[N]-op);
			a--;
			}
		}
		printf("Case #%d: %.10lf\n",ca,(double)ans/sum[N]);
	}
	return 0;
}