#include <iostream>
using namespace std;

int main() {
	int t,tt,ret;
	string s;
	cin>>t;
	tt=t;
	while(tt--)
	{
		ret=0;
		cin>>s;
		for(int q=0;s[q]!='\0';q++)
		{
			if(s[q+1]=='\0' && s[q]=='-')
				ret++;
			else
				if(s[q+1]!='\0' && s[q]!=s[q+1])
					ret++;
		}
		cout<<"Case #"<<t-tt<<": "<<ret<<endl;
	}
	return 0;
}