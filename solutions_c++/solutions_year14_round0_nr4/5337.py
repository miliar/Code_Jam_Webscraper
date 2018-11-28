#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
#define rep(i,n) for(int i=0;i<(n);++i)
#define rep1(i,n) for(int i=1;i<=(n);++i)
#define ALL(c) (c).begin(),(c).end()
double naomi[1000],ken[1000];
bool used[1000]={};
int main(){
	int times;
	cin >> times;
	rep(t,times){
		int n,ans=0,ans2=0;
		cin >> n;
		rep(i,n) cin >> naomi[i];
		rep(i,n) cin >> ken[i];
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		rep(i,n){
			bool renew=false;
			int l=lower_bound(ken,ken+n,naomi[i])-ken;
			for(int j=l;j<n;j++){
				if(!used[j]){
					renew=true;
					used[j]=true;
					break;
				}
			}
			if(!renew){
				rep(j,n){
					if(!used[j]){
						used[j]=true;
						break;
					}
				}
				ans2++;
			}
		}
		rep(i,n) swap(ken[i],naomi[i]);
		rep(i,n) used[i]=false;
		rep(i,n){
			bool renew=false;
			int l=lower_bound(ken,ken+n,naomi[i])-ken;
			for(int j=l;j<n;j++){
				if(!used[j]){
					renew=true;
					used[j]=true;
					break;
				}
			}
			if(!renew){
				rep(j,n){
					if(!used[j]){
						used[j]=true;
						break;
					}
				}
				ans++;
			}
		}
		printf("Case #%d: %d %d\n",t+1,n-ans,ans2);
	}
	return 0;
}