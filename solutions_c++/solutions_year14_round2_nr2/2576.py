// Google Code Jam 2014
// Patrick Granite
// Problem A

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

unsigned int solve(void){
	unsigned int count = 0;
	unsigned int A, B, K;
	unsigned int ticket; 
	string temp;
	getline(std::cin, temp);
	istringstream(temp) >> A >> B >> K;

	for (unsigned int o = 0; o < A; o++){
		for (unsigned  int n = 0; n < B; n++){
			ticket = o&n;
			if (ticket < K)
				count++;
		}
	}
	return count;
}

void main(void)
{
	int t, T;
	unsigned int res;
	string temp; 

	getline(std::cin, temp);
	istringstream(temp) >> T;
	
	for (t = 0; t < T; t++){
		res = solve();
		cout << "Case #" << t + 1 << ": " << res<< endl;
	}

}

