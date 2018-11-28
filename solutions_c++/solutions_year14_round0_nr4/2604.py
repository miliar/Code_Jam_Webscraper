#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<string>
#include<algorithm>
#include<unordered_map>
#include<vector>
using namespace std;
int main(){
	freopen("D-large.in","r",stdin);
	freopen("D-large.out", "w",stdout);
	int t;
	scanf("%d",&t);
	for(int casenum = 0;casenum <t;++casenum){
		int n;
		double a[1010];
		double b[1010];
		scanf("%d",&n);
		for(int i = 0;i<n;i++){
			scanf("%lf",&a[i]);
		}
		for(int i = 0;i<n;i++){
			scanf("%lf",&b[i]);
		}
		sort(a,a+n);
		sort(b,b+n);
		int ans = 0;
		int st_a = 0,st_b = 0;
		int ed_a = n-1,ed_b = n-1;
		while(st_a <=  ed_a){
			if(a[ed_a]>b[ed_b]){
				ans++;
				st_b++;
			}else{
				ed_b--;
			}
			ed_a--;
		}
		int ans2 = 0;
		st_a = st_b = 0;
		ed_a = ed_b = n-1;
		while(st_a<=ed_a){
			if(a[st_a]<b[st_b]){
				ed_b--;
			}
			else{
				ans2++;
				st_b++;
			}
			st_a++;
		}
		printf("Case #%d: %d %d\n",casenum+1, ans2, ans);
	}
	return 0;
}