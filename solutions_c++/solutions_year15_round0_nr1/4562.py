//
//  15a2.cpp
//  
//
//  Created by Ritish Goyal on 11/04/15.
//
//

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

#define rep(i, n) for(int i=0; i<n; i++)

int main() {
    int test; cin>> test;
    rep(z, test) {
        int s, ans = 0, sum = 0;
	string str;
	cin>>s>>str;
        int a[s+1];
        rep(i, s+1) {
	  a[i] = str[i] - '0';
        }
        rep(i, s+1) {
            if(sum < i) {
                ans += (i - sum);
                sum += (i - sum);
            }
            sum += a[i];
        }
        printf("Case #%d: %d\n", z+1, ans);
    }
}
