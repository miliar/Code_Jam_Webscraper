#include<iostream>
#include<math.h>
#include<vector>
#include<sstream>
#include<cstdlib>
#include<fstream>
using namespace std;



int main() {
	ifstream file("input.txt");
	streambuf *cinbuf = cin.rdbuf();
	cin.rdbuf(file.rdbuf());
	int T;
	cin >> T;
	int caseno = 1;
	for(int i = 0; i < T; i++) {
		int fchoice;
		cin >> fchoice;
		int pass;
		for (int k = 0; k < (fchoice-1)*4;k++){
			cin >> pass;
			//cout << pass << endl;
		}
 		vector<int> vec1;
		vector<int> vec2; 
		int val;
		for (int k = 0; k < 4; k++){
			cin >> val;
			vec1.push_back(val);
		}
		for (int k = 0; k < (4-fchoice)*4; k++){
			cin >> pass;
			//cout << pass << endl;
		}
		int schoice;
		cin >> schoice;
		for (int k = 0; k < (schoice-1)*4;k++){
			cin >> pass;
			//cout << pass << endl;
		}
		for (int k = 0; k < 4; k++){
			cin >> val;
			vec2.push_back(val);
		}
		for (int k = 0; k < (4-schoice)*4; k++){
			cin >> pass;
			//cout << pass << endl;
		}
		int ct = 0;
		int m_card;
		for (int i = 0; i < vec1.size(); i++){
			for(int j = 0; j < vec2.size(); j++){
				if(vec1[i] == vec2[j]) {
					ct++;
					m_card = vec1[i];
				}
			}
		}
		if (ct == 1){
			cout << "Case #" << caseno << ":" << " " << m_card << endl;
		} else if (ct > 1) {
			cout << "Case #" << caseno << ":" << " Bad magician!" << endl;
		} else {
			cout << "Case #" << caseno << ":" << " Volunteer cheated!" << endl;

		}
		caseno++;
	}	

	//cout << "a";
	return 0;
}
