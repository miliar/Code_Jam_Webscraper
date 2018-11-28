#include<cstdio>
#include<cstring>
#include<climits>
#include<cfloat>
#include<cmath>
#include<algorithm>
#include<vector>
#include<stack>
#include<set>
#include<queue>
#include<string>
#include<map>
#ifdef _WIN32
	#include <Windows.h>
#endif

using namespace std;

typedef pair<int,int> pr;
typedef long long ll;

int main()
{
#ifdef _WIN32
	int timer_start = GetTickCount();
	freopen("in.put", "r", stdin);
#endif
	// code here

	int T;
	scanf("%d",&T);
	for(int i=1; i<=T; i++){
		ll r,t,sum=0,temp,nn;
		scanf("%lld%lld",&r,&t);
		for(ll j=0LL; ; j++){
			temp = 2*r+1+4*j;
			if (sum+temp <= t) {
				sum+=temp;
			}
			else{
				nn=j;
				break;
			}
		}
		printf("Case #%d: %lld\n", i, nn);
	}

	// end of code

#ifdef _WIN32
	printf("\nElapsed time : %.3lf\n", (GetTickCount()-timer_start)/1000.0);
#endif
	return 0;
}
