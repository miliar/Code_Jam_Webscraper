#include <cstdio>
#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
#define maxn 1000009
int a[maxn];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("t.out","w",stdout);
	int T;
	int cs=1;
	cin>>T;
	while(T--){
		int n;cin>>n;
		for(int i=0;i<n;i++)scanf("%d",&a[i]);
		int ans1=0,ans2=0;
		int mx=0;
		for(int i=1;i<n;i++){
			if(a[i]<a[i-1]){
				ans1+=a[i-1]-a[i];
				mx=max(a[i-1]-a[i],mx);
			}
		}
		if(mx==0){
			ans2=0;
		}else{
			for(int i=0;i<n-1;i++){
				if(a[i]<mx){
					ans2+=a[i];
				}else{
					ans2+=mx;
				}
			}
		}
		printf("Case #%d: %d %d\n",cs++,ans1,ans2);
	}
}