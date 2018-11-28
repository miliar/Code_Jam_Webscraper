#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <fstream>

using namespace std;

#define rep(i,n) for(int i = 0; i < (n); ++i)
#define forr(i,a,b) for(int i = (a); i <= (b); ++i)

typedef long long ll;

int move_el(vector<int>& vs, int f, int t)
{
	int ans = 0;
	int d = f < t ? 1 : -1;
	while (f != t)
	{
		swap(vs[f], vs[f+d]);
		f += d;
		ans++;
	}
	return ans;
}

int sortF(vector<int>& vs, int f, int l)
{
	int sw = 0;
	for(int i = f+1; i < l; ++i)
	{
		int j = i;
		while (j > f && vs[j] < vs[j-1])
		{
			swap(vs[j], vs[j-1]);
			++sw;
			--j;
		}
	}
	return sw;
}

int sortB(vector<int>& vs, int f, int l)
{
	int sw = 0;
	for(int i = f+1; i < l; ++i)
	{
		int j = i;
		while (j > f && vs[j] > vs[j-1])
		{
			swap(vs[j], vs[j-1]);
			++sw;
			--j;
		}
	}
	return sw;
}

bool checkUpDown(const vector<int>& vs)
{
	bool up = true;
	for (int i = 1; i < vs.size(); ++i)
	{
		if (up && vs[i] < vs[i-1])
			up = false;
		if (!up && vs[i] > vs[i-1])
			return false;
	}
	return true;
}

int cntSwaps(const vector<int>& a, vector<int> b)
{
	int ans = 0;
	rep(i,a.size())
	{
		int bi = find(b.begin() + i, b.end(), a[i]) - b.begin();
		ans += move_el(b, bi, i);
	}
	return ans;
}

int solve(vector<int> a)
{
	if (a.size() <= 2)
		return 0;

	vector<int> as = a;
	sort(as.begin(), as.end());
	int ans = 999000999;
	do
	{
		if (checkUpDown(as))
		{
			int cans = cntSwaps(a, as);
			if (cans < ans)
				ans = cans;
		}
	}
	while (next_permutation(as.begin(), as.end()));
	
	return ans;
}

int main()
{
    ofstream fout("out.txt");
    freopen("in.txt","r",stdin);
	freopen("debug.txt","w",stdout);

    int t;
    cin >> t;

	int n;
	vector<int> vs,cs;
	rep(tc,t)
	{
		cin >> n;
		vs.resize(n);
		rep(i,n)
			cin>>vs[i];

		//int mi = max_element(vs.begin(), vs.end()) - vs.begin();
		//int ans = 999000999;
		//rep(i,n)
		//{
		//	cs = vs;
		//	int cans = 0;
		//	//cans += move_el(cs, mi, i);
		//	cans += sortF(cs, 0, i);
		//	cans += sortB(cs, i, n);

		//	if (cans < ans)
		//		ans = cans;
		//}
		
		fout << "Case #" << tc + 1 << ": " << solve(vs) << "\n";
	}

    return 0;
}