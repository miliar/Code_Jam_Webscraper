#include <bits/stdc++.h>
using namespace std;
int main(){
	int t;
	scanf("%d",&t);
	int ii=1;
	while(t--){
		int a;
		string b;
		cin>>a>>b;
		int num=0;
		int i;
		int sum=0;
		for(i=0;i<a+1;i++){
			if(sum>=i){
				sum+=b[i]-'0';
			}
			else{
				num+=i-sum;
				sum=i+(b[i]-'0');
			}
		}
		printf("Case #%d: %d\n",ii++,num);
	}
}