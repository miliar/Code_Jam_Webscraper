#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

int main(){
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
    
	int T;
	cin >> T;
    
	for (int t = 0; t < T; t++){
		int x, y;
        cin >> x >> y;
        
		cout << "Case #" << t + 1 << ": ";
		
        for (int i = 0; i < abs(x); i++)
            if (x > 0)
                cout << "WE";
            else
                cout << "EW";
        for (int i = 0; i < abs(y); i++)
            if (y > 0)
                cout << "SN";
            else
                cout << "NS";
        
        cout << endl;
	}
}
