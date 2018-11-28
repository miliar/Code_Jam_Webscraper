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
		int N;
		cin>>N;
		vector<double> nao(N);
		vector<double> ken(N);
		fori(i,0,N)	cin>>nao[i];
		fori(i,0,N)	cin>>ken[i];

		sort(nao.begin(),nao.end());
		sort(ken.begin(),ken.end());

		int y=0;
		
		int ni=N-1;
		int ki=N-1;
		fori(i,0,N)
		{
			if (ken[ki]>nao[ni])
				++y;
			else
				--ni;
			--ki;
		}

		y = N-y;
		int z=0;

		ni=N-1;
		ki=N-1;
		fori(i,0,N)
		{
			if (nao[ni]>ken[ki])
				++z;
			else
				--ki;
			--ni;
		}

		cout<<y<<" "<<z<<std::endl;
	}

	return 0;
}

