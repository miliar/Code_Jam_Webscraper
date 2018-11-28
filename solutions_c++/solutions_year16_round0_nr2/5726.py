#include<bits/stdc++.h>
using namespace std;
#define Int long long
int main(){
	Int t,i,j,ans,n;char str[200];
	scanf("%lld",&t);
	for(i=1;i<=t;i++){
		cin>>str;
		n=0;
		for(j=0;str[j]!='\0';j++){
			if(str[j]=='-'){
				if(	(j==0) || (str[j-1]=='+') )
					n++;
			}
		}
		if(str[0]=='-'){
			ans = 2*n -1;
		}else{
			ans = 2*n;
		}
		printf("Case #%lld: %lld\n",i,ans);
	}
	return 0;
}