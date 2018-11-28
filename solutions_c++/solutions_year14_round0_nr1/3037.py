// a.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
//#include <cmath>
#include <cstdlib>

using namespace std;

#define fori(i_,f_,t_) for(int i_=(f_);i_<(t_);++i_)
#define fore(i_,c_) for(auto i_=c_.begin();i_!=c_.end();++i_)
#define pb	push_back


int main(int argc, char* argv[])
{
	int T;
	cin>>T;
	fori(t,0,T)
	{
		cout<<"Case #"<<t+1<<": ";
		int z;
		int r;
		int a[4];
		cin>>r;
		--r;
		
		fori(i,0,4)
		{
			if (i==r)
			{
				fori(k,0,4)	cin>>a[k];
			} else
			{
				fori(k,0,4)	cin>>z;
			}

		}
		sort(a,a+4);
		int b[4];
		cin>>r;
		--r;
		fori(i,0,4)
		{
			if (i==r)
			{
				fori(k,0,4)	cin>>b[k];
			} else
			{
				fori(k,0,4)	cin>>z;
			}

		}
		sort(b,b+4);
		int c[4]={0,0,0,0};

		set_intersection(a,a+4,b,b+4,c);

		if (c[0]==0)
			cout<<"Volunteer cheated!";
		else if (c[1]!=0)
			cout<<"Bad magician!";
		else
			cout<<c[0];
		cout<<std::endl;
	}

	return 0;
}

