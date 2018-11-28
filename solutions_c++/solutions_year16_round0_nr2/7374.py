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

#define N 1000

using namespace std;

int t, i, lp, l, r, counter;
string s;
int a[N];
int tt = 1;

void swapp(int l, int r) {
	int i;
	for (i = l; i <= r; i++)
		a[i] = (a[i] ^ 1);

}

int main()  {

    #ifndef ONLINE_JUDGE
    freopen("a.in", "r" , stdin);
    freopen("a.out", "w", stdout);
    #endif

    cin >> t;
    while (t--) {
    	cin >> s;
    	for (i = 0; i < s.length(); i++)
    		a[i + 1] = (s[i] == '+' ? 1 : 0);

		l = 1;
		r = s.length();
		while (l <= r) {	
			while (a[r])
				r--;          
			
			if (a[l]) {
				lp = l;
				while (a[l])
					l++;
				swapp(lp, l - 1);
				l = lp;
				counter++;
			} else {
				swapp(l, r);
				counter++;
			}
		}
		cout << "Case #" <<tt++ <<": " << counter  - 1 << endl;
		counter = 0;
    }
          
    return 0;
}