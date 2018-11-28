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
#include <cmath>
using namespace std;

int main(){
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w+", stdout);
	int t;
    cin >> t;

	int A,B,K;

	for(int ti = 0; ti < t; ti++){
		cout << "Case #" << (ti+1) << ": ";
		cin >> A >> B >> K;
		int count = 0;
		for(int i = 0; i < A; i++){
			for(int j = 0; j < B; j++){
				if((i&j) < K){
					count++;
				}
			}
		}
		cout<<count;
		cout << endl;

	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}