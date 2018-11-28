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

unsigned long long solve(const string &s, unsigned mx) {
	//cout << "S: " << s << " " << mx << endl;
	unsigned long long somaExtras = 0;
	unsigned long long somaAteAgora = 0;

	somaAteAgora += s[0]-'0';
	for(unsigned i=1;i<=mx;i++) {
		int np = s[i]-'0';
		if (somaAteAgora < i) {
			somaExtras += i-somaAteAgora;
			somaAteAgora += i-somaAteAgora  + np;
		} else 
			somaAteAgora += np;
	}
	return somaExtras;
}

int main() {
     int nt;
     cin >> nt;
     for(int i=0;i<nt;i++) {
     	unsigned a;
     	string s;
     	cin >> a >> s;
     	cout << "Case #" << i+1 << ": " << solve(s,a) << "\n";
     }
   
	return 0;   
}
