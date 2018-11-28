#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <sstream>
#include <list>
#include <set>
#include <map>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

struct Atak
{
	int d;

	int i, j, w;
};

bool operator<(const Atak& a1, const Atak& a2)
{
	return a1.d < a2.d;
}

const int W_SIZE=10000;
const int W_SHIFT=W_SIZE/2;
int wall[W_SIZE];
vector<Atak> a;

bool check(int i)
{
	for(int l=a[i].i; l<=a[i].j; ++l)
		if(wall[l] < a[i].w)
			return true;
	return false;
}

void req(int i)
{
	for(int l=a[i].i; l<=a[i].j; ++l)
		if(wall[l] < a[i].w)
			wall[l] = a[i].w;
}

int solve()
{
	int i,j,ans=0;
	for(i=0; i<a.size(); ++i)
	{
		for(j=i; j<a.size(); ++j)
		{
			if(a[j].d != a[i].d)
				break;
			if(check(j))
				++ans;
		}
		for(j=i; j<a.size(); ++j)
		{
			if(a[j].d != a[i].d)
				break;
			req(j);
		}
		i = j - 1;
	}
	return ans;
}

int main()
{
	int t,tt,i,l;
	fin>>tt;
	for(t=1; t<=tt; ++t)
	{
		fin>>l;
		a.clear();
		for(i=0; i<W_SIZE; ++i)
			wall[i] = 0;

		for(i=0; i<l; ++i)
		{
			int d,n,w,e,s,dd,dp,ds;
			fin>>d>>n>>w>>e>>s>>dd>>dp>>ds;
			w*=2;
			e*=2;
			dp*=2;
			for(int k=0; k<n; ++k)
			{
				Atak aa;
				aa.d = d;
				aa.i = w + W_SHIFT;
				aa.j = e + W_SHIFT;
				aa.w = s;
				a.push_back(aa);

				d+=dd;
				w+=dp;
				e+=dp;
				s+=ds;
			}
		}
		sort(a.begin(), a.end());
		fout<<"Case #"<<t<<": "<<solve()<<endl;
	}
	return 0;
}
