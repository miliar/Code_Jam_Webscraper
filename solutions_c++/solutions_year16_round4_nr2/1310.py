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
#include <strings.h>
#include <limits.h>
#include <stdlib.h>
#include <float.h>
#include <strings.h>
#include <string.h>
#include <iomanip>
using namespace std;

#define isOn(S, j) (S & (1ll << j))

int main(){
	int tests;
	cin >> tests;
	for (int t = 0; t < tests; t++){
		cout << "Case #" << (t+1) << ": ";
		int N, K;
		cin >> N >> K;
		double pi[N+1];
		for (int i = 1; i <= N; i++){
			cin >> pi[i];
		}
		double solution = 0;
		for (int opt = 0; opt < (1 << N); opt++){
			double p2i[N+1];
			int count = 0;
			for (int i = 0; i < N; i++){
				if (isOn(opt, i)){
					count++;
					p2i[count] = pi[i+1];
				}
			}
			if (count == K){
				double prob[K+1][K+1];//With a people reach b
				for (int i = 0; i <= K; i++){
					prob[0][i] = 0;
				}
				prob[0][0] = 1;
				for (int i = 1; i <= K; i++){//Current person
					for (int j = 0; j <= K; j++){//Value to reach
						double prob1 = 0;
						if (j != 0){
							prob1 = p2i[i] * prob[i-1][j-1];
						}
						double prob2 = (1 - p2i[i]) * prob[i-1][j];
						prob[i][j] = prob1 + prob2;
					}
				}
				solution = max(solution, prob[K][K/2]);
			}
		}
		cout << fixed << setprecision(10) << solution << endl;
	}
}
