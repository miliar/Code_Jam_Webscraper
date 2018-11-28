#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define MAXN 105

int mote[MAXN];
int n,a;

int main(){
	freopen("A-small-attempt3.in","r",stdin);
	freopen("A-small-attempt3.out","w",stdout);
	int t,ti=1;
	scanf("%d",&t);
	while(t--){
		printf("Case #%d: ",ti++);
		scanf("%d %d",&a,&n);
		int i;
		for(i=0;i<n;i++)scanf("%d",&mote[i]);
		if(a==1){
			printf("%d\n",n);
			continue;
		}
		sort(mote,mote+n);
		int ans=0;
		for(i=0;i<n;i++){
			if(mote[i]<a)
				a+=mote[i];
			else{
				int tmp=a,tmps=0;
				while(tmp<=mote[i]){
					tmp=(tmp<<1)-1;
					tmps++;
				}
				if(tmps<(n-i)){
					ans+=tmps;
					a=tmp+mote[i];
				}
				else{
					ans+=n-i;
					break;
				}
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}