#include <stdio.h>
#include <cstring>
#include <functional>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
#include <vector>
#include <stack>
#include <map>
#include <cmath>
#include <string>
using namespace std;

int main(){
	string inputValue;
	int cases;
	cin >> inputValue;
	cases = atoi(inputValue.c_str());
	int k = 1;

	while(cases--){
		int N = 0;
		int M = 0;
		cin >> inputValue;
		N = atoi(inputValue.c_str());
		cin >> inputValue;
		M = atoi(inputValue.c_str());

		vector<vector<int>> Matrix(N, vector<int>(M));
		vector<vector<bool>> C(N, vector<bool>(M, false));

		int i;
		int j;
		int p;
		for(i = 0; i < N; i++){
			for(j = 0; j < M; j++){
				cin >> inputValue;
				Matrix[i][j] = atoi(inputValue.c_str());
			}
		}

		bool consegueTotal = true;

		for(i = 0; i < N && consegueTotal; i++){
			for(j = 0; j < M && consegueTotal; j++){
				int p, l;
				int min = Matrix[i][j];
				bool consegueI = true;
				bool consegueJ = true;
				for(p = 0; p < N; p++){
					if(min < Matrix[p][j]){
						consegueI = false;
						break;
					}
				}
				if(consegueI == false){
					min = Matrix[i][j];
					for(l = 0; l < M; l++){
						if(min < Matrix[i][l]){
							consegueJ = false;
							break;
						}
					}
				}

				if(consegueI == false &&  consegueJ == false){
					consegueTotal = false;
				}
			}
		}

		if(consegueTotal){
			printf("Case #%d: YES\n", k);
		}else{
			printf("Case #%d: NO\n", k);
		}
		k++;
	}

	return 0;
}