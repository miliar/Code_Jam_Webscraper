#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#define MAX_C	1000
#define MAX_P	1000

#define MAX_N	50
#define MAX_I	2000

vector<int> instersection(vector<int> &v1, vector<int> &v2);

int main(int argc, char *argv[]) {
	int T; // Number of Test cases
	vector<int> A1[4]; // Actual arrangement
	vector<int> A2[4]; // Actual arrangement

	cin >> T;

	for(int t=0; t<T; ++t) {
		int answer1, answer2; // Answer for this arrangement

		// Paso 1: guardo la fila
		cin >> answer1;

		for(int row=0; row<4; ++row) {
			for(int col=0; col<4; ++col) {
				int c;

				cin >> c;
				A1[row].push_back(c);
			}
		}

		// Paso 2: obtengo la segunda respuesta
		cin >> answer2;

		for(int row=0; row<4; ++row) {
			for(int col=0; col<4; ++col) {
				int c;
				
				cin >> c;
				A2[row].push_back(c);
			}
		}

		// Paso 3: Conjunto resultado
		vector<int> res;
		
		res= instersection(A1[answer1-1], A2[answer2-1]);

		switch(res.size()) {
			case 0:
				cout << "Case #" << t+1 << ": Volunteer cheated!" << endl;
				break;
			case 1:
				cout << "Case #" << t+1 << ": " << res[0] << endl;
				break;

			default:
				cout << "Case #" << t+1 << ": Bad magician!" << endl;
				break;
		}

		for(int row=0; row<4; ++row) {
				A1[row].clear();
				A2[row].clear();
		}
	}

}

vector<int> instersection(vector<int> &v1, vector<int> &v2)
{

    vector<int> v3;

    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());

    set_intersection(v1.begin(),v1.end(),v2.begin(),v2.end(),back_inserter(v3));

    return v3;
}