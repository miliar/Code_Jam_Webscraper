#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;

int chk;
int n, m;

long long find(int n){
	m = 100;
	chk = (1<<10) - 1;
	for(int i=1; i<m; i++){
		long long temp = n * i;
		while(temp){
			if(chk & 1<<(temp%10)) chk -= 1<<(temp%10);
			temp/=10;
			if(chk==0){
				return i*n;
			}
		}
	}
	return -1;
}
int main(){
	//freopen("input.txt", "r", stdin);
	int T;
	scanf("%d", &T);
	for(int i=1; i<=T; i++){
		scanf("%d", &n);
		printf("Case #%d: ", i);
		long long ans = find(n);
		if(ans==-1) printf("INSOMNIA\n");
		else printf("%lld\n", ans);
	}
    return 0;
}
