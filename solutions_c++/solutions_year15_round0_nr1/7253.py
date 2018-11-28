#include<bits/stdc++.h>
using namespace std;
int solve(char c[],int t){
	int count=0,no=0;
	for(int i=0;i<=t;i++){
		if(count>=i){
			count+=c[i]-'0';
		}else{
			no+=i-count;
			count=i;
			count+=c[i]-'0';
		}
	}
	return no;
}
int main(){
	int t,n,i=0;
	char a[2000];
	cin>>t;
	while(i++<t){
		cin>>n>>a;
		cout<<"Case #"<<i<<": "<<solve(a,n)<<endl;
	}
	return 0;
}
