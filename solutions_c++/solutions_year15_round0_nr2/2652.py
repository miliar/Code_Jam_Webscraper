#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <cctype>
#include <iomanip>
#include <algorithm>
#include <sstream>

#define f(i,n) for(int i=0;i<n;i++)
using namespace std;

unsigned long long mi(const vector<int> &v,int t,int n) {
	unsigned long long numStops = 0;
	for(int i=0;i<n;i++) {
		if (v[i] > t) {
			numStops += (v[i]+t-1)/t  - 1;
		}
	}

	return t+ numStops;
}


int solve(const vector<int> &v,int n) {
	unsigned long long m = 1999999999; m*=100000;
	int mx = 0;
	for(int i=0;i<n;i++) mx = max(v[i],mx);
	for(int i=1;i<=mx;i++) {
		m = min(m,mi(v,i,n));
	}
	return m;
}

int main() {
    int nt ;
    cin >> nt;

    for(int i=1;i<=nt;i++) {
    	
    	int n;
    	cin >> n;
    	vector<int> v(n);
    	f(j,n) cin >> v[j];
    	cout << "Case #" << i << ": " << solve(v,n) << "\n";
    }
   
	return 0;   
}
