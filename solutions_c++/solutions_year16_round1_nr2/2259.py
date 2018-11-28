#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int N;
vector< vector<int> > raw_line;
int data[50][50];
bool used[100];

int ans;
bool ans_row;

bool pick_data(int row) {
	if (row == N)
		return true;
	int min = 9999;
	int min_index1 = -1;
	int min_index2 = -1;
	bool minus_row;
	int minus_index;
	for (int i = 0; i < 2 * N - 1; i++) {
		if (used[i] == false) {
			if (raw_line[i][row] < min) {
				min = raw_line[i][row];
				min_index1 = i;
				min_index2 = -1;
			}
			else if (raw_line[i][row] == min) {
				min_index2 = i;
			}
		}
	}
	if (min_index2 != -1) {
		used[min_index1] = true;
		used[min_index2] = true;
		//try first candidate as row
		bool check = true;
		minus_index = -1;
		for (int i = 0; i < row; i++) {
			if (data[row][i] == -1) {
				minus_row = true;
				minus_index = i;
			} else if (data[row][i] != raw_line[min_index1][i]) {
				check = false;
				break;
			}
		}
		for (int i = 0; i < row; i++) {
			if (data[i][row] == -1) {
				minus_row = false;
				minus_index = i;
			} else if (data[i][row] != raw_line[min_index2][i]) {
				check = false;
				break;
			}
		}
		if (check) {
			//put frist candidate as row
			for (int i = row; i < N; i++)
				data[row][i] = raw_line[min_index1][i];
			for (int i = row; i < N; i++)
				data[i][row] = raw_line[min_index2][i];
			if (minus_index != -1) {
				if (minus_row)
					data[row][minus_index] = raw_line[min_index1][minus_index];
				else
					data[minus_index][row] = raw_line[min_index2][minus_index];
			}
			bool ret = pick_data(row + 1);
			if (ret == true)
				return true;
			if (minus_index != -1) {
				if (minus_row)
					data[row][minus_index] = -1;
				else
					data[minus_index][row] = -1;
			}
		} 
		//try first candidate as col
		check = true;
		minus_index = -1;
		for (int i = 0; i < row; i++) {
			if (data[row][i] == -1) {
				minus_row = true;
				minus_index = i;
			} else if (data[row][i] != raw_line[min_index2][i]) {
				check = false;
				break;
			}
		}
		for (int i = 0; i < row; i++) {
			if (data[i][row] == -1) {
				minus_row = false;
				minus_index = i;
			}
			else if (data[i][row] != raw_line[min_index1][i]) {
				check = false;
				break;
			}
		}
		if (check) {
			//put frist candidate as col
			for (int i = row; i < N; i++)
				data[row][i] = raw_line[min_index2][i];
			for (int i = row; i < N; i++)
				data[i][row] = raw_line[min_index1][i];
			if (minus_index != -1) {
				if (minus_row)
					data[row][minus_index] = raw_line[min_index2][minus_index];
				else
					data[minus_index][row] = raw_line[min_index1][minus_index];
			}
			bool ret = pick_data(row + 1);
			if (ret == true)
				return true;
			if (minus_index != -1) {
				if (minus_row)
					data[row][minus_index] = -1;
				else
					data[minus_index][row] = -1;
			}
		}
		used[min_index1] = false;
		used[min_index2] = false;
		return false;
	}
	else {
		used[min_index1] = true;
		ans = row;
		//try first candidate as row
		bool check = true;
		for (int i = 0; i < row; i++) {
			if (data[row][i] != -1 && data[row][i] != raw_line[min_index1][i]) {
				check = false;
				break;
			}
		}
		if (check) {
			//put frist candidate as row
			for (int i = row; i < N; i++)
				data[i][row] = -1;
			for (int i = row; i < N; i++)
				data[row][i] = raw_line[min_index1][i];
			ans_row = false;
			bool ret = pick_data(row + 1);
			if (ret == true)
				return true;
		}
		//try first candidate as col
		check = true;
		for (int i = 0; i < row; i++) {
			if (data[i][row] != -1 && data[i][row] != raw_line[min_index1][i]) {
				check = false;
				break;
			}
		}
		if (check) {
			//put frist candidate as col
			for (int i = row; i < N; i++)
				data[row][i] = -1;
			for (int i = row; i < N; i++)
				data[i][row] = raw_line[min_index1][i];
			ans_row = true;
			bool ret = pick_data(row + 1);
			if (ret == true)
				return true;
		}
		used[min_index1] = false;
		return false;
	}
}

bool run() {
	for (int i = 0; i < 2 * N; i++)
		used[i] = false;
	return pick_data(0);
	
}

int main() {
	int T;
	int temp_int;
	ifstream in("B-small-attempt1.in");
	ofstream out("output.txt");
	in >> T;
	for (int t = 0; t < T; t++) {
		raw_line.clear();
		in >> N;
		for (int i = 0; i < 2 * N - 1; i++) {
			vector<int> temp;
			for (int j = 0; j < N; j++) {
				in >> temp_int;
				temp.push_back(temp_int);
			}
			raw_line.push_back(temp);
		}
		if (!(run()))
			cout << "error" << t << endl;
		//output
		out << "Case #" << t + 1 << ": ";
		for (int i = 0; i < N; i++) {
			if (ans_row) {
				out << data[ans][i] << ' ';
			}
			else {
				out << data[i][ans] << ' ';
			}
		}
		out << endl;
	}
	in.close();
	out.close();
	return 0;
}