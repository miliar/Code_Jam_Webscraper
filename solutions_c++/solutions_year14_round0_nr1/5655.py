#include <iterator>
#include <algorithm>
#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <vector>
using namespace std;


set<int> getCardRow(ifstream& input_file)
{
	int row;
	input_file >> row;

	string line;
	set<int> cards;
	getline(input_file, line);
	for (int j = 1; j <= 4; ++j) {
		getline(input_file, line);
		if (row == j) {
			istringstream sstr(line);
			sstr.str(line);
			copy(istream_iterator<int>(sstr), istream_iterator<int>(), inserter(cards, cards.begin()));
		}
	}

	return cards;
}

void main()
{
	ifstream input_file("input.txt");
	ofstream output_file("output.txt");

	int nbCases;
	input_file >> nbCases;

	for (int i = 1; i <= nbCases; ++i) {
		
		auto cardRow1 = getCardRow(input_file);
		auto cardRow2 = getCardRow(input_file);

		vector<int> result;
		set_intersection(begin(cardRow1), end(cardRow1), begin(cardRow2), end(cardRow2), back_inserter(result));

		output_file << "Case #" << i << ": ";

		if (result.empty()) {
			output_file << "Volunteer cheated!" << endl;
		}
		else if (result.size() == 1) {
			output_file << result[0] << endl;
		}
		else {
			output_file << "Bad magician!" << endl;
		}

	}
	


}