#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

int main(){
	int T; cin >> T;
	for(int t = 1; t <= T; t++){
		double C, F, X;
		cin >> C >> F >> X;
		double acc = 0;
		double last = X / 2.0;
		int i = 0;
		while(1){
			acc += C/(2.0 + i*F);
			double x = X / (2.0 + (i+1)*F);
			if(acc + x > last) break;
			last = acc + x;
			i++;
		}
		cout << "Case #" << t << ": ";
		printf("%.7lf\n", last);
	}
	return 0;
}