#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int main(){
	int t; scanf("%d", &t);
	for(int cas=1;cas<=t;cas++){
		int a, b, k; scanf("%d %d %d", &a, &b, &k);

		int ans = 0;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				//cout << (i&j) << " " << k << " \n";
				if((i&j) < k){
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n", cas, ans);
	}
}
