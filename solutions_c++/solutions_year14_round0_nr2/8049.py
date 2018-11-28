//
// Google Code Jam 2014
// Qualification Round
// Problem B: Cookie Clicker Alpha
//

#include <iostream>
#include <iomanip>

using namespace std;

void testcase()
{
    double target_cookies; // X
    double cost_factory; // C
    double factory_cps; // F

    cin >> cost_factory >> factory_cps >> target_cookies;

    double total_time = 0;
    double current_rate = 2;

    // start loop
    double time_not_buying;
    double time_buying;

    while (true) {
	time_not_buying = target_cookies / current_rate;
	time_buying = (cost_factory / current_rate) + (target_cookies / (current_rate + factory_cps));

	if (time_buying < time_not_buying) {
	    total_time += cost_factory / current_rate;
	    current_rate += factory_cps;
	} else {
	    total_time += time_not_buying;
	    cout << total_time << endl;
	    break;
	}
    }
}

int main()
{
    ios_base::sync_with_stdio(false);

    int cases;
    cin >> cases;

    cout << setprecision(7) << fixed;

    for (int i = 1; i <= cases; i++) {
	cout << "Case #" << i << ": ";
	testcase();
    }
}
