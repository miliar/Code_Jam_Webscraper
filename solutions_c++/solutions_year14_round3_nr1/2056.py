#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>

using namespace std;

int gcd(int n,int m){return m==0?n:gcd(m,n%m);}

bool poss(int a, double n)
{
	if (n == 1)
	{
		return true;
	}
	else if((a=0) || (n<1))
	{
		return false;
	}
	else
	{
		return poss(a-1,n/2);
	}
}

int main()
{
	int t;
	cin>>t;
	int p,q,g,gen;
	string in;
	for (int j=0; j<t; j++)
	{
		gen=0;
		cin>>in;
		for (int i=0; i<in.length(); i++)
		{
			if (in[i]=='/')
			{
				p=atoi(in.substr(0,i).c_str());
				q=atoi(in.substr(i+1,in.length()).c_str());
			}
		}
		g = gcd(p,q);
		p=p/g;
		q=q/g;
		if (poss(40,q)){
			while(true)
			{
				while(2*p<q)
				{
					gen++;
					q=q/2;
				}
				if (poss(40-gen,q))
				{
					cout<<"Case #"<<j+1<<": "<<gen+1<<endl;
					break;
				}
				else
				{
					cout<<"Case #"<<j+1<<": impossible"<<endl;
					break;
				}
			}
		}
		else{
			cout<<"Case #"<<j+1<<": impossible"<<endl;
		}
	}
}
