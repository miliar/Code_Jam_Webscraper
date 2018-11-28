#include<iostream>
#include<string.h>
using namespace std;



int main(){

	int t,i=0,ans;
	cin>>t;
	string s;
	while(i<t){
	ans=0;
		i++;
		cin>>s;
		int l=s.length();
		char st[101];
		int j=0;
		
		while(j<l){
		char c=s[0];
			if(s[j]==c)
				st[j]=c;
			else{
			ans++;
				char rev;
				if(c=='-')
					rev='+';
				else rev='-';
				
				for(int k=0;k<j;k++){
					s[k]=rev;
				}	
			}
			j++;
		}
		if(s[0]=='-')
			ans++;
		cout<<"Case #"<<i<<": "<<ans<<endl;
	
	}

return 0;
}
