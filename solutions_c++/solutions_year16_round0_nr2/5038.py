#include<bits/stdc++.h>
using namespace std;
int ans,ind;

int main(){
	int i,t,j;
	cin>>t;
	for(j=1;j<=t;j++){
		cout<<"Case #"<<j<<": ";
		string s;
		cin>>s;
		ind = s.length();
		int cnt = 0,c=0;
		char start = s[0];
		if(start=='-'){
				cnt++;
				c = 1;
			}
		for(i=1;i<ind;i++){
			if(start==s[i]) {
			
			continue;
		}
		else{
			start = s[i];
			if(start=='-') cnt++;
		}
			
	}
	cout<<2*(cnt-c)+c<<endl;
}


}
