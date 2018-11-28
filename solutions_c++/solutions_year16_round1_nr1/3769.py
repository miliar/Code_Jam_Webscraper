#include <iostream>

using namespace std;

int main()	{
	int t,len,i,c;
	cin>>t;
	string str,res;
	c=0;
	while(t--)	{
		c++;
		cin>>str;
		len = str.length();
		res = str[0];
		for(i=1;i<len;i++)	{
			if(str[i]<res[0])	
				res = res + str[i];
			else
				res = str[i] + res;
		}
		cout<<"Case #"<<c<<": "<<res<<endl;
		//cout<<res<<endl;
	}
	return 0;
}