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
		double C,F,X;
		cin>>C>>F>>X;
		int n = (int)floor(X/C-2/F);
		double s=0.0;
		if (n<0) n=0;
 		fori(i,0,n)
		{
			s += C/(2.0+F*i);
		}

		s+= X/(2.0+F*n);

		cout.setf(ios_base::fixed);
		cout.precision(7);
        cout<<s<<std::endl;
	}

	return 0;
}

