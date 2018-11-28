#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#define inf (1<<30)
using namespace std;

int a[1111];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;
	cin>>T;
	for (int _=1;_<=T;_++){
		int n;
		cin>>n;
		for (int i=0;i<n;i++) scanf("%d",&a[i]);
		int ans=inf;
		for (int k=1;k<=1000;k++){
			int sum=k;
			for (int i=0;i<n;i++) sum+=(a[i]+k-1)/k-1;
			ans=min(ans,sum);
		}
		printf("Case #%d: %d\n",_,ans);
	}
}
