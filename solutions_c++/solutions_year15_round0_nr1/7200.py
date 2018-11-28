#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main(){
	int T;
	cin >> T;

	for (int i = 0; i < T; i++){
		int Smax;
		cin >> Smax;
		string people;
		cin >> people;

		int total = 0;
		int last_total = 0;
		int inv_total = 0;
		for (int j = 0; j < people.size(); j++){
			string temp;
			temp.push_back(people[j]);
			last_total=total;
			total += atoi(temp.c_str());
			if (atoi(temp.c_str())!=0){
				if (last_total < j){
					inv_total += j - last_total;
					total += j - last_total;
				}
		}
		}
		//if (total < Smax){
			cout << "Case #" << i + 1 << ": " << inv_total << endl;
		//}
		//else cout << "Case #" << i+1 << ": " << 0 << endl;
	}
	


}