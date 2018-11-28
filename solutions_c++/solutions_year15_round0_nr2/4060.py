#include <bits/stdc++.h>
using namespace std;
int cnt[1001];
int f(int x){
	if(x==0) return 0;
	for (int i = x; i >= 0; i--) {
		if(cnt[i]==0) continue;
		int tmp=0;
		for (int j = i-1; j >= 0; j--){
			if(cnt[j]>0){
				tmp=j;
				break;
			}
		}  
		int mini=1e9;
		int newcnt=cnt[i],xtmp=1e9;
		for (int k = 1; k < i; k++) {
			cnt[k]+=newcnt,cnt[i-k]+=newcnt;
			int newans=f(max(tmp,max(k,i-k)));
			// if(i==9 && k==1) {
			// 	cout<<newans<<" ** "<<k<<endl;
			// 	for (int j = 1; j <= 9; j++) {
			// 		if(cnt[j]>0) cout<<j<<" ";
			// 	}
			// 	cout<<endl;
			// }
			cnt[k]-=newcnt,cnt[i-k]-=newcnt;
			if(newans+newcnt<i){
				if(newcnt+newans<mini){
					mini=newcnt+newans;
					xtmp=k;
				}
			}
			else mini=min(mini,i);
		}
		if(mini>=i) return i;
		else{
			//cnt[xtmp]+=newcnt,cnt[i-xtmp]+=newcnt;
			return mini;
		}
	}
}
int main(){
	int test;
	scanf("%d",&test);
	for (int k = 1; k <= test; k++) {
		int d;
		cin>>d;
		int a[d];
		for (int i = 0; i < d; i++) cin>>a[i];
		int ans=0;
		for (int i = 0; i <= 1000; i++) cnt[i]=0;
		for (int i = 0; i < d; i++) cnt[a[i]]++;
		//for (int i = 0; i <= 9; i++) if(cnt[i]>0) cout<<i<<" ";
		//cout<<"^^^^"<<endl; 
		cout<<"Case #"<<k<<": "<<f(1000)<<endl;      
	}
}