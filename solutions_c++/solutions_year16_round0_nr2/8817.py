#include <iostream>
#include <string.h>
using namespace std;

int main() {
	int T;
	cin>>T;
	for(int k=1;k<=T;k++)
	{
		char str[102];
		cin>>str;
		int count = 0;
		int l = strlen(str)-1;
		for(int i=l; i>=0; i--)
		{
			if(i==l)
			{
				if(str[i]=='-') count++;
			}
			else if(str[i]!=str[i+1])
			{
				count++;
			}
		}
		cout<<"Case #"<<k<<": "<<count<<endl;
	}
	return 0;
}
