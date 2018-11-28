#include <iostream>
#include <stdlib.h>
#include <string>
#include <math.h>
using namespace std;

int main(){
	int cases;
	cin >> cases;
	for (int t=1; t <= cases; t++){
		int A,B,K, counter=0;
		cin >> A >> B >> K;
		for (int i=0; i < A; i++){
			for (int j=0; j < B; j++){
				if ((i&j) < K){
					counter++;
				}
			}
		}
		cout << "Case #" << t << ": " << counter << endl;
	}
	return 0;
}
