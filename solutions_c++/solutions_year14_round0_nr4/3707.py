#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

int chooseKen(long double choseNaomi, vector<long double> & Ken) {
	for(size_t i=0; i<Ken.size(); i++) {
		if(Ken[i] >= 0.0 && Ken[i] > choseNaomi) {
			Ken[i] = -1.0;
			return 0;
		}
	}
	return 1;
}

int main(int argc, char* argv[]) {
	ifstream input(argv[1]);
    size_t T, N, cc=0;
	long double temp = 0.0;
	
	if(input >> T) {
		while(cc++ < T && input >> N) {
			vector<long double> Naomi, Ken;
			size_t cheatpoints = 0, points = 0;

			while(N-- > 0 && input >> temp)
				Naomi.push_back(temp);

			N =  Naomi.size();
			while(N-- > 0 && input >> temp)
				Ken.push_back(temp);

			sort(Naomi.begin(), Naomi.end());
			sort(Ken.begin(), Ken.end());
			vector<double long> copyN(Naomi);

			/*for(size_t i=0; i<Naomi.size(); i++)
				cout << Naomi[i] << " ";
			cout << endl;
			for(size_t i=0; i<Ken.size(); i++)
				cout << Ken[i] << " ";
			cout << endl;*/

			for(size_t i=0; i<Ken.size(); i++)
				cheatpoints += chooseKen(Ken[i], copyN);

			for(size_t i=0; i<Naomi.size(); i++)
				points += chooseKen(Naomi[i], Ken);

			cout << "Case #" << cc << ": " <<  Naomi.size() - cheatpoints << " " << points << endl;			
		}		
	}

	return 0;
}
