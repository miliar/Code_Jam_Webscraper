// 1A_A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <math.h>

using namespace std;

int main(int argc, char* argv[])
{
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        int count = 0;
        int a, b, k;
        cin >> a >> b >> k;
        for (int i = 0; i < a; ++i) {
            for (int j = 0; j < b; ++j) {
                if ((i & j) < k) {
                    ++count;
                }
            }
        }
        cout << "Case #" << t + 1 << ": " << count << endl;
    }
	return 0;
}

