#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <cstring>

using namespace std;
#define clr(A) memset(A,0,sizeof(A))


typedef long long LL;
typedef unsigned long long ULL;

typedef pair<int,int> P;
const int INF = 1000000009;
const int mm = 10005;
priority_queue<int> que;
int a[mm];
int D;
int cal(int mid){
	int res = mid;
	for(int i = 0; i < D; i++)
		res += (a[i] - 1) / mid;
	return res;
}

int main(){
//    freopen("wcbao.in","r",stdin);
//    freopen("ans.out","w",stdout);
    int T, c = 0;
    cin >> T;
    while(T--){
    	int l = 1, r = 0,ans = 1;
    	scanf("%d", &D);
    	for(int i = 0; i < D; i++){
    		scanf("%d",a+i);
    		r = max(r,a[i]);
    	}
    	ans = INF;
    	for(int i = 1;i<=r;i++){
            int t = i;
            for(int j = 0; j < D; j++)
            t += (a[j]-1)/i;
            ans = min(ans,t);
    	}
//    	while(l<=r){
//    		int mid1 = (l+l+r)/3, mid2 = (l+r+r)/3;
//    		int sum1 = cal(mid1), sum2 = cal(mid2);
//    		ans = min(sum1,sum2);
//    		if(sum1 < sum2) r = mid2 - 1;
//    		else l = mid1 + 1;
//    	}
    	printf("Case #%d: %d\n",++c,ans);
    }
    return 0;
}
