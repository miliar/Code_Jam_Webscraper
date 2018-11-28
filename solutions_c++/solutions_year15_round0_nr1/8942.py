#include <iostream>

using namespace std;

int main(){
	int t,x=1;
	cin>>t;
	while(t--){
		int n;
		string s;
		cin>>n;
		cin>>s;
		int tot=0,need=0;
		tot=s[0]-'0';
		for(int i=1;i<(int)s.size();i++){
			if(s[i]>'0' and tot<i)
				need+=(i-tot),tot=i;
			tot+=s[i]-'0';
		}
		cout<<"Case #"<<x<<": "<<need<<"\n";
		x++;
	}
	return 0;
}