#include <fstream>
#include <string>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

int getMinFlips(string pancakes) {
	if (pancakes.empty() || all_of(pancakes.begin(), pancakes.end(), [](char i){return i == '+';})) {
		return 0;
	}
	
	if(all_of(pancakes.begin(), pancakes.end(), [](char i){return i == '-';})) {
		return 1;
	}
	std::size_t found = pancakes.find_first_not_of(pancakes[0]);
	if (found != std::string::npos) {
		pancakes.replace(pancakes.begin(), pancakes.begin()+found, found, pancakes[found]);
	}
	
	return getMinFlips(pancakes) + 1;
}
int main()
{
	ofstream myfile;
	myfile.open("output.txt");
	ifstream file("B-large.in");
    string str;
    
    if (file) {
        getline(file, str);
        int T = atoi(str.c_str());

		for (int t = 1; t <= T; ++t) {	
			getline(file, str);
			if (str.back() != '+' && str.back() != '-')
				str.pop_back();

			int minFlips = getMinFlips(str);
			myfile << "Case #" << t << ": " << minFlips << endl;
		}
    }
	myfile.close();
    return 0;
}