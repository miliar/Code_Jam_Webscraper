#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("A-large-practice.out","w",stdout);
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++){
		string s;
		int j,c=0;
		cin>>s;
		for(j=0;j<s.length()-1;j++){
			if(s[j]!=s[j+1]){
				c++;
			}
		}
		if(s[s.length()-1]=='-'){
			cout<<"Case #"<<i<<": "<<c+1<<endl;
		}
		else
		cout<<"Case #"<<i<<": "<<c<<endl;
	}
}
