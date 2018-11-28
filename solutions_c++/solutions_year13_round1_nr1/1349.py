#include<iostream>
#include<stdio.h>
#include<string.h>
#include<cstdlib>
#include<set>
#include<vector>
#include<map>

using namespace std;

int main()
{

int t=0;
cin>>t;
int n=1;
int r,l;
int lim=0;

while(n<=t)
{
	cin>>r>>l;
	int count=0;
	for(int i=0;;i+=2)
	{
		lim=(r+i+1)*(r+i+1)-(r+i)*(r+i);
		l=l-lim;
		if(l>=0)count++;
		else break;
	}
	cout<<"Case #"<<n<<":"<<" "<<count<<endl;
	n++;
}
return 0;
}