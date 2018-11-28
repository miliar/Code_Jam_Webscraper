#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <map>
#include <stack>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

ifstream fin("A.in");
ofstream fout("B.out");

int T, A, B, X, K;
long int ways;

int main(){
	int i, j, k , l;

	cin >> T;
	for (i = 1; i <= T; i++){
		cin >> A >> B >> K;
		ways = 0;
		for (k = 0; k < A; k++){
			for (l = 0; l < B; l++){
				if ((l&k) < K){
					ways++;
				}
			}
		}
		cout << "Case  #" << i << ": " << ways << '\n';
	}

	return 0;
}