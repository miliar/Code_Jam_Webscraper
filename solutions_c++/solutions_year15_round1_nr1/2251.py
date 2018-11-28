
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>

using namespace std;


int countMethod1(vector<int> v) {
    int total = 0;

    for (int i = 1; i < v.size(); i++) {
    	if (v[i-1] > v[i]) {
    	    total += v[i-1] - v[i];
    	}
    }

    return total;
}

int countMethod2(vector<int> v, int rate) {
    int total = 0;
    
    for (int i = 1; i < v.size(); i++) {
        
        total += (v[i-1] >= rate) ? rate : v[i-1];
    }

    return total;
}

int countRate(vector<int> v) {
    int rate = 0;
    
    for (int i = 1; i < v.size(); i++) {
        rate = max(rate, v[i-1] - v[i]);
    }
    
    return rate;
}

int main(void) {
    int t, n, x;
    vector<int> v;
    
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    cin >> t;
    
    for (int test = 1; test <= t; test++) {
        cin >> n;
        
        for (int i = 0; i < n; i++) {
            cin >> x;
            v.push_back(x);
        }
        
        cout << "Case #" << test << ": " << countMethod1(v) << " " << countMethod2(v, countRate(v)) << endl;
        v.clear();
    }
    
    return 0;
}
