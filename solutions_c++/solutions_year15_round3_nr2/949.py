#include <stdio.h>
#include <string.h>
#include <queue>
#include <map>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector <string> v;
string k, p;
int n, s, l, mx;
double nom[110], don;


int cnt (string a){
	int ret = 0;
	for (int i=0;i<=s-l;i++){
		if (a.substr(i, l) == p)
			ret++;
	}
	return ret;
}

void sol (string w){
	if (w.size() == (size_t)s){
		int c = cnt(w);
		mx = max (mx, c);
		nom[c] += 1.000;
		don += 1.000;
		return;
	}

	for (int i=0;i<n;i++)
		sol (w+k[i]);

	return;
}


int main (){

	freopen ("b-small.in", "r", stdin);
	freopen ("b-small.out","w",stdout);

	int t;
	scanf ("%d", &t);

	for (int tc = 1; tc <= t; tc++){
	
		scanf ("%d %d %d", &n, &l, &s);

		cin >> k >> p;

		don = 0;
		mx = 0;
		for (int i=0;i<100;i++)
			nom[i] = 0;
		sol ("");

		double e = 0;
		for (int i=1;i<=s-l+1;i++){
			//cout << nom[i] << " " << don << endl;
			e += ((double)(i)) * (nom[i]/don);
		}
		
		//cout << mx << " " << e << endl;
		
		double ret = (double)(mx) - e + 1e-9;

		printf ("Case #%d: %.8f\n", tc, ret);

	}


	return 0;

}
