#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int t;
int n;
double a[1010];
double b[1010];
int fl[1010];

int main(){
	scanf("%d",&t);
	for(int tt=1; tt<=t; tt++){
		printf("Case #%d: ",tt);
		scanf("%d",&n);
		memset(fl,0,sizeof(fl));
		for(int i=0; i<n; i++) scanf("%lf",&a[i]);
		for(int i=0; i<n; i++) scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		int ca=0;
		for(int i=0; i<n; i++){
			int f=0;
			for(int j=0; j<n; j++){
				if(b[j] > a[i] && !fl[j]){
					fl[j]=1;
					f=1;
					break;
				}
			}
			if(!f) break;
		}
		int cnt=0;
		for(int i=0; i<n; i++){
			if(!fl[i]) cnt++;
		}
		memset(fl,0,sizeof(fl));
		int ans=0;
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				if(a[j] > b[i] && !fl[j]){
					fl[j]=1;
					ans++;
					break;
				}
			}
		}
		printf("%d %d\n",ans,cnt);
	}
	return 0;
}
