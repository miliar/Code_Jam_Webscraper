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
	int m, n;

	double C, f, x, kor1,kor2, D, a,b,c;
int main()
{
	
 freopen("B-large.txt", "r", stdin);
 freopen("B-large.out", "w", stdout);
 //freopen("INPUT.txt", "r", stdin);
	
	cin >> n;
	double time = 0, ahyennayaPeremennaya = 0; int in = 0;
	for (int i = 0; i < n; i++) {	
		cin >> c >> f >> x;
		while(true){
			ahyennayaPeremennaya += c / (2 + in * f); 
			time = ahyennayaPeremennaya + x / (2 + (in + 1) * f);
			if (time < (ahyennayaPeremennaya + c / (2 + (in + 1) * f) + x / (2 + (in + 2) * f)))
				break;
			else {}
			in++;
		}
		cout << "Case #" << i + 1 << ": ";
		if (x / 2 < time)
				printf("%.6f\n", x / 2);
		else printf("%.6f\n", time);
		time = 0, ahyennayaPeremennaya = 0;
		in = 0;
	}
	//cout << kor1 << " " << kor2 << endl;
	//cout << m;

 return 0;
}	