#include<bits/stdc++.h>

using namespace std;

int n,i,j,k,ans,top;
string str;

int main(){
	cin >> n;

	for(i=1 ; i<=n ; i++){
		cin >> k;

		cin >> str;

		ans = 0;
		top = 0;

		for(j=0 ; j<str.size() ; j++)
			if(j>top){
				ans += j-top;
				top = j+str[j]-'0';
			}
			else 
				top += str[j]-'0';
		printf("Case #%d: %d\n",i,ans);
	}
}
