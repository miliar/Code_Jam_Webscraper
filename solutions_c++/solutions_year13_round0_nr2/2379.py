// c.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
//#include <cmath>
#include <cstdlib>

using namespace std;

#define fori(i_,f_,t_) for(int i_=f_;i_<t_;++i_)
#define fore(i_,c_) for(auto i_=c_.begin();i_!=c_.end();++i_)
#define pb	push_back


int main(int argc, char* argv[])
{
	int T;
	cin>>T;
	fori(t,0,T)
	{
		cout<<"Case #"<<t+1<<": ";
		int N,M;
		cin>>N>>M;
		vector<vector<int>> vvh(N);
		fori(n,0,N)
		{
			vector<int> vh(M);
			fori(m,0,M)
			  cin>>vh[m];
			vvh[n]=vh;
		}

		vector<int> maxn(N,0);
		vector<int> maxm(M,0);
		fori(n,0,N)
		{
			fori(m,0,M)
			{
				int h = vvh[n][m];
				if (h>maxn[n])
					maxn[n]=h;
				if (h>maxm[m])
					maxm[m]=h;
			}
		}

		bool p = true;
		fori(n,0,N)
		{
			fori(m,0,M)
			{
				int h = vvh[n][m];
				if (h<maxn[n] && h<maxm[m])
				{
					p = false;
					break;
				}
			}
			if (!p)	break;
		}

        cout<<(p?"YES":"NO")<<std::endl;
	}

	return 0;
}

