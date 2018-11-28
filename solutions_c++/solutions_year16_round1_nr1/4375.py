#include <iostream>
#include <string>
using namespace std;
int main()
{
	int t,i;
	string str,temp;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		cin>>str;
		temp=str[0];
		for(i=1;i<str.length();i++)
			if(str[i]>=temp[0])
				temp=str[i]+temp;
			else
				temp+=str[i];
		cout<<"Case #"<<k<<": "<<temp<<endl;
	}
	return 0;
}