#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int t, num;
double d;

int game1(vector<double> n, vector<double> m)
{
	int ret=0;
	sort(n.begin(), n.end());
	vector<double>::iterator it;
	for(int i=0 ; i<m.size() ; i++)
	{
		it=lower_bound(n.begin(), n.end(), m[i]);
		if(it==n.end()) continue;
		else
		{
			ret++;
			n.erase(it);
		}
	}
	return ret;
}

int game2(vector<double> n, vector<double> m)
{
	int ret=0;
	sort(m.begin(), m.end());
	vector<double>::iterator it;

	for(int i=0 ; i<n.size() ; i++)
	{
		it=lower_bound(m.begin(), m.end(), n[i]);
		if(it==m.end()) ret++;
		else m.erase(it);
	}

	return ret;
}

int main(void)
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
#endif

	cin>>t;
	for(int j=1 ; j<=t ; j++)
	{
		vector<double> n, m;
		cin>>num;
		for(int i=0 ; i<num ; i++)
		{
			cin>>d;
			n.push_back(d);
		}
		for(int i=0 ; i<num ; i++)
		{
			cin>>d;
			m.push_back(d);
		}
		int sol1=game1(n, m), sol2=game2(n, m);
		cout<<"Case #"<<j<<": "<<sol1<<" "<<sol2<<endl;
	}
}