#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <cstdlib>
using namespace std;
#define ll long long int

ll t,len,i,j,ans,m;
string S;

void swap(ll k){
	char use;
	if(k==0){
		if(S[k]=='-') S[k]='+';
		else S[k]='-';
		return;		
	}
	for(m=0; m<k ;k--,m++){
		use = S[m];
		S[m]=S[k];
		S[k]=use;
		if(S[m]=='-') S[m]='+';
		else S[m]='-';
		if(S[k]=='-') S[k]='+';
		else S[k]='-';
	}
	if(m==k){
		if(S[m]=='-') S[m]='+';
		else S[m]='-';
	}
	return;
}

int main(){
	scanf("%lld",&t);
	for(j=1;j<=t;j++){
		cin>>S;
		len = S.length();
		ans=0;
		for(i=len-1;i>=0;i--){
			if(S[i]=='-'){
				if(S[0]=='-'){
					swap(i);
					ans++;
					continue;
				}
				else{
					for(m=1; m<i; m++){
						if(S[m]=='-') break;
					}
					swap(m-1);
					swap(i);
					ans+=2;
					continue;
				}
			}
		}
		printf("Case #%lld: %lld\n",j,ans);
	}
}

