#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
using namespace std;

int lawn[100][100];
bool covered[100][100];

int main () {
	
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int T;
    cin >> T;
    int a, b;
    for (int t=1; t<=T; t++) {
    	cin >> a >> b;
    	int ans = 0;
    	if (a == 1) ans ++;
    	if (a <= 4 && b >= 4) ans++;
    	if (a <= 9 && b >= 9) ans++;
    	if (a <= 121 && b >= 121) ans++;
    	if (a <= 484 && b >= 484) ans++;
    	printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}