#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		int temp=0,ans=0,x;
		scanf("%d",&x);
		string s;
		cin>>s;
		for(int j=0;j<=x;j++){
			if(temp<j){
				ans+=(j-temp);
				temp=j;
			}
			temp+=(s[j]-'0');
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
