#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>
#define ll long long
using namespace std;
int main(){
	ll t,n,count;
	string s;
	scanf("%lld",&t);
	for(int tt=1;tt<=t;tt++){
		count=0;
		cin>>s;
		n=s.length();
		for(int i=n-1;i>=0;i--){
			
			if(s[i]==43) continue;
			else{
				 count++;
				 reverse(s.end()-i,s.begin());
				 for(;s[i]!=45 && i>=0;i--);
				 for(int j=i;j>=0;j--) if(s[j]==45) s[j]=43; else s[j]=45;
			}
	    }
	    printf("Case #%d: %lld\n",tt,count);
	}
	return 0;
}
