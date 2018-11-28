#include <bits/stdc++.h>

using namespace std;


int main(){

	int t,ca = 1;
	scanf("%d",&t);
	while(t--){
		printf("Case #%d: ",ca++);
		int n;
		scanf("%d",&n);
		string s;
		cin>>s;
		int resp = 0;
		int qtd = (s[0]-'0');
		for(int i  = 1;i<=n;i++){
			if(qtd<i){
				resp+=(i-qtd);
				qtd+=(i-qtd);
			}
			qtd+=(s[i]-'0');
		}
		printf("%d\n",resp);
	}


	return 0;
}