//A
#include <bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	int t1=t;
	getchar();
	while(t--){
		cout<<"Case #"<<t1-t<<": ";
		string s;
		cin>>s;
		
		string res="";		
		//cout<<f<<endl;
		res=s[0];
		for (int i = 1; i < (int)s.size(); i++)
		{	
			if(s[i]>=res[0]){
				res=s[i]+res;
			}else{
				res+=s[i];
			}
		}
		
		cout<<res<<endl;
	}
	return 0;
}
