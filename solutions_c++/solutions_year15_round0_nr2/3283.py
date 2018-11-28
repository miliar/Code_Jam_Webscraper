/*************************************************************************
    > File Name: b.cpp
    > Author: 
    > Created Time: 六  4/11 16:37:47 2015
 ************************************************************************/

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 1200;

int T, n, a[maxn];

int calc(int cur){
	int ans = 0;
	for (int i=0; i<n; i++)
		if (a[i]>cur){
			int t = (a[i]+cur-1)/cur;
			ans += t-1;
		}
	return ans + cur;
}

int main(){
	scanf("%d", &T);
	for (int cT=0; cT<T; ){
		int L=1, R=0;
		scanf("%d", &n);
		for (int i=0; i<n; i++){
			scanf("%d", a+i);
			if (a[i] >= R)
				R = a[i];
		}
		int ans = R;
		for (int i=1; i<R; i++){
			int tmp = calc(i);
			if (ans > tmp)
				ans = tmp;
		}
		printf("Case #%d: %d\n", ++cT, ans);
	}
	return 0;
}

