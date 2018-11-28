#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int main()
{
	string input;
	int casenum;
	cin >> casenum;
	for(int id = 1; id <= casenum; id++) {
		cin >> input;
		string output = "";
		output += input[0];
		for(int i = 1; i < input.size(); i++) {
			if(input[i] >= output[0]) output = input[i] + output;
			else output = output + input[i];
		}
		printf("Case #%d: ", id);
		cout << output << endl;
	}
	return 0;
}