// a.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
//#include <cmath>
#include <string>
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
		int N;
		cin>>N;
		vector<vector<int>> vs(N);
		bool fail=false;
		string bs;
		fori(n,0,N)
		{
			string s;
			cin>>s;
			
			char p=0;
			int k=-1;
			fori(i,0,s.size())
			{
				char c=s[i];
				if (c==p)
				{
					++vs[n].at(k);
				} else
				{
					vs[n].push_back(1);
					if (n==0)
						bs += c;
					else if ((k+1) >= bs.size() || bs[k+1]!=c)
					{
						fail=true;
						break;
					}
					++k;
					p=c;
				}
			}
			if (fail || bs.size()!=(k+1))
			{
				fail = true;
				break;
			}
		}

		std::cout<<"Case #"<<t+1<<": ";

		int r = 0;
		if (!fail)
		{
			fori(i,0,bs.size())
			{
				
				vector<int> d;
				fori(n,0,N)
				{
					d.push_back(vs[n].at(i));
				}

				sort(d.begin(),d.end());
				
				int a = d[d.size()/2];

				fori(n,0,N)
				{
					r += abs(a - d[n]);
				}

			}
			std::cout<<r;
		} else
			std::cout<<"Fegla Won";
		

        std::cout<<std::endl;
	}

	return 0;
}

