#include <iostream>
#include <sstream>
#include <numeric>
#include <set>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <math.h>
#include <stdlib.h>
#include <limits.h>
#include <strings.h>

using namespace std;

int main(){
	int tests;
	cin >> tests;
	for (int t = 0; t < tests; t++){
		int N, C;//capacity
		int files[701];
		cin >> N >> C;
		bzero(files, sizeof(files));
		for (int i = 0; i < N; i++){
			int f;
			cin >> f;
			files[f]++;
		}
		int usedFiles = 0;
		int current = 700;
		int usedDisks = 0;
		while(usedFiles != N){
			while(files[current] == 0){
				current--;
			}
			files[current]--;
			usedDisks++;
			int current2 = C - current;
			while((current2 >= 0) && (files[current2] == 0)){
				current2--;
			}
			if (current2 >= 0){
				usedFiles++;
				files[current2]--;
			}
			usedFiles++;
		}
		cout << "Case #" << (t+1) << ": " << usedDisks << endl;
	}
}
