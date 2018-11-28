#include <iostream>
#include <cstring>
#include <stack>
#include <cstdio>
#include <map>
using namespace std;
#define LL long long
#define MOD 1000000007
#define pcc pair<char,char>
#define ff first
#define ss second


int main()
{
freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);	
int t;
cin>>t;int cc=0;
int x,r,c;
while(t--)
{
	cc++;
	string anse="RICHARD";
	cin>>x>>r>>c;
	if(x==1)
	{
		anse="GABRIEL";
		
	}
	else if(x==2)
	{
		if((r*c)%2 != 0);
		else
		anse="GABRIEL";
	}
	else if(x==3)
	{
		if((r*c)%3 != 0 || min(r,c)==1);
		else
		anse="GABRIEL";
	}
	else if(x==4)
	{
		if((r*c)%4 != 0);
		else if(r%4 && c%4);
		else if(min(r,c)<3);
		else
		anse="GABRIEL";
	}
	
	
	
	
	
	
	cout<<"Case #"<<cc<<": "<<anse<<"\n";
}
    
  return 0;
}

