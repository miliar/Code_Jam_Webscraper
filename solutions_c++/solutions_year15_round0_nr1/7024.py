#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

// each shyness level have 0-9 people
// at most 1000 shyness levels

struct ProblemInput{
	int s_max; // s_max+1 = digits.size
	string digits_s;
};

int solve_problem(int s_max, string digits_s);

void get_input(int &num_tests, vector<ProblemInput> &inputs);

void output(int case_num, int answer, string file);

void test();

void main() {
	//test();

	int num_tests = 0;
	vector<ProblemInput> inputs;
	get_input(num_tests, inputs);

	for (int i = 0; i < num_tests; i++) {
		int answer = solve_problem(inputs[i].s_max, inputs[i].digits_s);

		output(i + 1, answer, "output-large.txt");
	}
}

void test() {
	int num_tests = 0;
	vector<ProblemInput> inputs;
	get_input(num_tests, inputs);

	for (int i = 0; i < num_tests; i++) {
		int answer = solve_problem(inputs[i].s_max, inputs[i].digits_s);

		cout << answer << endl;
	}
}

void get_input(int &num_tests, vector<ProblemInput> &inputs) {
	ifstream infile("A-large.in");
	if (infile.is_open()) {
		infile >> num_tests;
		for (int i = 0; i < num_tests; i++) {
			ProblemInput input;
			infile >> input.s_max;
			infile >> input.digits_s;
			inputs.push_back(input);
		}
	}
	else {
		cout << "Failed to open input files." << endl;
	}
}

void output(int case_num, int answer, string file) {
	ofstream myfile(file, ios::app); // append a new line
	if (myfile.is_open()) {
		myfile << "Case #" << case_num << ": " << answer << endl;
		myfile.close();
	}
	else {
		cout << "Unable to open output file" << endl;
		exit(0);
	}
}

int solve_problem(int s_max, string digits_s) {
	vector<int> shyness_count(s_max+1, 0); // init as all 0s
	for (int i = 0; i < digits_s.size(); i++) {
		shyness_count[i] = digits_s[i] - '0';
	}

	int answer = 0;
	int standup = 0; // the num of standup people
	for (int i = 0; i < shyness_count.size(); i++) {
		if (standup < i) {
			int delta = i - standup; // need some friends
			answer += delta;
			standup += delta + shyness_count[i];
		}
		else { // they standup by themselves
			standup += shyness_count[i];
		}
	}

	return answer;
}