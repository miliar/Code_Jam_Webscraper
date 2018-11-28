#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm> 
#include <vector>
using namespace std;

int main(int argc, char* argv[])
{
	ifstream input;
	ofstream output;
	
	input.open(argv[1]);
	output.open("output.out");

	int cases;
	input >> cases;

	for (int c = 1; c <= cases; c++) {
		int N;
	
		input >> N;
		
		vector<double> Ken(N), Naomi(N);

		for (int i = 0; i < N; i++) {
			input >> Naomi[i];
		}
	
		for (int i = 0; i < N; i++) {
			input >> Ken[i];
		}
	
		sort(Ken.begin(), Ken.end());
		sort(Naomi.begin(), Naomi.end());
		
		int N_go_first = 0, K_go_first = 0;

		for (int n_pos = 0, k_pos = 0; n_pos < N; n_pos++) {
			for (; k_pos < N; k_pos++) {
				if (Ken[k_pos] > Naomi[n_pos]) {
					N_go_first++;
					k_pos++;
					break;
				}
			}
		}
		
		for (int n_pos = 0, k_pos = 0; k_pos < N; k_pos++) {
			for (; n_pos < N; n_pos++) {
				if (Naomi[n_pos] > Ken[k_pos]) {
					K_go_first++;
					n_pos++;
					break;
				}	
			}
		}
		
		output << "Case #" << c << ": ";
		output << K_go_first << " " << N - N_go_first;
		
		if (c != cases) {
			output << endl;
		}
	}
	
	input.close();
	output.close();
}
