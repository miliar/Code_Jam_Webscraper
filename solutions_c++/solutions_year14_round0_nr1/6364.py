#include <iostream>
#include <fstream>
#include <vector>

void readcards(std::vector<std::vector<int> > &cards, int &choice, std::ifstream &small_in) {
	small_in >> choice;
	
	for(int i = 0; i < cards.size(); ++i) {
		for(int j = 0; j < cards[i].size(); ++j) {
			small_in >> cards[i][j];
		}
	}
	choice--;
}

int main() {
	using namespace std;
	
	ifstream small_in("A-small-attempt0.in");
	ofstream small_out("out.txt");
	
	// read number of test cases
	int test_cases;
	small_in >> test_cases;
	
	// cards chosen
	vector<vector<int> > cards(4, vector<int>(4, 0));
	vector<int>          possible(4, 0);
	
	int choice, count, guess = 0;
	
	for(int i = 0; i < test_cases; ++i) {
		// read cards and choice
		readcards(cards, choice, small_in);
		
		for(int j = 0; j < cards[choice].size(); ++j) {
			possible[j] = cards[choice][j];
		}
		
		// read cards second time
		readcards(cards, choice, small_in);
		count = 0;
		
		for(int j = 0; j < cards[choice].size(); ++j) {
			// how many of possible's cards are in that row?
			for(int k = 0; k < possible.size(); ++k) {
				if(cards[choice][j] == possible[k]) {
					++count;
					guess = possible[k];
					break;
				}
			}
		}
		
		small_out << "Case #" << i + 1 << ": ";
		
		switch(count) {
		case(0):
			small_out << "Volunteer cheated!";
			break;
		case(1):
			small_out << guess;
			break;
		default:
			small_out << "Bad Magician!";
		}
		
		small_out << endl;
	}
	
	small_in.close();
	
	
	
	
	return 0;
}
