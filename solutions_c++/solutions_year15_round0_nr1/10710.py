#include<iostream>
using namespace std;
int main(){
	int t,S,i;
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>S;
		char str[S+2];
		cin>>str;
		int count=str[0]-48,ans=0;
		
		for(int j=1;j<=S;j++){
			int n=(int)str[j]-48;
			if(count<j&&n!=0){
				ans+=j-count;
				count=j;
			}
		
			count+=n;


		}
		cout<<ans<<endl;
	}
	return 0;
}
