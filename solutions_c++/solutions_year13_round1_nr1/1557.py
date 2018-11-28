#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("aout", "w", stdout);
    int T;
    cin >> T;
    for(int iCase = 1; iCase <= T; ++iCase)
    {
	long long r, t;
	cin >> r >> t;
	long long er = r + 1;
	long long demand = er*er - r*r;
	long long ans = 0;
	while( t >= demand )
	{
	    ++ans;
	    t -= demand;
	    er += 2;
	    r += 2;
	    demand = er*er - r*r;
	}
	cout << "Case #" << iCase << ": " << ans << endl;
    }
}
