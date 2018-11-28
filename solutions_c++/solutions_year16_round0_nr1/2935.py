#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
using namespace std;

int main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		long long n;
		cin >> n;
		if (n == 0) {
		    cout << "INSOMNIA" << endl;
		}
		else {
		    long long mult = 1;
		    bool check[10];
    		for (int i = 0; i < 10; i++) {
    		    check[i] = 0;
    		}
		    bool awake = 0;
		    long long m;
		    do {
		        awake = 0;
		        m = n*mult;
		        mult++;
		        do {
		            check[m%10] = 1;
		            m /= 10;
		        } while (m > 0);
		        for (int i = 0; i < 10; i++) {
		            if (check[i] == 0) {
		              //  cout << "HERE" << endl;
		                awake = 1;
		                break;
		            }
		        }
		    } while (awake);
		    cout << n*(mult-1) << endl;
		}
	}
	exit(0);
}