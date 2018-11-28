#include <iostream>
#include <stdio.h>
using namespace std;

long int func()
{
	long int n,cnt=0;
	string str;
	cin>>n>>str;
	long int already_standing = str[0]-'0';
	for(long int i=1;i<=n;i++)
	{
		if((str[i-1]=='0')&&(already_standing <i))
			already_standing = i,cnt++;
		already_standing += (str[i]-'0');	
	}
	return cnt;
}

int main()
{
	//freopen("1.in","r",stdin);
	//freopen("aout.out","w",stdout);
	long int t;
	cin>>t;
	for(long int i=0;i<t;i++)
	    cout<<"Case #"<<i+1<<": "<<func()<<"\n";
	return 0;
}