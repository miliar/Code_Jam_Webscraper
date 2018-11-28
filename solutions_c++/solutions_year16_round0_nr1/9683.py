#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <climits>
#include <algorithm>

using namespace std;

vector<string> outputs;
vector<string> inputs;

void readInFile() {
	string line;
	ifstream myfile("A-large.in");
	if (myfile.is_open())
	{
		while (getline(myfile, line))
		{
			inputs.push_back(line);
		}
		myfile.close();
	}
	inputs.erase(inputs.begin());
}

void outputAnswer() {
	ofstream myfile("angry.out");
	if (myfile.is_open())
	{
		for (int i = 0; i < outputs.size(); i++) {
			myfile << "Case #" + to_string(i+1) + ": " + (outputs[i]) + "\n";
		}
		myfile.close();
	}
}

bool isDoneCounting(bool has_seen[]) {
	bool isDone = true;
	for (int i = 0; i < 10; i++) {
		isDone = isDone && has_seen[i];
	}
	return isDone;
}

int main() {
	readInFile();
	for (int i = 0; i < inputs.size(); i++) {
		int starting_num = stoi(inputs[i]);
		int num_on = 0;
		int mult_factor = 1;
		bool loopDone = false;
		bool has_seen[] = { false, false, false, false, false, false, false, false, false, false };
		bool abort = false;
		while (!loopDone) {
			num_on = starting_num * mult_factor;
			if (num_on == starting_num * (mult_factor + 1)) {
				abort = true;
				break;
			}
			string number_on = to_string(num_on);
			for (int j = 0; j < number_on.length(); j++) {
				int digit = stoi(number_on.substr(j, 1));
				has_seen[digit] = true;
			}
			mult_factor++;
			loopDone = isDoneCounting(has_seen);
		}
		if (!abort) {
			outputs.push_back(to_string(num_on));
		}
		else {
			outputs.push_back("INSOMNIA");
		}
	}
	outputAnswer();

}