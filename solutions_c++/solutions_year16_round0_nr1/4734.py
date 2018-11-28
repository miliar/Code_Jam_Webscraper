#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <limits.h>
#include <map>
#define MX 1000002
#define MOD 100000001
#define BASE 5.0

#include <time.h>
#include <stdlib.h>
using namespace std;



int main(){
	ios_base::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif
    int digit[10];
    int t;
    unsigned long long n;
    cin >> t;
    for (int icase = 1; icase <= t; icase ++) {
    	cin >> n;
    	for (int i = 0; i<10; i++) digit[i] = 0;
    	unsigned long long curn = 0;
    	unsigned long long tempcurn;
    	int pass = 0;
    	bool check = true;
    	for (int i = 0; i<101 && check; i++) {
    		curn += n;
    		tempcurn = curn;
    		while (tempcurn > 0) {
    			if (digit[tempcurn%10] == 0){
	    			pass++;
	    			digit[tempcurn%10] = 1;
	    		}
    			tempcurn /= 10;
    		}
    		if (pass == 10) {
    			check = false;
    			cout << "Case #" << icase << ": " << curn << "\n";
    		}
    	}
    	if (check)
    		cout << "Case #" << icase << ": INSOMNIA\n";
    }
    return 0;
}