#include <fstream>
#include <string>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> digits;

bool areAllDigitsSeen(int num)
{
	for(int n = num; n > 0; n = n /10) {
		digits.erase(remove(digits.begin(), digits.end(), n%10), digits.end());
	}
	
	return digits.empty();
}

int getSleepyNumber(int N)
{
	if (0 == N){
		return 0;
	}

	int i = 2;
	int sleepyNumber = N;
	while(!areAllDigitsSeen(sleepyNumber)) {
		sleepyNumber = i++ * N;
	}
	
	return sleepyNumber;
}

void resetDigitsSeen() {
	digits.clear();
	for (int i = 0; i <= 9; ++i){
		digits.push_back(i);
	}
}

int main()
{
	ofstream myfile;
	myfile.open("output.txt");
	ifstream file("A-large.in");
    string str;
    
    if (file) {
        getline(file, str);
        int T = atoi(str.c_str());
		
		for (int t = 1; t <= T; ++t) {
			resetDigitsSeen();
			
			getline(file, str);
			int N = atoi(str.c_str());
			int sleepyNumber = getSleepyNumber(N);
			
			if (0 == sleepyNumber) {
				myfile << "Case #" << t << ": INSOMNIA" << endl;
			} else {
				myfile << "Case #" << t << ": " << sleepyNumber << endl;
			}
		}
    }
	myfile.close();
    return 0;
}