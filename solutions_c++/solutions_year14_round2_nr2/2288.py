#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>


using namespace std;

#define ll long long
#define ui unsigned int
#define debug(a) cout << #a << ": " << a << endl;
#define debugVector(a) cout << #a << ": "; for(ui i; i < a.size(); i++) {cout << a[i] << " ";} cout << endl;
#define pb(a) push_back(a)
#define init(); ofstream fOut; fOut.open ("result.txt");
#define case(i) fOut << "Case #" << (i) << ": "; cout << "Case #" << (i) << ": "

int main()
{
    init();
    int tests; cin >> tests;
    int A,B,K, t;
    for (int i = 1; i <= tests; i++) {
		cin >> A; cin >> B; cin >> K;

		ll pos = 0;
		//beide größer
		
		for (int k = 0; k < A; k++) {
			for (int l = 0; l < B; l++) {
				if ((k & l) < K) {
					pos++;
				}
			}
		}

		case(i);
		cout << pos << endl;
        fOut << pos << endl;
    }

}
