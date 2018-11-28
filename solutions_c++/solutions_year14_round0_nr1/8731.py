#include <iostream>
#include <vector>
#include <list>

using namespace std;

int main(){

	int number_of_cases;

	cin >> number_of_cases;
	for (int i =0; i< number_of_cases; ++i){
		vector< vector<int> > arrangement1;
		vector< vector<int> > arrangement2;

		arrangement1.resize(4);
		arrangement2.resize(4);
		for(int j = 0; j<4; ++j){
			arrangement1[j].resize(4);
			arrangement2[j].resize(4);
		}
		int row1, row2;
		cin >> row1;
		for(int j = 0; j<4; ++j){
			for(int k=0; k<4; ++k){
				cin >> arrangement1[j][k];
			}
		}
		cin >> row2;
		for(int j = 0; j<4; ++j){
			for(int k = 0; k<4; ++k){
				cin >> arrangement2[j][k];
			}
		}
		--row1;
		--row2;
		
		list<int> answer_list;
		for(auto r1 : arrangement1[row1]){
			for(auto r2 : arrangement2[row2]){
				if (r1 == r2)
					answer_list.push_back(r1);
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if(answer_list.empty())
			cout << "Volunteer cheated!";
		if(answer_list.size() > 1)
			cout << "Bad magician!";
		if(answer_list.size() == 1)
			cout << answer_list.front();
		cout << endl;
	}

}
