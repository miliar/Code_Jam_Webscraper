#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<sstream>
#include<algorithm>
#include<cstring>
#include<cmath>

typedef long long ll;

using namespace std;

int main()
{
	string inp;
	getline(cin,inp);
	int T=atoi(inp.c_str());
	for(int i=1;i<=T;i++)
	{
		getline(cin,inp);
		ll n=atol(inp.c_str());
		if((2*n)==n)
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else
		{
			bool notComplete=true;
			bool nums[10]={false,
						false,
						false,
						false,
						false,
						false,
						false,
						false,
						false,
						false};
			ll cnt=1;
			while(notComplete==true)
			{
				ll nm=cnt*n;
				ostringstream oo;
				oo<<nm;
				string nn=oo.str();
				for(int ii=0;ii<nn.length();ii++)
				{
					int k=(int)(nn.at(ii)-'0');
					if(nums[k]==false)
						nums[k]=true;
				}
				notComplete=false;
				for(int ii=0;ii<10;ii++)
				{
					if(nums[ii]==false)
						notComplete=true;
				}
				if(notComplete==true)
					cnt++;
			}
			cout<<"Case #"<<i<<": "<<cnt*n<<endl;
		}
	}
	return 0;
}

