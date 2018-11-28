/*
 * A3.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: Darin
 */

#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

bool check(int x){
	string s1 = "";
	string s2 = "";
    while (x > 0){
    	s1 = s1 + (char)(x % 10);
    	s2 = (char) (x % 10) + s2;
    	x = x / 10;
    }
    return (s1 == s2);
}
int main(){
	//freopen("t.in","r",stdin);
	//freopen("t.out","w",stdout);
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++){
		int A, B;
		cin >> A >> B;
		int ans = 0;
		for (int i = 1; i <= B; i++){

			int x = i*i;
			if (x < A) continue;
			if (x > B) break;
			if (!check(i)) continue;
			if (check(x)) {
				ans++;
			}
		}
		cout << "Case #" << test << ": " << ans << endl;
	}
}
