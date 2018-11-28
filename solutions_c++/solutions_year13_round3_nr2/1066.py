#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <deque>
#include <utility>
using namespace std;


/*int a=0,b=0;

pair<int,string> MIN(pair<int,string> a,pair<int,string> b,pair<int,string> c,pair<int,string> d)
{
	vector<pair<int,string>> v;
	v.push_back(a);
	v.push_back(b);
	v.push_back(c);
	v.push_back(d);
	sort(v.begin(),v.end());
	return v[0];
}


pair<int,string> GET(int x,int y,string s,int krok,int count)
{
	if(a==x && b==y)
		return make_pair(count,s);
	else
	{
		++krok;
		++count;
		return MIN((GET(x+1,y,s+"E",krok,count)),(GET(x-1,y,s+"W",krok,count)),(GET(x,y+1,s+"N",krok,count)),(GET(x,y-1,s+"S",krok,count)));
		//GET(x+1,y,s+"E",c);
		//GET(x-1,y,s+"W",c);
		//GET(x,y+1,s+"N",c);
		//GET(x,y-1,s+"S",c);
	}
}*/


string GET(int a,int b)
{
	string r="";
	int c=1;
	if(a>0)
	{
		int p=0;
		int co=1;
		while(p!=a)
		{
			if(co%2==1)
			{
				r+="W";
				p-=co;
			}
			else
			{
				r+="E";
				p+=co;
			}
			++co;
			++c;
		}
	}
	else
	{
		int p=0;
		int co=1;
		while(p!=a)
		{
			if(co%2!=1)
			{
				r+="W";
				p-=co;
			}
			else
			{
				r+="E";
				p+=co;
			}
			++co;
			++c;
		}
	}
	if(b>0)
	{	
		int p=0;
		int co=1;
		while(p!=b)
		{
			if(co%2==1)
			{
				r+="S";
				p-=co;
			}
			else
			{
				r+="N";
				p+=co;
			}
			++co;
			++c;
		}
	}
	else
	{	
		int p=0;
		int co=1;
		while(p!=b)
		{
			if(co%2!=1)
			{
				r+="S";
				p-=co;
			}
			else
			{
				r+="N";
				p+=co;
			}
			++co;
			++c;
		}
	}
	return r;
}





int main()
{
	freopen("C:\\in.txt","r",stdin);
	freopen("C:\\out.txt","w",stdout);
	int T;
	cin>>T;
	for(int i=1;i<=T;++i)
	{
		int a,b;
		cin>>a>>b;
		string S=GET(a,b);
		cout<<"Case #"<<i<<": "<<S<<endl;
	}
	//cout<<S.length()<<endl;
	return 0;
}