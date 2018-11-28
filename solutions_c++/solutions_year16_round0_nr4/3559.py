#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int
main(int argc, char** argv)
{
	int N, a, n=1;
	cin >> N;
	while(n <= N) {
		int K,C,S;
		cout << "Case #" << n << ": ";
		cin >> K >> C >> S;
		for (int i = 1; i <= S; i++) {
			cout << i << " ";	
		}
		cout << endl;
		n++;
	} 
	return 0;
}