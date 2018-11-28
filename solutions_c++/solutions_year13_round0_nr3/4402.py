#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.o", "w+", stdout);

	int t;
	int a;
	int b;
	int tempNum;
	int naf[5] = {1,4,9,121,484};
    cin >> t;
	
	for(int ti = 0; ti < t; ti++){
		cout << "Case #" << (ti+1) << ": ";
		cin >> a;
		cin >> b;
		tempNum = 0;
		for(int ni = 0; ni < 5; ni++){
			if((naf[ni] >= a) && (naf[ni] <= b)){
				tempNum++;
			}
		}
		cout << tempNum << endl;
	}
}