#include <string>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
#include <iomanip> 

using namespace std;

const double PI = 2 * acos(0);
const double eps = 1e-9;

//#define SMALL
#define LARGE
int main() {
#ifdef SMALL
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif

	int n, N;

    double res = 0;

	cin >> N;
    string trash;
    getline(cin, trash);

    
    cout << std::fixed;

    for (int nn = 1; nn<N+1; ++nn) {
        res = 0;
        double cost, farm, target;

        string temp, s;
        getline(cin, temp);

        stringstream ss(temp);
        ss >> s;
        cost = stof(s);
        
        ss >> s;
        farm = stof(s);
        
        ss >> s;
        target = stof(s);

        double rate = 2.;


        double buyTime = cost/rate + target/(rate+farm);
        double withstandTime = target / rate;

        while(buyTime < withstandTime) {
            res += cost/rate;
            rate += farm;

            buyTime = cost/rate + target / (rate+farm);
            withstandTime = target / rate;
        }

        res += withstandTime;



        cout<<"Case #" << nn << ": ";
        cout << setprecision(7) << res << endl;
    }
    return 0;
}

