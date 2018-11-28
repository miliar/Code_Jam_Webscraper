#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int casenum = 0;casenum<t;casenum++){
		int smax;
		scanf("%d", &smax);
		char str[1100];
		scanf("%s", str);
		int ans = 0;
		int sum = 0;
		sum+=str[0]-'0';
		for(int i = 1;i<=smax;i++){
			if(sum<i){
				ans+=i-sum;
				sum = i;
			}
			sum+=str[i]-'0';
		}
		printf("Case #%d: %d\n",casenum+1, ans);
	}
	return 0;
}