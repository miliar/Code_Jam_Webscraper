#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

int main()
{
int T,s,k=0;
string str;
cin >> T;
while(k<T)
{
k++;
cin>> s; cin>>str;
long int N=0,R=0;

	for(int i=0; i<str.length();i++)
	{
		if(N<i && ((int)str[i]-48)>0)
		{
		R+=i-N;
		N+=i-N;
		}
		N+=(int)str[i]-48;
	//	cout<<N;	
	}
cout<<"Case #"<<k<<": "<<R<<endl;
}


return 0;
}
