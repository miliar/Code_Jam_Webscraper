#include<iostream>
#include<string>
#include<sstream>
#include<math.h>
using namespace std;
bool ispalindrome(string n)
{
	int len = n.length();
	for(int i = 0 ;i<len;i++)
	{
		if(n[i]!=n[len-i-1])
			return false;
	}
	return true;
}
int main()
{
	int num=0;
	int a,b;
	int roota,rootb;
	int t;
	cin>>t;
	for(int i = 0;i<t;i++)
	{
		int count = 0;
		cin>>a>>b;
		roota = sqrt(a);
		rootb = sqrt(b);
		if(roota*roota < a)
			roota++;
		for(int j=roota;j<=rootb;j++)
		{
			num = j*j;
			stringstream sn,sn1;
			sn<<num;
			sn1<<j;
			sn1<<j;
			if(ispalindrome(sn.str())&&ispalindrome(sn1.str()))
				count++;
		}	
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
}
