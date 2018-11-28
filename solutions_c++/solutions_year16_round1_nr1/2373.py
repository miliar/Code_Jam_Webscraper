#include<bits/stdc++.h>
using namespace std;
string s , temp;
int main()
{
	int t , p = 0;
	cin>>t;
	while(t--)
	{
		p++;
		temp = "";
		cin>>s;
		int l = s.length();
		temp = temp + s[0];
		for(int i =1 ;i<l;i++)
		{
			if(s[i] >= temp[0])
			temp = s[i] + temp;
			else
			temp = temp + s[i];
		}
		cout<<"Case #"<<p<<": "<<temp<<endl;
	}
}
