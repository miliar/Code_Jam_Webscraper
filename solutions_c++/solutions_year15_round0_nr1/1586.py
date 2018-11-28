#include<bits/stdc++.h>
using namespace std;

int t;

int main(){
	ios::sync_with_stdio(0);
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);	
	cin>>t;
	for(int i=1;i<=t;i++) {
		string str;
		int smax,ans=0,sum=0;
		cin>>smax>>str;
		int j=0;
		while(str[j]) {
			if(sum>=j) {
				sum += (str[j] - '0');
			}else{
				sum = j+(str[j] - '0');
				ans++;
			}
			j++;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}	
