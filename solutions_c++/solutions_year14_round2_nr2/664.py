#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{
	long long r,T,t,i,j,k,cnt,l,m,a,g,b,n,x;
	//fstream cin;
	//cin.open("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2014\\Round 1B\\B\\Small Input.txt",ios::in);
	//freopen("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2014\\Round 1B\\B\\Small Output.txt","w",stdout);
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cout<<"Case #"<<k<<": ";
		cin>>a>>b>>l;
		cnt=0;
		for(i=0;i<a;i++)
		for(j=0;j<b;j++)
		if((i&j)<l)
            cnt++;
		cout<<cnt<<endl;
	}
	return 0;
}