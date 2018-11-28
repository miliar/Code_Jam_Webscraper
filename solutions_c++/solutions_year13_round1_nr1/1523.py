#include<iostream>
#include<fstream>
#include<sstream>
using namespace std;
int main()
{
	long long r,T,t,i,j,k,cnt;;
	unsigned long long x,y;
	//fstream cin;
	//cin.open("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2013\\Round 1A\\A\\Small Input.txt",ios::in);
	//freopen("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2013\\Round 1A\\A\\Small Output.txt","w",stdout);
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>r>>T;
		x=T;
		cnt=1;
		y=2*r+1;
		x-=y;
		r+=2;
		y=2*r+1;
		while(x>=y)
		{
			x-=y;
			cnt++;
			r+=2;
			y=2*r+1;
		}
		cout<<"Case #"<<k<<": "<<cnt<<endl;
	}
	return 0;
}