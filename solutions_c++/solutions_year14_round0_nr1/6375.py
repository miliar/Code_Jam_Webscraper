#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <array>
#include <algorithm>

using namespace std;

typedef vector<int> Row;
typedef vector<Row> Grid;

struct Choice {
	Grid grid;
	int row;
};

Choice readChoice(istream& in){
	Choice choice;

	int row;
	in >> row;
	choice.row = row - 1;

	for (int j = 0; j < 4; j += 1){
		Row line;
		for (int k = 0; k < 4; k += 1){
			int val;
			in >> val;
			line.push_back(val);
		}
		choice.grid.push_back(line);
	}

	return choice;
}

string solve(Choice c1, Choice c2){
	Row first(c1.grid[c1.row]);
	Row second(c2.grid[c2.row]);
	Row result(4);

	sort(begin(first), end(first));
	sort(begin(second), end(second));

	auto ending = set_intersection(begin(first), end(first), begin(second), end(second), begin(result));
	
	int size = ending - begin(result);
	if (size == 0){
		return "Volunteer cheated!";
	} else if (size == 1){
		return to_string(result[0]);
	} else {
		return "Bad magician!";
	}
}

int main(int argc, char** argv){
	ifstream in(argv[1]);

	string line;

	int T;
	in >> T;

	for (int i = 1; i <= T; i += 1){
		Choice c1(readChoice(in));
		Choice c2(readChoice(in));

		string answer(solve(c1, c2));

		cout << "Case #" << i << ": " << answer << endl;
	}
}