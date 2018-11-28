#include <iostream>
#include <map>
#include <vector>

using namespace std;

//void addToMap(map<int, int>&m, int idx, int n)
//{
//	if (m.find(idx) == m.end())
//		m[idx] = n;
//	else
//		m[idx]
//}

typedef long long llong;

llong pay(int N, int from, int to, llong npeope)
{
	llong n = to - from;
	return n*(2*N-n+1)/2*npeope;
}

int main()
{
	int T;
	cin>>T;
	vector<pair<int, llong> >a;
	for (int z = 0; z < T; ++z)
	{
		int N, M;
		cin>>N>>M;
		map<int, int> in, out;
		llong plain = 0, best = 0;
		for (int i = 0, o, e, p; i < M; ++i)
		{
			cin>>o>>e>>p;
			in[o] = in[o] + p;
			out[e] = out[e] + p;
			plain += pay(N, o, e, p);
		}
		
		a.clear();
		map<int, int>::iterator iin = in.begin(), iout = out.begin();		

		while (iout != out.end())
		{	
			int st = 0;
			llong delta = 0;
			if (iin == in.end() || iin->first > iout->first)
			{
				st = iout->first;
				delta = -iout->second;
				++iout;
			}
			else if (iin->first < iout->first)
			{
				st = iin->first;
				delta = iin->second;
				++iin;				
			}			
			else
			{
				st = iout->first;
				delta = iin->second - iout->second;
				++iin;
				++iout;
			}
			if (delta > 0)
			{
				a.push_back(make_pair(st, delta));
			}
			else
			{
				delta = -delta;
				for (int i = a.size() - 1; delta > 0; --i)
				{
					llong np = min(delta, a[i].second);
					best += pay(N, a[i].first, st, np);
					delta -= np;
					a[i].second -= np;
					if (a[i].second == 0)
						a.erase(a.begin() + i);
				}
			}
		}
		cout<<"Case #"<<(z+1)<<": "<<plain - best<<endl;
	}
	return 0;
}

