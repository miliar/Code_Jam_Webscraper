#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int T;
long long e,r;
int n;
int le[11000];
long long v[11000];
int st[11000],sn;

int main(){
	scanf("%d",&T);
	int h,i,j,k;
	for(h=1;h<=T;h++){
		scanf("%lld%lld%d",&e,&r,&n);
		if(r>e)r=e;
		sn=0;
		memset(le,-1,sizeof(le));
		for(i=0;i<n;i++){
			scanf("%d",&v[i]);
			while(sn>0){
				if(v[st[sn-1]]<=v[i]){
					le[st[sn-1]]=i-st[sn-1];
					sn--;
				}else break;
			}
			st[sn++]=i;
		}
		long long ne=e,ans=0;
		for(i=0;i<n;i++){
			if(le[i]==-1 || le[i]*r>=e){
				ans+=ne*v[i];
				ne=0;
			}else if(ne+r*le[i]>=e){
				ans+=(ne+r*le[i]-e)*v[i];
				ne=e-r*le[i];
			}
			ne+=r;
		}
		printf("Case #%d: %lld\n",h,ans);
	}
}
