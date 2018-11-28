#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<queue>
#include<cmath>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
using namespace std;

int TEST,NNN,number,num1,num2,num3,now[10005],ans[10005];

void digui(int l,int r,int llll){
	if (l==r) {
		now[l]=llll;
		return;
	}
	int mid=(l+r) >> 1;
	digui(l,mid,llll);
	digui(mid+1,r,(llll-1+3) % 3);
	bool bz=0;
	int l1=l,l2=mid+1;
	while (l1<=mid) {
		if (now[l1]<now[l2]) {bz=0;break;
		}
		if (now[l1]>now[l2]) {bz=1;break;
		}
		++l1;
		++l2;
	}
	if (bz) {l1=l,l2=mid+1;
		while (l1<=mid) {
			swap(now[l1],now[l2]);++l1;++l2;
		}
	}
}

int main(){
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	cin>>TEST;
	fo(tpq,1,TEST) {
		printf("Case #%d: ",tpq);
		scanf("%d%d%d%d",&NNN,&num1,&num2,&num3);
		number=1 << NNN;
		ans[1]=100000;
		fo(llll,0,2){
			memset(now,0,sizeof(now));
			digui(1,number,llll);
			int pqsum[3];
			pqsum[0]=pqsum[1]=pqsum[2]=0;
			fo(i,1,number) pqsum[now[i]]++;
			if (pqsum[0]!=num2 || pqsum[1]!=num1 || pqsum[2]!=num3) continue;
			bool bz=0;
			fo(i,1,number) {
				if (now[i]<ans[i]) {bz=1;break;
				}
				if (now[i]>ans[i]) {bz=0;break;
				}
			}
			if (bz) {
				memcpy(ans,now,sizeof(ans));
			}
		}
		if (ans[1]==100000) {
			puts("IMPOSSIBLE");
		}
		else {
			for(int i=1;i<=number;i++) {
				if (ans[i]==0) printf("P");
				if (ans[i]==1) printf("R");
				if (ans[i]==2) printf("S");
			}
			printf("\n");
		}
	}
	return 0;
}
