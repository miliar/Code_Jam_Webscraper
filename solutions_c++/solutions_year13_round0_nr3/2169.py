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

inline bool ispalindrome(unsigned __int64 v)
{
	char vs[32];

	_ui64toa(v,vs,10);
	int l=strlen(vs)-1;
	int f=0;
	while(f<l)
	{
		if (vs[f]!=vs[l])
			return false;
		++f;
		--l;
	}
	return true;
}

typedef unsigned __int64 ui64;
int main(int argc, char* argv[])
{
	vector<ui64> fqs;
	fori(d,1,10)
	{
		ui64 v = d*d;
		if (ispalindrome(v))
			fqs.push_back(v);
	}

	int n=1;
	fori(k,1,3)
	{
	  fori(i,n,n*10)
  	  {
        

		fori(d,-1,10)
		{
			int a = i;
			ui64 v = i;
			if (d>=0)
				v = v* 10 + d;
			
			while(a)
			{	
				v = v*10 + a%10;
				a /= 10;
			}
			v = v*v;
			if (ispalindrome(v))
				fqs.push_back(v);
		}

	  }
	
	  n *=10;
	}	
#if 0
	cout<<"N: "<<fqs.size()<<std::endl;
	for(size_t i=0;i<fqs.size();++i)
	{
		cout<<i<<": "<<fqs[i]<<std::endl;
	}
#endif
	int T;
	cin>>T;
	fori(t,0,T)
	{
		cout<<"Case #"<<t+1<<": ";
		ui64 A,B;
		cin>>A>>B;
		int n=0;
		fore(pv,fqs)
		{
			ui64 v= *pv;
			if (v>=A && v<=B)
			{
				++n;
			}
		}
        cout<<n<<std::endl;
	}

	return 0;
}

