#include<iostream>
#include<string>
#include<cmath>
#include<sstream>

using namespace std;

void result(int res)
{
	static int k=0;
	k++;
	cout<<"Case #"<<k<<":"<<" "<<res<<endl;
}

bool is_fair(int x)
{
	stringstream out;
	string s;
	out<<x;
	s=out.str();
	int len = s.size();
	if(len==1)
		return true;
	int flag=0;
	for(int i=0;i<len/2;i++)
	{
		if(s.at(i)!=s.at(len-i-1))
		{
			flag=1;
			break;
		}
	}
	if(flag)
		return false;
	else
		return true;	
}

bool is_square(int x)
{
	double v,f,diff;
	v=sqrt(x);	
	f=floor(v);
	
	diff = v-f;
	if(diff == 0)
	{
		if(is_fair((int)v)==1)
			return true;
		else
			return false;
	}
	else 
		return false;
}
int main()
{
	int n;
	int st,en,count;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		count=0;
		cin>>st>>en;
		for(int j=st;j<=en;j++)
		{
			if(is_fair(j)==1)
			{
				if(is_square(j)==1)
				{
					count++;
				}
			}
		}
		result(count);				
	}	
	return 0;
}
