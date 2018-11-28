#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstdio>
#define uint long long int
#define MP make_pair
#define PB push_back
using namespace std;
int n;
vector< pair<uint, uint> > wek; 
vector< pair<uint, uint> > newwek; 
uint rek(vector<pair<uint, uint> > w)
{
	if (w.empty())
	{
		return 0;
	}
	uint mini = 1001 * 1001 * 1000;
	uint pref = 0; 
	// cout<<"d1"<<endl;
	for (int i = 0; i < w.size(); i++)
	{
		pref += w[i].first;
		mini = min(mini, w[i].second);
	}
	uint wynik = mini * (pref * n - pref * (pref - 1) / 2);
	vector<pair<uint, uint> > acc;
	while(!w.empty())
	{
		// cout<<"d2"<<endl;
		if (w.back().second == mini)
		{
			wynik += rek(acc);
			acc.clear();
		}
		else
		{
			acc.PB(MP(w.back().first, w.back().second - mini));
		}
		w.pop_back();
	}
	wynik += rek(acc);
	return wynik;
}
int main()
{
	ios_base::sync_with_stdio(0);
	
	int test;
	cin>>test;
	for (int y = 1; y <= test; y++)
	{
		cout<<"Case #"<<y<<": ";
		cin>>n;
		uint wynik = 0;
		uint cost = 0;
		int m;
		cin>>m;
		for (int i = 1; i <= m; i++)
		{
			int o, e, p;
			cin>>o>>e>>p;
			wek.PB(MP(o, p));
			wek.PB(MP(e, -p));
			uint odl = e - o;
			cost += p * (odl * n - odl * (odl - 1) / 2);
		}
		sort(wek.begin(), wek.end());
		uint akt = 0;
		for (int i = 0; i < wek.size(); i++)
		{
			//cout<<wek[i].first<<" w "<<wek[i].second<<endl;
			if (i && wek[i].first != wek[i - 1].first)
			{
				newwek.PB(MP(wek[i].first - wek[i - 1].first, akt));
			}
			akt += wek[i].second;
		}
		/* for (int i = 0; i < newwek.size(); i++)
		{
			cout<<newwek[i].first<<" "<<newwek[i].second<<endl;
		} */
		wynik = rek(newwek);
		cout<<cost - wynik<<endl;
		wek.clear();
		newwek.clear();
	}
	return 0;
		

}