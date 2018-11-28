#include <iostream>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <set>

#define f(x, y) for(int x = 0; x < y; ++x)

using namespace std;

string getLast(unsigned int n);

int main(){

	unsigned int T, N, nextN;

	cin >> T;

	f(x, T){
		cin >> N;
		
		cout << "Case #" << (x +  1) << ": " << (N == 0 ? "INSOMNIA" : getLast(N)) << endl;
	}

	return 0;
}

string getLast(unsigned int n){
	unsigned int last = 0;
	set<int> found;
	string number;

	while(found.size() < 10){
		last += n;
		number = to_string(last);
		f(x, number.size()){
			found.insert(number[x] - '0');
		}
	}

	return to_string(last);
}
