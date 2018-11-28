#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <cmath>
#include <iostream>
#include <cstdio>

#define swap(type, x, y) {type t = x; x = y; y = t}

using namespace std;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);


	int T, case_no = 0;
	cin>>T;
	while(T--){
		case_no++;
		double C, F, X;
		cin>>C>>F>>X;

		double prev = -1.0;

		for(int i = 0; 1; i++){
			double incr = 2.0;
			double time_spent = 0;
			for(int j = 1; j <= i; j++){
				time_spent += C/incr;
				incr += F;
			}

			time_spent += X/incr;

			if(prev != -1.0 && time_spent > prev)break;
			else prev = time_spent;
		}

		printf("Case #%d: %0.7lf\n", case_no, prev );
	}

	return 0;
}