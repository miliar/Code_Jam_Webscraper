// 2013_QD.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

// template

#include "stdafx.h"

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

//#define pb push_back
//#define all(v) v.begin(),v.end()
//#define rall(v) v.rbegin(),v.rend()
//#define sz size()
//#define rep(i,m) for(int i=0;i<(int)(m);i++)
//#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
//#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
//#define mem(a,b) memset(a,b,sizeof(a))
//#define mp make_pair
//#define dot(a,b) ((conj(a)*(b)).X)
//#define X real()
//#define Y imag()
//#define length(V) (hypot((V).X,(V).Y))
//#define vect(a,b) ((b)-(a))
//#define cross(a,b) ((conj(a)*(b)).imag())
//#define normalize(v) ((v)/length(v))
//#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
//#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)
//
//typedef stringstream ss;
//typedef pair<int, int> pii;
//typedef vector<pii> vpii;
//typedef vector<string> vs;
//typedef vector<int> vi;
//typedef vector<double> vd;
//typedef vector<vector<int> > vii;
//typedef long long ll;
//typedef long double ld;
//typedef complex<double> point;
//typedef pair<point, point> segment;
//typedef pair<double, point> circle;
//typedef vector<point> polygon;

struct chest
{
	int openkey;
	vector<int> keys;
	bool locked;
};


int keys[201];

chest cc[201];
int K, N;
vector<int> ans;

int locks[201];
int allkeys[201];
bool early_terminate()
{

	memset(locks, 0, sizeof(locks));
	memset(allkeys, 0, sizeof(allkeys));
	for (int i=1; i<=N; i++)
		allkeys[i] = keys[i];
	for (int i=1; i<=N; i++)
	{
		locks[cc[i].openkey] ++;
		for (int j = 0; j < cc[i].keys.size(); j++)
			allkeys[(cc[i].keys)[j]] ++;
	}
	for (int i=1; i<=N; i++)
		if (locks[i] > allkeys[i]) return true;
	return false;
}

bool locked[201];

bool Tryout(int opened, int nokey)
{
	bool flag;
	if (opened + nokey == N) return true;
	for (int i=1; i<=N; i++)
	{
		if ((locked[i]) && (allkeys[cc[i].openkey] > 0) && (cc[i].keys.size() > 0))
		{
			//update state
			locked[i] = false;
			allkeys[cc[i].openkey] --;
			for (int j = 0; j < cc[i].keys.size(); j++)
				allkeys[(cc[i].keys)[j]] ++;
			opened++;
			if (opened + nokey == N) return true;
			if (Tryout(opened, nokey)) return true;
			//roll back
			for (int j = 0; j < cc[i].keys.size(); j++)
				allkeys[(cc[i].keys)[j]] --;
			locked[i] = true;
			allkeys[cc[i].openkey] ++;
			opened--;
		}
	}
	return false;
}

// check if current state can go to the end
bool greed_try()
{
	int opened = 0;
	// copy current state
	for (int i=1; i<=200; i++)
		allkeys[i] = keys[i];
	for (int i=1; i<=N; i++)
	{
		locked[i] = cc[i].locked;
		if (locked[i] == false) opened ++;
	}
	int k = 1;
	while (k <= N)
	{
		if ((locked[k]) && (allkeys[cc[k].openkey] > 0) && (find(cc[k].keys.begin(), cc[k].keys.end(), cc[k].openkey) != cc[k].keys.end()))
		{
			opened ++;
			locked[k] = false;
			allkeys[cc[k].openkey]--;
			for (int i=0; i<cc[k].keys.size(); i++)
				allkeys[(cc[k].keys)[i]]++;
			k = 1;
		}
		else k++;
	}
	if (opened == N) return true;

	int nokey=0;
	for (int i=1; i<=N; i++)
		if ((locked[i]) && (cc[i].keys.size() == 0)) nokey++;
	// pick locks has a key inside
	bool flag = Tryout(opened, nokey);
	if (!flag) return false;
	else if (nokey == 0) return true;
	else
	{
		for (int i =1; i<=N; i++)
		{
			if (locked[i] == false) continue;
			if (allkeys[cc[i].openkey] == 0) return false;
			else
			{
				locked[i] = false;
				allkeys[cc[i].openkey] --;
			}
		}
		return true;
	}
}

void Solve()
{
	int opened = 0;
	int i=1;
	while (opened < N)
	{
		while (!((cc[i].locked) && (keys[cc[i].openkey] > 0))) i++;
		//update state
		cc[i].locked = false;
		keys[cc[i].openkey] --;
		for (int j = 0; j < cc[i].keys.size(); j++)
			keys[(cc[i].keys)[j]] ++;
		opened++;
		ans.push_back(i);
		if (greed_try() == false)
		{
			//roll back
			ans.pop_back();
			for (int j = 0; j < cc[i].keys.size(); j++)
				keys[(cc[i].keys)[j]] --;
			cc[i].locked = true;
			keys[cc[i].openkey] ++;
			opened--;
			i++;
		}
		else
		{
			i=1;
		}
	}
}
#define SMALL
//#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("D-small-attempt2.in","rt",stdin);
	freopen("D-small1.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large-practice.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	int T;
	int key,num;
	string str;
	string snum;
	int pos;
	bool found;
	cin >> T;
	for (int i = 1; i<=T; i++)
	{
		memset(keys, 0, sizeof(keys));
		cin >> K >> N;
		for (int j=1; j<=K; j++)
		{
			cin >> key;
			keys[key] ++;
		}
		for (int j=1; j<=N; j++)
		{
			cin >> cc[j].openkey;
			cc[j].locked = true;
			cc[j].keys.clear();
			cin >> num;
			for (int k =0; k<num; k++)
			{
				cin >> key;
				cc[j].keys.push_back(key);
			}
		}
		ans.clear();
		if (early_terminate())
			found = false;
		else if (greed_try())
		{
			found = true;
			Solve();
		}
		else 
			found = false;
		cout << "Case #" << i << ": ";
		if (found)
			for (int j =0; j<ans.size(); j++)
				cout << ans[j] << " ";
		else
			cout << "IMPOSSIBLE";
		cout << endl;
	}
}







