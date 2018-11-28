#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include<cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;


int main()
{
    ios_base::sync_with_stdio(false);
	freopen("input_2_b.txt", "rt", stdin);
	freopen("output_2_b.txt", "wt", stdout);

	int t;
	double c,f,x;
	cin >> t;
	for(int k = 1; k <= t; k++) {
        cin >> c >> f >> x;
        if(c >= x) cout << "Case #" << k << ": " << fixed << setprecision(7) << (double)x/2 << endl;
        else {
            double time = (double)c/2, curr = (double)c, rate = 2.0;
            while(1) {
                double a = (double)(x-curr)/rate;
                double b = (double)x/((double)(rate+f));
                if(time + a <= time + b) {
                    cout << "Case #" << k << ": " << fixed << setprecision(7) << time + a << endl;
                    break;
                }
                else {
                    rate += f;
                    double val = (double)c/rate;
                    time += (double)val;
                }
            }
        }
	}
}
