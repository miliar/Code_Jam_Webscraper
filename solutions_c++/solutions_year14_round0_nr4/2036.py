#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

#define rep(i,n) for(int i = 0; i < (n); ++i)
#define forr(i,a,b) for(int i = (a); i <= (b); ++i)

typedef long long ll;

int scoreWar(const vector<double>& a, const vector<double>& b)
{
	int score = a.size();
	for (int bi = b.size()-1, ai = a.size()-1; bi >= 0; --bi)
	{
		while (ai >= 0 && b[bi] < a[ai])
			--ai;

		if (ai < 0)
			break;

		--ai;
		score--;
	}
	return score;
}

int scoreDWar(const vector<double>& a, const vector<double>& b)
{
	return a.size() - scoreWar(b,a);

	//int score = a.size();
	//for (int ai = 0, bi = b.size()-1; ai < a.size() && a[ai] < b[bi]; ++ai, --bi)
	//	score--;
	//return score;
}


int main()
{
#ifdef my_env_def
    freopen ("out.txt","w",stdout);
    freopen("in.txt","r",stdin);
#endif

    int t;
    cin >> t;
	int n;
	vector<double> a,b;
	rep(tc,t)
	{
		cin >> n;
		
		a.resize(n);
		rep(i,n)
			cin >> a[i];

		sort(a.begin(), a.end());

		b.resize(n);
		rep(i,n)
			cin >> b[i];

		sort(b.begin(), b.end());
		
		cout << "Case #" << tc + 1 << ": " << scoreDWar(a,b) << " " << scoreWar(a,b) << "\n";
	}

#ifdef my_env_def
    fclose(stdout);
#endif
    return 0;
}