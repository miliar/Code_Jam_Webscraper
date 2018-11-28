#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

bool che(string s){

	for(int i=0;i<s.length();i++)
		if(s[i]!='+') 
			return false;
	return true;

}

string ff(int i,string s){
	for(int j=0;j<=i;j++){
		if(s[j]=='-') 
			s[j]='+';
		else 
			s[j]='-';
	}
	return s;
}

int main() {
	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin>>t;
	int k=0;
	while(t--){
		k++;
		string s;
		cin>>s;
		int n=0;
		int p=s.length()-1;
		for(int i=p;i>=0;i--){
 
			if(che(s)) break;
			if(s[i]=='-'){
				s=ff(i,s);
				n++;
			}
		}
		cout<<"Case #"<<k<<": "<<n<<endl;
	}
}
