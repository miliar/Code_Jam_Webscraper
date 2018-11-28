#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
using namespace std;
string s;
int n;
int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int t;
	cin>>t;
	for(int i = 1; i<=t;i++){
		cin>>n>>s;
		long ans = 0,sum = 0;
		for(int j = 0; j<= n;j++){
			if(sum >= j){
				sum += s[j] - 48;
			}else{
				ans += j - sum;
				sum = j +s[j] - 48;
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
		
	return 0;
}

