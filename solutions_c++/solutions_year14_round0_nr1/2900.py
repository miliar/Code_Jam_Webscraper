#define N 4

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// read field and answer from standart input
void readField(int q[][N], int &a)
{
	cin >> a;
	a--;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> q[i][j];
		}
	}
}

int main (void)
{
	int T; 						// number of games
	int q1[N][N], q2[N][N]; 	// game fields
	int a1, a2;					// answers
	int r1[N], r2[N];			// chosen rows
	
	cin >> T;
	
	for (int t = 0; t < T; t++) {

		// get 2 input fields
		readField(q1, a1);
		for (int j = 0; j < N; j++) r1[j] = q1[a1][j];
		
		readField(q2, a2);
		for (int j = 0; j < N; j++) r2[j] = q2[a2][j];
		
		// compute set intersection
		sort(r1, r1 + N);
		sort(r2, r2 + N);
		vector<int> i(N);
		vector<int>::iterator it;
		it = set_intersection(r1, r1 + N, r2, r2 + N, i.begin());
		i.resize(it - i.begin());
		
		// Output
		cout << "Case #" << t+1 << ": "; 

		switch (i.size()) {
			case 1:
				cout << i[0];
				break;
			case 0:
				cout << "Volunteer cheated!";
				break;
			default:
				cout << "Bad magician!";
		}
		cout << endl;
			
	}
		
	return 0;	
}
			