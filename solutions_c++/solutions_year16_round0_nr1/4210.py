#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <climits>
#include <stdlib.h>
#include <vector>
#include <string.h>
#include <stack>
#include <algorithm>
#include <queue>
#include <stdint.h>
using namespace std;
int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		int N;
		cin >> N;
		printf("Case #%d: ",t);
		if(N==0){
			cout << "INSOMNIA\n";
			continue;
		}
		int seen = 0;
		int count = 1;
		stringstream ss;
		string s;
		while(true){
			if(seen == 1023){
				cout << N*(count-1);
				break;
			}
			ss << count*N;
			string s = ss.str();
			for(int i = 0; i < s.size();i++){
				int v = (int) s[i] - '0';
				seen |= 1<<v;
			}
			count++;
		}
		cout << endl;
	}
	return 0;
}