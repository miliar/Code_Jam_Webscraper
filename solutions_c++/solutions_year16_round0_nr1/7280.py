#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <map>

#define sqr(a) (a) * (a)
#define NN 1001000

using namespace std;

int tt = 1, i, t, n;
int ans[NN];
bool used[11];

int calc(int n) {
	long long N = n;
	int counter = 0;
	bool ok = false;
    while (!ok) {
    	long long q = N;
    	while (q > 0) {
    		used[q % 10] = true;
    		q /= 10;
    	}
		ok = true;
    	for (i = 0; i < 10; i++)
    		if (!used[i]) {
    			ok = false;
    			break;
    		}
    	N += n;
    }        	
    for (int i = 0; i < 10; i++)
    	used[i] = false;
	return N - n;
}

void precount() {
	long long dv, j;
	for (int i = 1; i <= 1000000; i++) {
		/*dv = 1;
		j = i;
		while (j % 10 == 0) {
			j /= 10;
			dv *= 10;
		}
		*/
		ans[i] = calc(i);
	}
}

int main()  {

    #ifndef ONLINE_JUDGE
    freopen("a.in", "r" , stdin);
    freopen("a.out", "w", stdout);
    #endif

    cin >> t;

   	precount();

    while (t--) {
    	cin >> n;
    	if (n)
	    	cout << "Case #" << tt++ << ": " << ans[n] << endl;
		else
			cout << "Case #" << tt++ << ": " << "INSOMNIA" << endl;
    }
      

    return 0;
}