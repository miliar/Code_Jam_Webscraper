/* Lawnmower */
/*
 Auther: MM BARI
 progrmming language: c++
 email: talashbari@gmail.com
 */


#include <string>
using std::string;

#include <iostream>
using std::cerr;
using std::cout;
using std::endl;

#include <fstream>
using std::ifstream;
using std::ofstream;

using namespace std;
char board[4][4];
#include <map>
using std::map;

int main()
{
	
	ifstream input_file;
	ofstream output_file; 
	
    input_file.open("input.txt");
    output_file.open("output.txt");
  
	size_t cases;
	input_file >> cases;
	
	int N;
	int M;
	int aij;
	
	
	for (size_t i = 1; i <= cases; ++i) {

		input_file >> N;
		input_file >> M;

		int lawn[N][M];
		int expected_lawn[N][M];
		
		int set_point = 0;
		int expected_max_size = 0;
		int max_size = 0;
		
		for (size_t row = 0; row < N; ++row) {
			for (size_t col = 0; col < M; ++col) {
				input_file >> aij;
				if (max_size < aij) {
					max_size = aij;
				}
				lawn[row][col] = 100;
				expected_lawn[row][col] = aij;
			}
		}
		
		map<int, int> safe_list;
		// cut the maximum size from row 1 to N
		for (size_t row = 0; row < N; ++row) {
			expected_max_size = expected_lawn[row][0];
			// Finding the max size
			for (size_t col = 0; col < M; ++col) {
				if (expected_max_size < expected_lawn[row][col]) {
					expected_max_size = expected_lawn[row][col];
				}
			}
			// cutting the max size
			for (size_t col = 0; col < M; ++col) {
				if (expected_max_size == expected_lawn[row][col]) {
					set_point++;
					safe_list[col] += 1;
				}
				lawn[row][col] = expected_max_size;
			}	
		}
		
		if (set_point == (N*M)) {
			output_file << "Case #" <<i << ": YES";
			
			if (i != cases) {
				output_file << endl;
			}
			continue;
		}
		
		if (max_size > 1) {
			expected_max_size = max_size - 1;
		}
		
		// cut the next maximum size from column 1 to M
		for (size_t col = 0; col < M; ++col) {
			// cutting the next max size
			for (size_t row = 0; row < N; ++row) {
				if (safe_list[col] == N) {
					break;
				}
				lawn[row][col] = expected_max_size;
			}	
		}
		
		bool result = true;
		for (size_t row = 0; row < N; ++row) {
			for (size_t col = 0; col < M; ++col) {
				if (lawn[row][col] != expected_lawn[row][col]) {
					result = false;
					row = N;
					break;
				}
			}
		}
				
		
		if (result) {
			output_file << "Case #" <<i << ": YES";
		} else {
			output_file << "Case #" <<i << ": NO";
		}

		if (i != cases) {
			output_file << endl;
		}
	}				
	
    input_file.close();
    output_file.close();
	return 0;
}