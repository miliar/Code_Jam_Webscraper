#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)

using namespace std;

typedef long long li;

const int N = 3000;

int n;
int x[N];
int y[N];
bool used[N];

vector<char> path;

vector<int> inc(vector<char> a)
{
	vector<int> result(a.size());
	forn(i, a.size())
	{
		result[i] = 1;
		forn(j, i)
			if (a[j] < a[i])
				result[i] = max(result[i], result[j] + 1);
	}
	return result;
}

pair< vector<int>,vector<int> > gen(vector<char> a)
{
	pair< vector<int>,vector<int> > p;
	p.first = inc(a);
	reverse(a.begin(), a.end());
	p.second = inc(a);
	reverse(p.second.begin(), p.second.end());
	reverse(a.begin(), a.end());
	return p;		
}


bool found;

void dfs(int pos)
{
	vector< vector<char> > ss;
	ss.push_back(vector<char>(1, 0));

	for (int i = 2; i <= n; i++)
	{
		vector< vector<char> > nxt;

		for (vector< vector<char> >::iterator j = ss.begin(); j != ss.end(); j++)
		{
			const vector<char>& v = *j;

			forn(last, i)
			{
				int tt = 1;

				forn(prev, i - 1)
					if (v[prev] < last)
						tt = max(tt, x[prev] + 1);

			    if (tt == x[i - 1])
			    {
			    	bool fail = false;
			    	forn(prev, i - 1)
			    		if (v[prev] >= last && y[prev] < y[i - 1])
			    		{
			    			fail = true;
			    			break;
			    		}

			    	if (!fail)
			    	{

    				vector<char> rr(i);
    				forn(t, i - 1)
    					rr[t] = v[t] < last ? v[t] : v[t] + 1;
    				rr[i - 1] = last;
					nxt.push_back(rr);

					}
			    }
			}
		}

		sort(nxt.begin(), nxt.end());
		nxt.erase(unique(nxt.begin(), nxt.end()), nxt.end());

		//if (nxt.size() > 2000000)
		//	nxt.erase(nxt.begin() + 2000000, nxt.end());
	
		cerr << i << " " << nxt.size() << endl;
		ss = nxt;
	}

	path = vector<char>(n + 1, n + 1);

	int iter = 0;

	for (vector< vector<char> >::iterator j = ss.begin(); j != ss.end(); j++)
	{
		pair<vector<int>,vector<int> > p = gen(*j);
   		bool fail = false;
   		forn(i, n)
   			if (p.first[i] != x[i] || p.second[i] != y[i])
   			{
   				fail = true;
   				break;
   			}
   		iter++;
		if (!fail)
		{
			path = min(path, *j);   
			cerr << "yes " << iter << endl;
			break;
		}
	}

	if (path[0] < n)
		found = true;
}

int main(int argc, char* argv[])
{
    // freopen("input.txt", "rt", stdin);

    int testCases;
    cin >> testCases;
	int result = 0;

    forn(tt, testCases)
    {
    	cin >> n;
    	
    	forn(i, n)
    		cin >> x[i];
    	forn(i, n)
    		cin >> y[i];

    	forn(i, n)
    		used[i] = false;

    	path.resize(n);
    	found = false;

    	dfs(0);

    	assert(found);

    	pair<vector<int>, vector<int> > p = gen(path);
	   	set<int> ss;

    	forn(i, n)
    	{
    		ss.insert(i);
	   		assert(p.first[i] == x[i]);
	   		assert(p.second[i] == y[i]);
	   	}
	   	assert(ss == set<int>(path.begin(), path.end()));

    	cout << "Case #" << (tt + 1) << ":";
    	forn(i, n)
    		cout << " " << path[i] + 1;
    	cout << endl;
    }

    return 0;
}
