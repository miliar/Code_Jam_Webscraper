#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>

using namespace std;

int main(){

	int n, sz, friends, cont;
	cin >> n;
	string plateia;

	for (int i = 0; i < n; i ++){
		cin >> sz >> plateia;
		cont = plateia[0]-'0';
		friends = 0; 
		for (int j = 1; j < sz+1; j ++){
			if (cont >= j || plateia[j] == 0) cont += (plateia[j]-'0');
			else{
			   friends += j - cont;
			   cont += j - cont + plateia[j] - '0';
			}
		}
		cout << "Case #" << i+1 << ": " << friends << endl;
	}

	return 0;
}
