#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

const int MaxInt=numeric_limits<int>::max();
typedef vector<int> VI;
typedef vector<string> VS;
#define For(i,a,n) for (int i=a; i<n; ++i)
#define Fori(n) For(i,0,n)

struct S
{
	long long stacja, ile, x;
	bool we;

	bool operator<(const S &s) const
	{
		if (stacja!=s.stacja)
			return stacja<s.stacja;
		if (we!=s.we)
			return we;
		return x<s.x;
	}
};
long long n, m;

const int M=1000002013;
long long oplata(long long pocz, long long kon, long long ile)
{
	long long odl=kon-pocz, wyn=n*(n+1)/2-(n-odl)*(n-odl+1)/2;
	wyn%=M;
	wyn=wyn*ile%M;
	return wyn;
}

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
	cin>>n>>m;
	vector<S> p;
	long long x=0;
	Fori(m)
	{
		S s;
		int pocz, kon, ilu;
		cin>>pocz>>kon>>ilu;
		s.ile=ilu;
		s.x=i;
		s.we=true;
		s.stacja=pocz;
		p.push_back(s);
		s.we=false;
		s.stacja=kon;
		p.push_back(s);
		x=(x+oplata(pocz, kon, ilu))%M;
	}
	sort(p.begin(), p.end());
	long long ilu=0, opl=0;
	set<S> jada;
	Fori(m*2)
		if (p[i].we) 
		{
			ilu+=p[i].ile;
			jada.insert(p[i]);
		}
		else
		{
			while (p[i].ile)
			{
				set<S>::iterator it=jada.end();
				--it;
				S ss=*it;
				jada.erase(ss);
				long long il=min(p[i].ile, ss.ile);
				p[i].ile-=il;
				ss.ile-=il;
				if (ss.ile)
					jada.insert(ss);
				opl=(opl+oplata(ss.stacja, p[i].stacja, il))%M;
			}
		}
    cout<<"Case #"<<ca<<": "<<(x+M-opl%M)%M<<endl;
  }


  return 0;
}
