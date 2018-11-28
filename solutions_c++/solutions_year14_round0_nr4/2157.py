#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void print(vector<double>& );

int regularWar(vector<double>& Naomi, vector<double>& Ken);
int deceitfulWar(vector<double>& Naomi, vector<double>& Ken);

struct Compare {
	double val;
	Compare(double val_): val(val_) {}
	bool operator()(double cmp) {
		return cmp > val;
	}
};

int main() {

	int testCases = 0;
	int numBlocks = 0;
	double NaomiBlock = 0;
	double KenBlock = 0;

	vector<double> regNaomi;
	vector<double> regKen;
	vector<double> decNaomi;
	vector<double> decKen;

	cin>>testCases;

	for (int c = 0; c < testCases; c++ ) {

		cin>>numBlocks;

		// Populate Naomi and Ken's blocks for regular War
		regNaomi.resize(numBlocks, 0);
		regKen.resize(numBlocks, 0);

		for (int i = 0; i < numBlocks; i++) {
			cin>>regNaomi[i];
		}

		for (int i = 0; i < numBlocks; i++) {
			cin>>regKen[i];
		}

		sort(regNaomi.begin(), regNaomi.end());
		sort(regKen.begin(), regKen.end());

		// Populate Naomi and Ken's blocks for Deceitful War
		decNaomi.resize(numBlocks, 0);
		decKen.resize(numBlocks, 0);

		for (int i = 0; i < numBlocks; i++) {
			decNaomi[i] = regNaomi[i];
		}

		for (int i = 0; i < numBlocks; i++) {
			decKen[i] = regKen[i];
		}

		cout<<"Case #"<<c+1<<": ";
		cout<<deceitfulWar(decNaomi, decKen)<<" ";
		cout<<regularWar(regNaomi, regKen)<<endl;


/*
		cout<<"************************************"<<endl;
		cout<<"Naomi Deceitful Wins: "<<deceitfulWar(decNaomi, decKen)<<endl;
		cout<<"************************************"<<endl;
*/
	}

	return 0;
}

// Regular War:
// Naomi's regular war strategy: keep playing her largest blocks, hoping
// for wins.
int regularWar(vector<double>& Naomi, vector<double>& Ken) {

	int NaomiWins = 0;
	int rounds = Naomi.size();

	for (int rounds = Naomi.size() - 1; rounds >= 0; rounds--) {

		// Under a blind strategy, Naomi will always player her biggest block
		// If Ken cannot beat it, he will play his smallest block.
		if (Naomi[rounds] > Ken[rounds]) {

//			cout<<"Naomi's "<<Naomi[rounds]<<" beats Ken's "<<Ken[rounds]<<endl;
			NaomiWins++;
			Naomi.pop_back();
			Ken.erase(Ken.begin(), Ken.begin() + 1);

		}

		// Otherwise, Ken will beat it with his smallest "larger" block.
		else {

			Compare c(Naomi[rounds]);

			// For small sample size, linear search will not be "too inefficient"
			vector<double>::iterator it;
			it = find_if(Ken.begin(), Ken.end(), c);

//			cout<<"Ken's "<<*it<<" beats Naomi's"<<Naomi[rounds]<<endl;

			Naomi.pop_back();
			Ken.erase(it, it + 1);
		}

	}

	return NaomiWins;
}

// Deceitful War:
// Naomi's Deceitful War strategy when she knows the weigh of each of Ken's
// blocks, and knowing the strategy that Ken will play.
int deceitfulWar(vector<double>& Naomi, vector<double>& Ken) {

	int NaomiWins = 0;
	int rounds = Naomi.size();

	for (int rounds = Naomi.size() - 1; rounds >= 0; rounds--) {

		// If Naomi has a block whose weight is smaller than all of Ken's,
		// she'll trade it for Ken's largest block by declaring val where
		// 2ndmax(Ken) < val < max(Ken), forcing Ken to play max(Ken) to
		// beat her min(Naomi).
		if (Naomi[0] < Ken[0]) {

//			cout<<"Ken's "<<Ken[rounds]<<" beats Naomi's "<<Naomi[0]<<endl;

			Ken.pop_back();
			Naomi.erase(Naomi.begin(), Naomi.begin() + 1);
		}

		// Otherwise, Naomi will take Ken's smallest block with her smallest
		// block. She will declare a value larger than all of Ken's blocks,
		// forcing Ken to play min(Ken). She will then play min(Naomi).
		else {

//			cout<<"Naomi's "<<Naomi[0]<<" beats Ken's "<<Ken[0]<<endl;

			NaomiWins++;
			Naomi.erase(Naomi.begin(), Naomi.begin() + 1);
			Ken.erase(Ken.begin(), Ken.begin() + 1);
		}

	}

	return NaomiWins++;

}
// Print:
// Prints the weights of Naomi or Ken's blocks.
void print(vector<double>& blocks) {

	for (int i = 0; i < blocks.size(); i++) {
		cout<<blocks[i]<<" ";
	}

	cout<<endl;
}
