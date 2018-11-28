#define _USE_MATH_DEFINES
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<climits>
#include<string>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<cmath>
#include<queue>
#include<cstring>
#include<stack>
#include<functional>
#include<deque>
#include<cstdlib>
#include<ctime>
using namespace std;
typedef long long ll;

int main(){
	int T;
	cin>>T;
	for(int tc=1;tc<=T;tc++){
		int D,P[1000], ma = 0;
		cin>>D;
		for(int i=0;i<D;i++){
			cin>>P[i]; ma = max(ma,P[i]);
		}
		int ans = ma;
		for(int i=2;i<ma;i++){
			int sum = 0;
			for(int j=0;j<D;j++){
				sum += P[j]/i-1;
				if(P[j]%i>0) sum++;
			}
			ans = min(ans,sum+i);
		}
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}
