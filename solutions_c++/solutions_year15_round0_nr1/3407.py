/*************************************************************************
    > File Name: a.cpp
    > Author: 
    > Created Time: 一  3/23 12:59:53 2015
 ************************************************************************/

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 1200;

int T, n;
char a[maxn];

int main(){
	scanf("%d", &T);
	for (int cT=0; cT<T; ){
		scanf("%d%s", &n, a);
		int ans = 0;
		for (int i=1, acc=a[0]-'0'; i<=n; i++){
			if (acc < i){
				ans += i-acc;
				acc = i;
			}
			acc += a[i]-'0';
		}
		printf("Case #%d: %d\n", ++cT, ans);
	}
	return 0;
}

