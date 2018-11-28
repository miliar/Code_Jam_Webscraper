/*
 * Created on: 2015-04-12 01:43
 * Created by: suren
 *
 * Distributed under beerware licence.
 */

#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <algorithm>
#include <cstdlib>
#include <cmath>

using namespace std;

typedef vector<int> vi;
typedef vector< vi > vvi;
typedef pair<int, int> ii;
typedef vector< ii > vii;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()

int main() {
    int t;
    cin >> t;
    for(int cas = 1; cas <= t; cas++){
        int x, r, c;
        cin >> x >> r >> c;
        int res;
        if(x == 1) {
            res = 1;
        }
        else if(x == 2) {
            if(r%2 && c%2) {
                res = 0;
            }
            else {
                res = 1;
            }
        }
        else if(x == 3) {
            if((c*r)%3 == 0 && c > 1 && r > 1) {
                res = 1;
            }
            else {
                res = 0;
            }
        }
        else {
            if(c + r >= 7) {
                res = 1;
            }
            else {
                res = 0;
            }
        }

        if(res) {
            printf("Case #%d: GABRIEL\n", cas);
        }
        else {
            printf("Case #%d: RICHARD\n", cas);
        }
    }

    return 0;
} 
