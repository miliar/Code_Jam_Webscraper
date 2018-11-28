#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <math.h>
#include <hash_set>
#include <algorithm>
#include <time.h>
#include <map>
#include <set>
#include <stack>
 
#define _USE_MATH_DEFINES
using namespace std;


int main(){
	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for(int t=0; t<T; ++t){
		int a,b,k;
		cin >> a >> b >> k;
		int res=0;
		for(int i=0; i<a; ++i){
			for(int j=0; j<b; ++j){
				int c = i&j;
				if(c < k)res++;
			}
		}
		cout << "Case #" << t+1 << ": " << res << endl;
	}

    return 0;
}