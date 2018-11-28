#include <iostream>
#include <fstream>
#include <set>

using namespace std;
int T, row1, row2;

int main(){
	ifstream infile("input.txt");
	infile >> T;

	set<int> cards;
	set<int> cards2;
	set<int> answer;

	for(int i = 1; i <= T; i++){
		cards.clear();
		cards2.clear();
		answer.clear();

		infile >> row1;

		for(int ii = 1; ii <= 4; ii++){
			int one, two, three, four;
			infile >> one >> two >> three >> four;
			if(ii == row1){
				cards.insert(one);
				cards.insert(two);
				cards.insert(three);
				cards.insert(four);
			}
		}

		infile >> row2;

		for(int ii = 1; ii <= 4; ii++){
			int one, two, three, four;
			infile >> one >> two >> three >> four;
			if(ii == row2){
				cards2.insert(one);
				cards2.insert(two);
				cards2.insert(three);
				cards2.insert(four);
			}
		}

		set_intersection(cards.begin(),cards.end(),cards2.begin(),cards2.end(), std::inserter(answer,answer.begin()));

		cout << "Case #" << i << ": ";
		if(answer.size() == 1){
			set<int>::iterator it = answer.begin();
			cout << *it << endl;
		}
		else if(answer.size() > 1){
			cout << "Bad magician!" << endl;
		}
		else{
			cout << "Volunteer cheated!" << endl;
		}
	}
}