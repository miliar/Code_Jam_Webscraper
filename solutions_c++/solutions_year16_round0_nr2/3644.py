//Naman Agarwal
//IIT Mandi
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
#include <string>

using namespace std;

#define lli long long int

int main() {
	ios::sync_with_stdio(false);
	lli t,tc=1;
	cin>>t;
	while(t--){
		string s;
		cin>>s;
		lli n=s.length();
		lli ans[s.length()];
		lli allp,alln;
		if(s[0]=='+'){
			allp=1;
			alln=0;
			ans[0]=0;
		}else{
			allp=0;
			alln=1;
			ans[0]=1;
		}
		for(lli i=1;i<n;i++){
			if(s[i]=='+'){
				ans[i]=ans[i-1];
			}else{
				if(s[i-1]=='-'){
					ans[i]=ans[i-1];
				}else{
					ans[i]=ans[i-1]+2;
				}
			}	
		}
		cout<<"Case #"<<tc<<": "<<ans[n-1]<<"\n";
		tc++;
	}
	return 0;
}