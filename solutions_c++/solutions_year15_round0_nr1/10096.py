#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	cin>>T;
	int no=1;
	while(T--){
		int n,cnt=0,ans=0;
		cin>>n;
		char x;
		for(int i=0;i<=n;i++){
			cin>>x;
			if(x!='0'){
				if(cnt<i){
					ans+=(i-cnt);
					cnt+=(i-cnt);
				}
				cnt+=(x-48);
			}
		}
		cout<<"Case #"<<no<<": "<<ans<<endl;
		no++;
	}
	return 0;
}
