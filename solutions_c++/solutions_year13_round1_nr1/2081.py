#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<cstdio>
#define ll long long
using namespace std;


ll get_answer(ll r, ll t)
{
	ll required=0,count=0,r1=r,r2=r1+1;
	while(1)
	{
		required=(r2*r2-r1*r1);
		if(t>=required)
		{
			t=t-required;
			//cout<<"r1= "<<r1<<" r2="<<r2<<endl;
			r1=r2+1;
			r2=r1+1;
			++count;
		}
		else
			break;
	}

	return count;
}
int main()
{
	ll r,t,test;
	ifstream infile;
	ofstream outfile;
  	infile.open("A-small-attempt0.in");
  	outfile.open("b-output.out");
  	if (infile.is_open())
	{
		infile>>test;

		ll k=0;
		while(test--)
		{
			infile>>r;
			infile>>t;

			ll ans=get_answer(r,t);

			outfile<<"Case #"<<++k<<": "<<ans<<endl;

		}
	  	
	}	
	infile.close();
	outfile.close();
  return 0;
}
