    #include <iostream>
    #include <iomanip>
    #include <math.h>
    #include<algorithm>
    #include<string>
    #include <vector>
#include <fstream>

using namespace std;

long long pww(long long n, int deg) {
		long long ans = 1;
		while(deg) {
			if (deg % 2 == 0) {
				n *= n;
				deg /= 2;
			}
			else {
				deg--;
				ans *= n;
			}
		}
		return ans;
	}

	long long gcd (long long a, long long b) {
    if (b == 0)
        return a;
    return gcd(b, a%b);
}

	int der_otr[4*1000000+3];

	void build_d(int a[], int v, int l, int r) {
		if (l == r) 
			der_otr[v] = a[l];
		else {
			int tmp = (l + r)/2;
			build_d(a, 2*v, l, tmp);
			build_d(a, 2*v + 1, tmp + 1, r);
			der_otr[v] = der_otr[v*2] + der_otr[v*2 + 1];
		}
	}
	
	int sum (int v, int l, int r, int zapr_l, int zapr_r) {
		if (zapr_l > zapr_r)
			return 0;
		if (l == zapr_l && r == zapr_r)
			return der_otr[v];
		else {
			int tmp = (l + r)/2;
			return sum (2*v, l, tmp, zapr_l, min(zapr_r,tmp)) + 
				sum (2*v + 1, tmp + 1, r, max(zapr_l,tmp + 1 ), zapr_r);
		}
	}
	void upd (int v, int l, int r, int index, int new_value) {
		if (l == r)
			der_otr[v] = new_value;
		else {
			int tmp = (l + r)/2;
			if (index <= tmp)
				upd (2*v, l, tmp, index, new_value);
			else
				upd (2*v + 1, tmp+1, r, index, new_value);
			der_otr[v] = der_otr[2*v] + der_otr[2*v + 1];
		}
	}
	int n;
	
int main()
{
	
 freopen("A-small-attempt3.txt", "r", stdin);
 freopen("A-small-attempt3.out", "w", stdout);
 //freopen("INPUT.txt", "r", stdin);
 
	cin >> n;
	int m1[4], m2[4]; string t;
	int u = 0; string s, sneed1, sneed2;

	for (int i = 0; i < n; i++) {
		int j = 0;
		cin >> u;
		while (j < 4){
			if (u == (j + 1)) {
				cin >> m1[0] >> m1[1] >> m1[2] >> m1[3] ;
				j++;
			}
			if (j == 4)
				break;
			//cin >> s;
			int suka = 0;
			while (suka < 4) {
				cin >> t;
				suka++;
			}
			j++;
		}
		j = 0;
		cin >> u;
		while (j < 4){
			if (u == (j + 1)) {
				cin >> m2[0] >> m2[1] >> m2[2] >> m2[3] ;
				j++;
			}
			if (j == 4)
				break;
			//cin >> s;
			int suka = 0;
			while (suka < 4) {
				cin >> t;
				suka++;
			}
			j++;
		}
		int ans = 0, up;
		for (int v = 0; v < 4; v++)
			for (int k = 0; k < 4; k++) 
				if (m1[v] == m2[k]) {
					ans++;
					up = m1[v];
				}
		cout << "Case #" << i + 1 << ": ";
		if (ans == 1)
			cout <<  up;
		else
			if (ans == 0)
				cout << "Volunteer cheated!";
			else
				cout << "Bad magician!";
		cout << "\n";
	}	

 return 0;
}	