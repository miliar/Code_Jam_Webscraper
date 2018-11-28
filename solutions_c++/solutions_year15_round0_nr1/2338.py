#include<stdio.h>
#include<string>
#include<iostream>
using namespace std;
int c = 0;
int n;
main(){
	int T;
	freopen("test.inp","r",stdin);
	freopen("test.out","w",stdout);
	cin>>T;
	while(T > 0){
		c++;
		string s;
		cin>>n;
		cin>>s;
		int curr = 0;
		int ans = 0;
		for(int i = 0 ; i <= n ; i++)
			if(curr >= i) curr+=s[i] - 48;
			else{
				ans+=(i - curr);
				curr = i + s[i] - 48;
			}
		cout<<"Case #"<<c<<": "<<ans<<'\n';
		T--;
	}
}
