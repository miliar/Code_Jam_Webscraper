#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <math.h>
using namespace std;

void incr(bool arr[], int n);
long getdec(bool arr[], int n, int base);
bool isValid(bool arr[], int n, int divi[]);
int getdiv(long n);
int main() {
	FILE *fin = freopen("C-small.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("C-small.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": " << endl;
		int n;
		cin >> n;
		int j;
		cin >> j;
		bool num[n];
		num[0] = 1;
		for (int i = 1; i < (n-1); i++) {
		    num[i] = 0;
		}
		num[n-1] = 1;
		
		int divi[9];
		for (int i = 0; i < j; i++) {
		    while (true) {
	            if (isValid(num, n, divi)) {
	                break;
	            }
	            incr(num, n);
		    }
		    for (int l = 0; l < n; l++) {
		        cout << num[l];
		    }
		    for (int l = 0; l < 9; l++) {
		        cout << " " << divi[l];
		    }
		    cout << endl;
		    incr(num, n);
		}
		
	}
	exit(0);
}

void incr(bool arr[], int n) {
    for (int i = n-2; i > 0; i--) {
        if (arr[i]) {
            arr[i] = !arr[i];
        }
        else {
            arr[i] = 1;
            return;
        }
    }
    return;
}

long getdec(bool arr[], int n, int base) {
    long ret = 0;
    long powow = 1;
    for (int i = n-1; i >= 0 ; i--) {
        ret += (arr[i]*powow);
        powow *= base;
    }
    return ret;
}

bool isValid(bool arr[], int n, int divi[]) {
    for (int i = 2; i <= 10; i++) {
        long res = getdec(arr, n, i);
        int rem = getdiv(res);
        // cout << rem << "/" << res << " ";
        if (rem) {
            divi[i-2] = rem;
        }
        else {
            return 0;
        }
    }
    return 1;
}

int getdiv(long n) {
    int till = ceil(sqrt((double)n));
    for (int i = 2; i <= till; i++) {
        if (n%i == 0) {
            return i;
        }
    }
    return 0;
}
