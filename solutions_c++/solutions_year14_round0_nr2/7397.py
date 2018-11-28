#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

double solve();

int main()
{
    cout << fixed;
    cout << setprecision(7);
    int T;
    cin >> T;
    for(int i=1; i<=T; ++i)
    {
	cout << "Case #" << i << ": " << solve() << endl;
    }

    return 0;
}


double solve()
{
    double C, F, X;
    cin >> C >> F >> X;

    if(C >= X)
    {
	return X/2;
    }

    double pgoal = max(2.0, F*(X - C)/C);

    int nr_farms = ceil((pgoal-2)/F); 
    
    double p_actual = 2.0 + nr_farms*F;

    double time_to_get_farms = 0;
    for(int i=0; i<nr_farms; ++i)
    {
	time_to_get_farms += C/(2.0+i*F);
    }
    

    return time_to_get_farms + X/p_actual;
}
