#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

bool digits[10];

bool done() {
	FOR (i, 10)
		if (!digits[i])
			return false;
	return true;
}

void add(int num) {
	while (num) {
		digits[num % 10] = true;
		num /= 10;
	}
}

int main(){
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    cout << "Case #" << (test + 1) << ": ";
    int n;
    cin >> n;
    if (!n)
    	cout << "INSOMNIA";
    else {
    	SET(digits, 0);
    	int val = n;
    	while (!done()) {
    		add(val);
    		val += n;
    	}
    	val -= n;
    	cout << val;
    }
    cout << "\n";
  }
  return 0;
}
