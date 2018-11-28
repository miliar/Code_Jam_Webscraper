#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;
typedef long long ll;
const int MAXN = 3100;

ifstream fin ("A.in");
ofstream fout ("A.out");

int N, M;
vector <pair <int, int> > sval;
vector <pair <int, int> > poss;

ll takemod(ll a) {
	return ((a % 1000002013) + 1000002013) % 1000002013;
}

ll getcost(ll a) {
	return takemod(N * a - a * (a - 1) / 2);
}

inline bool cmp (pair <int, int> left, pair <int, int> right)
{
    if (left.first != right.first)
        return left.first < right.first;
    return left.second > right.second;
}

int main()
{
    int ntest; fin >> ntest;
    for (int test = 0; test < ntest; test++)
    {
    sval.clear();
    poss.clear();
    
    fout << "Case #" << test + 1 << ": ";
    
    fin >> N >> M;
	ll oritot = 0;
    for (int i = 0; i < M; i++)
    {
        int start, end, p;
        fin >> start >> end >> p;
        
        sval.push_back (make_pair (start, p));
        sval.push_back (make_pair (end, -p));
		
		int num = end - start;
		oritot += takemod(getcost(num) * p);
		oritot = takemod(oritot);
    }
    
    sort (sval.begin(), sval.end(), cmp);
	
	ll newtot = 0;
	
	for (int i = 0; i < sval.size(); i++)
	{
        //cout << sval[i].first << " " << sval[i].second << "\n";
        if (sval[i].second > 0)
            poss.push_back (sval[i]);
        else
        {
            sval[i].second = -sval[i].second;
            while (sval[i].second)
            {
                if (poss[poss.size()-1].second > sval[i].second)
                {
                    poss[poss.size()-1].second -= sval[i].second;
                    newtot += takemod (sval[i].second * getcost (sval[i].first - poss[poss.size()-1].first));
                    newtot = takemod (newtot);
                    break;
                }
                else
                {
                    //poss[poss.size()-1].second -= sval[i].second;
                    newtot += takemod (poss[poss.size()-1].second * getcost (sval[i].first - poss[poss.size()-1].first));
                    newtot = takemod (newtot);
                    sval[i].second -= poss[poss.size()-1].second;
                    poss.pop_back();
                }
            }
        }
    }
    
	
	/*ll s = 0;
	ll newtot = 0;
	vector<pair<int, ll> > upper;
	for (int i = 0; i < sval.size(); ) {
		int x = sval[i].first;
		while (i < sval.size() && sval[i].first == x) {
			s += sval[i].second;
			i++;
		}
		
		cout << i << " " << s << "\n";
		
		int mnx = x;
		while (upper.size() && s <= upper.back().second) {
			int px = upper.back().first;
			mnx = min(mnx, px);
			ll ps = upper.back().second;
			newtot += takemod(getcost(x - px) * (ps - s));
			cout << x << ' ' << px << ' ' << s << ' ' << ps << endl;
			newtot = takemod(newtot);
			upper.pop_back();
		}
		upper.push_back(pair<int, ll>(mnx, s));
		
	}*/
	//cout << oritot << " " << newtot << "\n";
	fout << takemod(oritot - newtot) << endl;
	}
	
	system ("Pause");
}
