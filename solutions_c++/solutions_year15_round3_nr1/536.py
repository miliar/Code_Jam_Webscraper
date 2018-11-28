#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <cstdio>
#include <ctime>
#include <climits>


using namespace std;


int main(){
	freopen("/Users/Arseniy/All/A/input.txt", "r", stdin);
    freopen("/Users/Arseniy/All/A/output.txt", "w", stdout);
    int r, c, w, t;
    cin >> t;
    for (int o=0;o<t;o++){
    	cout << "Case #" << o+1 << ": ";
    	cin >> r >> c >> w;
    	int ans = 0;
    	if (w == 1){
    		cout << r*c << endl;
    		continue;
    	}
    	int p = 0;
    	if ((c % w) != 0)
    		p++;
    	ans = r*(c/w) + p + w-1;
    	cout << ans << endl;
    }
	return 0;
}