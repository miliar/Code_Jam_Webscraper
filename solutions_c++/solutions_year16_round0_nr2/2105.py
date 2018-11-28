#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <fstream>
#include <string>
#include <cstdlib>
//#include <stack>
#include <queue>

const std::string inputFile = "B-large.in";
const std::string outputFile = "B.out";

using namespace std;

int main() {
	fstream f;
	f.open(inputFile.data());

	ofstream out(outputFile.data());

	int t;
	f >> t;
	cout << t;
	for(int i=1; i<=t; i++) {
		out << "Case #" << i << ": ";
		int result = 0;
		string cur;
		f >> cur;
		f.ignore();
		cout << cur << endl;
		vector<bool> stack;
		for(int j=0; j<cur.length(); j++) {
			if(cur[j] == '+') stack.push_back(true);
			else stack.push_back(false);
		}
		std::reverse(stack.begin(), stack.end());
		for(int j=0; j<stack.size(); j++) {
			cout << stack[j] << " ";
		}

		while(find(stack.begin(), stack.end(), false) != stack.end()) {
			cout << "debug" << endl;
			for(int j=0; j<stack.size(); j++) {
				cout << stack[j] << " ";
			}
			result++;
			int index = stack.size()-1;
			while(*(stack.begin()+index)) {
				index--;
			}
			if(index == stack.size()-1) {
				cout << "ha" << endl;
				index = 0;
				while(*(stack.begin()+index)) {
					index++;
				}
			}
			else{
				index++;
			}
			cout << "eh " << index << endl;
			//do maneuver
			std::reverse(stack.begin()+index, stack.end());
			while(stack.begin()+index != stack.end()) {
				stack[index] = !stack[index];
				index++;
			}
			cout << "ah" << endl;

			/*
			deque<bool> temp;
			while(find(stack.begin(), stack.end(), false) != stack.end()) {
				temp.push_back(!stack.back());
				stack.pop_back();
			}
			while(!temp.empty()) {
				stack.push_back(temp.front());
				temp.pop_front();
			}*/
		}
		out << result;
		out << endl;
	}

	f.close();
	out.close();

	return 0;
}
