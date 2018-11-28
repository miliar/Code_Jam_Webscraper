#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <fstream>
#include <queue>
#include <math.h>
#include <set>
#include <stdlib.h>
#include <time.h>
#include <list>

#define For(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n)  For(i,0,n)

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))
#define check(a) rep(i, a.size()) cout << a[i] << endl
#define SORT(c) sort((c).begin(),(c).end())
#define ll long long
#define vi vector<int>
#define all(it,a) for(auto it = a.begin(); it!=a.end(); it++)
using namespace std;


int main(void) {
	int iti, k, j;
	cin >> iti >> k >> j;
	cout << "Case #1:" << endl;
	int res = 0;
	string tmpl = "1";
	rep(i, k - 2) {
		tmpl += '0';
	}
	tmpl += '1';

	int count = 0;

	for (int l = 0; l < (2 << (k - 3)); l++) {
		string str = tmpl;
		int piv = k - 2;
		int temp = l;
		while (temp != 0) {
			if (temp % 2 == 1) {
				str[piv] = '1';
			}
			temp >>= 1;
			piv--;
		}

		bool ok = true;

		int resarray[9];
		//cout << endl << str << endl;
		For(i, 2, 11) {

			long long targ = 0;
			for (int m = 0; m < str.length(); m++) {
				targ *= i;
				targ += (str[m] - '0');
			}


			bool isPrime = true;
			long long m = sqrt(targ);
			int waru = 2;
			for (; waru <= m; waru++) {
				if (targ % waru == 0) {
					isPrime = false;
					break;
				}
			}

			//cout << targ << " " << waru <<" "<< isPrime << endl;
			resarray[i - 2] = waru;
			if (isPrime) {
				ok = false;
				break;
			}
		}
		if (ok) {
			cout << str << " ";
			rep(i, 9) {
				if (i != 0)
					cout << " ";
				cout << resarray[i];
			}
			cout << endl;
			count++;
			if (count >= j)
				break;
		}

	}




	return 0;
}
