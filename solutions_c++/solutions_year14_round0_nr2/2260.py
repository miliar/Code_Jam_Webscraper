#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

#define rep(i,n) for(int i = 0; i < (n); ++i)
#define forr(i,a,b) for(int i = (a); i <= (b); ++i)

typedef long long ll;


double solve(double c, double f, double x)
{
	double ans = x / 2.;
	int fn = 0;
	double t = 0, cans;
	int badF = 0;
	while (badF < 100) // todo
	{
		t += c / (2. + f * fn);
		fn++;
		cans = t + x / (2. + f * fn);
		if (cans < ans)
		{
			ans = cans;
			badF = 0;
		}
		else
			badF++;
	}
	return ans;
}

int main()
{
#ifdef my_env_def
    freopen ("out.txt","w",stdout);
    freopen("in.txt","r",stdin);
#endif

    int t;
    cin >> t;
	double c, f, x;

	rep(tc,t)
	{
		cin >> c >> f >> x;
		double ans = solve(c,f,x);
		cout.precision(8);
		cout << "Case #" << tc + 1 << ": " << std::fixed << ans << "\n";
	}

#ifdef my_env_def
    fclose(stdout);
#endif
    return 0;
}