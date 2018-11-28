#include<bits/stdc++.h>

using namespace std;

string str;

int main(){
	int t;
	cin>>t;
	for(int kk=1;kk<=t;kk++){
	int n;
	cin>>n;
	cin>>str;
	int i;
	int ans=0;
	long long cnt=str[0]-'0';
	for(i=1;str[i];i++){
		if(cnt<i){
			ans+=(i-cnt);
			cnt+=(i-cnt);
		}
		cnt+=(str[i]-'0');
	}
		cout<<"Case #"<<kk<<": "<<ans<<endl;
	}
	
	return 0;
}