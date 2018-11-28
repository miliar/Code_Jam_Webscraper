#include<iostream>
#include<fstream>
#include<vector>

using namespace std;


int main() {
	ifstream in("A-large.in");
	int tc_count;
	in >> tc_count;

//	cout << tc_count << endl;
	for(int i = 0;i<tc_count;++i) {
		int smax;
		in >> smax;
		//cout << smax << endl;
		int number_clapping = 0;
		int friends_needed = 0;
		in.ignore(1);
		for(int j = 0;j<smax + 1;++j){
			//read amount at this shyness
			int curr_shy = (int) in.get() - '0';
			//cout << curr_shy << endl;
			if(curr_shy > 0) {
				//if there are more people
				if(j < number_clapping){
					//these people will clap
					number_clapping += curr_shy;
				} else {
					//cout << "here" << endl;
					//these people wont clap without help
					int new_friends_needed = j - number_clapping;
					friends_needed += new_friends_needed;
					number_clapping += new_friends_needed + curr_shy;
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << friends_needed << endl;
	}
}
