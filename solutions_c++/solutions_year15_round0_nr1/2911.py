#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
using namespace std;
int t,ans,sum,n;
char s[1005];

int main(){
	scanf("%d",&t);
	for (int tc = 1; tc <= t; ++tc){
		scanf("%d",&n);
		scanf("%s",s);
		ans = 0;
		sum = 0;
		for (int i = 0; i <= n; ++i){
			int x = s[i] - '0';
			if (sum < i && x  > 0){
				ans += i-sum;
				sum = i;
			}
			sum += x;
		}
		printf("Case #%d: %d\n",tc,ans);
	}
}