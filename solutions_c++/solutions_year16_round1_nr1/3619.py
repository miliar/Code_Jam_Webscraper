#include<iostream>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

int main(){

		int t,i=1;
		cin>>t;
		while(i<=t){
			
			string s,ans;
			cin>>s;
			int len=s.length();
			int j=1;
			string c;
			c=s[0];
			ans=c+ans;
			while(j<len){
				c=s[j];
				char ch=c[0];
				if(ch>=ans[0]){
					ans=c+ans;
				}
				else{
					ans=ans+c;
				}
				j++; 
			}
		cout<<"Case #"<<i<<": "<<ans<<endl;
		i++;
		}
	


return 0;
}
