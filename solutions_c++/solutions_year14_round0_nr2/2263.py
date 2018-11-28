// 1A_A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main(int argc, char* argv[])
{
    freopen ("B-large.in", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int k = 0; k < T; ++k) {
        long double eps = 1e-07;
        long double c, f, x;
        cin >> c >> f >> x;
        long double speed = 2;
        long double time = 0;
        while (x / speed > c / speed + x / (speed + f)) {
            time += c / speed;
            speed += f;
        }
        cout.precision(8);
        cout << "Case #" << k + 1 << ": " << std::fixed << time + x / speed << endl;
    }
	return 0;
}

