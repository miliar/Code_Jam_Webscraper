#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>
using namespace std;
int main(){
	int t;
	int cases=1;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		int ans=0;
		int sum=0;
		for(int i=0;i<=n;i++){
			char ins;
			cin>>ins;
			if(ins!='0'){
				int in=ins-'0';
				int Toadd=max(i-sum,0);
				ans+=Toadd;
				sum+=in+Toadd;
			}
		}
		printf("Case #%d: %d\n",cases++,ans);
	}
	return 0;
}