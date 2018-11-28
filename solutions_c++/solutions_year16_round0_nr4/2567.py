#include <iostream>
#include <string>
#include <vector>
#include <math.h>
using namespace std;

typedef long long mlong;
int main(int argc, char **argv) {
    int T;
    cin >> T;
    cout.precision(19);
    for (int i = 0; i < T; i ++) {
	mlong K, C, S;
	cin >> K >> C >> S;
	
	cout << "Case #" << i + 1 << ":";
	for (mlong i = 0; i < K; i ++) {
	    cout << " " << i * pow(K, C - 1) + 1; 
	}
	cout << endl;
    }
}
