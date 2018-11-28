#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	size_t a, b, k, T, result,i, j, l, tmp;
	cin >> T;
	for (i =0; i < T; i++){
	//Readkflop
		cin >> a>> b>> k;
		if (a < b)swap(a, b);
		result = a + b - 1;
		//joiwopo
		for (j = 1; j < a; ++j)
			for (l = 1; l < b; ++l){
				if ((j & l) < k)result++;
				//sdhsdkkldskls
			}
		cout << "Case #"<<i+1 << ": " << result << endl;
	}
	return 0;
}