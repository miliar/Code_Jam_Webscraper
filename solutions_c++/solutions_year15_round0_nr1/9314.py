#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		cout<<"Case #"<<i<<": ";
		int n;
		cin>>n;
		string s;
		cin>>s;
		int sum=0,ans=0;
		for(int j=1;j<=s.length();j++)
		{
			sum+=s[j-1]-'0';
			if(sum<j){sum++;ans++;}		
		}		
		cout<<ans<<endl; 	
	}
return 0;
}
