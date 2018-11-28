#include<iostream>
#include<string.h>
using namespace std;

int returnMinFlips(string s){
int ans=0;
for(int i=s.length()-1;i>=0;i--){
	if(s[i]=='-'){
		ans++;
		for(int j=0;j<=i;j++){
			if(s[j]=='+')s[j]='-';
			else if(s[j]=='-')s[j]='+';
		}
	}	
}
	
return ans;
}

int main(){
int t,k=1;
cin>>t;
while(t--){
string s;
cin>>s;
cout<<"Case #"<<k++<<": "<<returnMinFlips(s)<<endl;
}
return 0;
}

