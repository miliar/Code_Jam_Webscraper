#include <bits/stdc++.h>

using namespace std;
#define int long long
int power(int a,int b){
	int ans=1;
	for(int i=0;i<b;i++){
		ans*=a;
	}
	return ans;
}
signed main(){
	int tc,i=0;
	cin>>tc;
	while(tc-->0){
		i++;
		int k,c,s;
		cin>>k>>c>>s;
		int len=power(k,c);
		cout<<"Case #"<<i<<": ";
		if(k==1){
			cout<<1<<endl;
			continue;
		}
		int dif=(len-s)/(s-1);
		int now=1;
		while(now<=len){
			cout<<now<<" \n"[now==len];
			now+=dif+1;
		}
	}
	return 0;
}
