#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>
#include <math.h> 
#include <assert.h>
#include <utility>


using namespace std;

#define ll long long
#define ui unsigned int
#define debug(a) cout << #a << ": " << a << endl;
#define debugVector(a) cout << #a << ": "; for(ui i; i < a.size(); i++) {cout << a[i] << " ";} cout << endl;
#define pb(a) push_back(a)
#define case(i) fOut << "Case #" << (i) << ": "; cout << "Case #" << (i) << endl;

ui solve(ui smax, string s) {
	//shyness, number
	vector<int>  shiness;
	shiness.resize(smax+1);

	for (ui i = 0; i < smax+1; i++) {
		shiness[i] = s[i] - '0';
	}

	int count = shiness[0];
	int result = 0;
	for (int i = 1; i < smax+1; i++) {
		int toAdd = max(0, i - count);
		count += shiness[i] + toAdd;
		result += toAdd;
	}

	return result;
}


int main()
{
    ui tests; cin >> tests;
    ui smax;
    string s;
    for (ui t = 0; t < tests; t++) {
    	cin >> smax;
    	cin >> s;

    	cout << "Case #" << (t+1) << ": " << solve(smax, s) << endl;


    }

    
 

}
