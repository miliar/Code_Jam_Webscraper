#include<fstream>
#include<iostream> 
using namespace std;

int main(){
	ifstream f("A-small-attempt2.in");
	ofstream g("Output");
	int T, i, j, k, answer1, answer2, line1[4], line2[4], card;
	int number_of_matches, match_position;
	f >> T;
	for(i = 0; i < T; ++i){
		// first configuration
		f >> answer1;
		for(j = 0; j < 4; ++j)
			for(k = 0; k < 4; ++k){
				f >> card;
				if(j == answer1 - 1)
					line1[k] = card;
			}
			
		// second configuration
		f >> answer2;
		for(j = 0; j < 4; ++j)
			for(k = 0; k < 4; ++k){
				f >> card;
				if(j == answer2 - 1)
					line2[k] = card;
			}
			
		// processing the answers
		number_of_matches = 0;
		match_position = 0;
		for(j = 0; j < 4; ++j)
			for(k = 0; k < 4; ++k)
				if(line1[j] == line2[k]){
					++number_of_matches;
					match_position = j;
				}
		if(number_of_matches == 1){
			g << "Case #" << i+1 << ": " << line1[match_position] << endl;
			continue;
		}
		if(number_of_matches > 1){
			g << "Case #" << i+1 << ": " << "Bad magician!" << endl;
			continue;
		}
		g << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
	}
	return 0;
}
