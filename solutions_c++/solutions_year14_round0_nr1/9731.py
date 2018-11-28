#include <iostream>
#include <vector>
#include <set>
using namespace std;

#define PB push_back

int main(){
	int tests;
	cin >> tests;
	for(int test = 1; test <= tests; ++test){
		int F1, F2;
		set<int> S1, S2;
		cin >> F1;
		for(int i = 1; i <= 4; ++i){
			for(int j = 0; j < 4; ++j){
				int temp;
				cin >> temp;
				if(i == F1)
					S1.insert(temp);
			}
		}
		cin >> F2;
		for(int i = 1; i <= 4; ++i){
			for(int j = 0; j < 4; ++j){
				int temp;
				cin >> temp;
				if(i == F2)
					S2.insert(temp);
			}
		}
		vector<int> RES;
		set<int>::iterator IT;
		for(IT = S1.begin(); IT != S1.end(); ++IT){
			if(S2.find(*IT) != S2.end())
				RES.PB(*IT);
		}
		if(RES.size() == 1)
			cout << "Case #" << test << ": " << RES[0] << "\n";
		else
			cout << "Case #" << test << ": " << ((RES.size() > 1)? "Bad magician!" : "Volunteer cheated!") << "\n";
	}
	return 0;
}