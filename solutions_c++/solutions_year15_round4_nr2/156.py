#include <bits/stdc++.h>
using namespace std;

const long double EPS = 0.00000001;

int main()
{
	int t;
	cin >> t;
	for(int ta=1;ta<=t;++ta)
	{
		cout << "Case #" << ta << ": ";
		int n;
		long double v, x;
		cin >> n >> v >> x;
		vector<pair<long double,long double> > inp(n);
		for(int i=0;i<n;++i)
			cin >> inp[i].second >> inp[i].first;
		sort(inp.begin(),inp.end());
		if(inp[0].first > x+EPS || inp.back().first < x-EPS)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			long double tr=0, trc=0;
			for(int i=0;i<n;++i)
			{
				tr += inp[i].second;
				trc += inp[i].first*inp[i].second;
				//cout << endl << tr << ' ' << trc;
			}
			if(trc/tr < x)
			{
				//cout << endl << "d:" << tr << ' ' << trc;
				int i=-1;
				while(i<n-1 && trc/tr+EPS < x)
				{
					//cout << endl << "d:" << tr << ' ' << trc;
					i++;
					tr -= inp[i].second;
					trc -= inp[i].first*inp[i].second;
				}
				//cout << endl << "d:" << tr << ' ' << trc;
				if(i>-1)
				{
					long double r;
					if(i==n-1)
						r = inp[i].second;
					else
						r = (tr*x-trc)/(inp[i].first-x);
					//cout << endl << "d" << r << endl;
					tr += r;
					trc += inp[i].first*r;
				}
				
				printf("%Lf\n",v/tr);
			}
			else
			{
				//cout << endl << "c:" << tr << ' ' << trc;
				int i=n;
				while(i>0 && trc/tr-EPS > x)
				{
					//cout << endl << "c:" << tr << ' ' << trc << ' ' << trc/tr << ' ' << x;
					i--;
					tr -= inp[i].second;
					trc -= inp[i].first*inp[i].second;
				}
				//cout << endl << "c:" << tr << ' ' << trc;
				if(i<n)
				{
					long double r;
					if(i==0)
						r = inp[i].second;
					else
						r = (tr*x-trc)/(inp[i].first-x);
					//cout << endl << "c" << r << endl;
					tr += r;
					trc += inp[i].first*r;
				}
				
				printf("%Lf\n",v/tr);
			}
		}
	}
}
