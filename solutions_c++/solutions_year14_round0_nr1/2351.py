#include <iostream>

using namespace std;

int main() {

	int test_cases = 0;
	int first_row = 0;
	int second_row = 0;
	int dummy = 0;

	int first_cards[4] = {0, 0, 0, 0};
	int second_cards[4] = {0, 0, 0, 0};


	cin>>test_cases;

	for (int i = 0; i < test_cases; i++) {

		int num_match = 0;
		int match_value = 0;

		cin>>first_row;

		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (j == first_row - 1) {
					cin>>first_cards[k];
				} else {
					cin>>dummy;
				}
			}
		}

		cin>>second_row;

		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (j == second_row - 1) {
					cin>>second_cards[k];
				} else {
					cin>>dummy;
				}
			}
		}

		// If more than one match, bad magician
		// If no matches at all, volunteer cheated
		// If exactly one match, that is the answer

		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (first_cards[j] == second_cards[k]) {
					num_match++;
					match_value = first_cards[j];
				}
			}
		}

		cout<<"Case #"<<i+1<<": ";

		if (num_match > 1) {
			cout<<"Bad Magician!"<<endl;
		}
		else if (num_match < 1) {
			cout<<"Volunteer cheated!"<<endl;
		}
		else {
			cout<<match_value<<endl;
		}

	}

	return 0;

}