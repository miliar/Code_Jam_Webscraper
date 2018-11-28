#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define maxn 10100
int N,val[maxn],ans;
void cal()
{
	int L = 0, R = N;
	ans = 0;
	while(L<R){
		int L_v = val[L], L_i = L;
		for (int i = L; i<R; i++){
			if (val[i]<L_v){
				L_v = val[i];
				L_i = i;
			}
		}
		if (L_i-L < R-L_i-1){
			for (int i = L_i; i>L; i--){
				ans++;
				swap(val[i], val[i-1]);
			}
			L++;
		}else {
			for (int i = L_i; i+1<R; i++){
				ans++;
				swap(val[i],val[i+1]);
			}
			R--;
		}
	}
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    int t,cas;
    scanf("%d",&t);
    for (cas = 1; cas <= t; cas++){
        scanf("%d",&N);
        for (int i = 0;i<N;i++)
            scanf("%d",&val[i]);
        cal();
        printf("Case #%d: %d\n",cas, ans);
    }
	return 0;
}
