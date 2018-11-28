#include <iostream>
#include <string.h>
#include <bitset>
#include <vector>
#include <math.h>

using namespace std;


int main(void) {

	int t;
	cin >> t;
	int k;
	int c;
	int s;
	for(int i=0; i<t;i++) {

		cin >> k;
		cin >> c;
		cin >> s;
		cout << "Case #" << i+1 <<": ";
		for(int i=1;i<=k; i++) cout << i << " ";
		cout << endl;
	}

	return 0;
}
