#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	// your code goes here
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int q=1;q<=t;q++){
		int smax;
		cin>>smax;
		char s[smax+2];
		cin>>s;
		int tot=0,inv=0;
		for(int i=0;i<=smax;i++){
			if(tot>=i)
				tot+=(s[i]-'0');
			else{
				inv+=(i-tot);
				tot=i+(s[i]-'0');
			}
		}
		cout<<"Case #"<<q<<": "<<inv<<endl;
	}
	return 0;
}
