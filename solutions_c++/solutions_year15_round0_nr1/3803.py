#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <stack>
#include <utility>
#include <fstream>

using namespace std;

fstream fin;
#define cin fin

int main(){
	int T;
	cin.open("A-large.in");
	
	cin >> T;

	string ss;
	int smax = 0;

	for(int t = 1; t <= T; t++){
		cin >> smax >> ss;
		int res = 0, ans = 0;
		for(int i = 0; i < (int) ss.size(); i++){
			res += ss[i] - '0';
			if(res == 0){
				ans++;
				res++;
			}
			res--;
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}