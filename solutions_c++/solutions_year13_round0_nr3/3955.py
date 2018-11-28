/*
LANG: C++
ID: 2012agura1
*/

#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <ctime>

using namespace std;
FILE *fin  = fopen("c.in",  "r");
FILE *fout = fopen("gcj-c.out", "w");

bool pal(long long i) {
    long long digit, rev = 0, num = i;
    do {
        digit = num % 10;
        rev = (rev * 10) + digit;
        num = num / 10;
    } while (num != 0);
    //cout << i << " " << rev << endl;
    return (i == rev);
}

int main () {
	int T;
    long long A,B,a,b,n;
    
	fscanf(fin, "%d", &T);

    for(int t = 1; t <= T; t++) {
        fscanf(fin, "%lld %lld", &A, &B);
        n = 0;
        a = (long long)sqrt(A);
        if(a*a < A) a++;
        b = (long long)sqrt(B);
        //cout << "a b: " << a << " " << b << endl;

        for(long long i = a; i <= b; i++) {
            if(pal(i) && pal(i * i)) {
                n++;
                //cout << i << " " << (i * i) << endl;
            }
        }

        fprintf(fout, "%s%d%s%lld\n", "Case #", t, ": ", n);
    }

	return 0;
}


