/*
ID: alexlin1
PROG: cookieclicker
LANG: C++
*/

#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <iomanip>
using namespace std;



double solve() {
    double cost,incr,win, currtime = 0.0;
    double speed = 2.0;
    cin >> cost >> incr >> win;
    
    while (win / speed > cost / speed + win / (speed + incr)){
        currtime += cost / speed; speed += incr;
    }
    
    return currtime += win / speed;
}

int main() {
	if (fopen("cookieclicker.in","r")) {
		freopen("cookieclicker.in","r",stdin);
		freopen("cookieclicker.out","w",stdout);
	}
	int N;
    cin >> N;
    cout << fixed << setprecision(7);
    double a;
    for (int i=0;i<N;i++){
        a = solve();
        cout << "Case #" << i+1 << ": " << a << "\n";
    }
}