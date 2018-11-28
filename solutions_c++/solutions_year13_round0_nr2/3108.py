#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>

using namespace std;

int main (int argc, char *argv[]) {
	
	size_t T, count = 1;
	string line;
	
	// get T
	getline(cin, line);
	stringstream(line) >> T;

	// get all cases and process it
	for(size_t count = 1; count <= T; count++) {
		// get N, M
		int N, M;
		getline(cin, line);
		stringstream(line) >> N >> M;
		
		// init
		int lawn[N][M];
		bool f[N][M];
		bool feasible = true;
		for(size_t i = 0; i < N; i++) {
			for(size_t j = 0; j < M; j++)
				f[i][j] = false;
		}
			
		// read data
		for(size_t i = 0; i < N; i++) {
			getline(cin, line);
			stringstream ss(line);
			for(size_t j = 0; j < M; j++)
				ss >> lawn[i][j];
		}
		
		// test each row
		for(size_t i = 0; i < N; i++) {
			// find max cut
			int max = lawn[i][0];
			for(size_t j = 1; j < M; j++) {
				if (lawn[i][j] > max)
					max = lawn[i][j];
			}
			
			// cut the max
			for(size_t j = 0; j < M; j++) {
				if (lawn[i][j] == max)
					f[i][j] = true;
			}
		}
		
		// test each column
		for(size_t j = 0; j < M && feasible; j++) {
			// find max cut
			int max = lawn[0][j];
			for(size_t i = 1; i < N; i++) {
				if (lawn[i][j] > max)
					max = lawn[i][j];
			}
			
			// cut the max
			for(size_t i = 0; i < N; i++) {
				if (lawn[i][j] == max)
					f[i][j] = true;
				if (f[i][j] == false) {
					feasible = false;
					break;
				}
			}
		}
		
		// // print data
		// for(size_t i = 0; i < N; i++) {
		// 	for(size_t j = 0; j < M; j++)
		// 		cout << setw(3) << lawn[i][j];
		// 	cout << endl;
		// }
		// cout << "--" << endl;
		// for(size_t i = 0; i < N; i++) {
		// 	for(size_t j = 0; j < M; j++)
		// 		cout << setw(3) << f[i][j];
		// 	cout << endl;
		// }
		
		// print output
		cout << "Case #" << count << ": ";
		if (feasible)
			cout << "YES";
		else
			cout << "NO";
		cout << endl;
		
		// cout << "===========" << endl;
	}
	
	return 0;
}