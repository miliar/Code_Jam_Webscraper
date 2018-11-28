#include<iostream>
#include<cstring>
using namespace std;

char s[1111];
int main(){
	int n;
	cin>>n;
for(int t=1;t<=n;t++)	{
	cin>>s;
	int l=strlen(s);
	string an="";
	an=an+s[0];
	for(int i=1;i<l;i++){
		char c=an.at(0);
		if(c<=s[i])an=s[i]+an;
		else an=an+s[i];
	}
	cout<<"Case #"<<t<<": "<<an<<endl;
}
return 0;
}

