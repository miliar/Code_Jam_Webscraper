/*Dijkstra 4-10-15
Transferred from python version cause that one too slow
*/

#include <iostream>
#include <fstream>
#include <vector>

#define f0(i, N) for (int i = 0; i < N; i++)

using namespace std;

char operations[4][4] = 
	{
		{1, 2, 3, 4},
		{2, -1, 4, -3},
		{3, -4, -1, 2},
		{4, 3, -2, -1}
	};

char multiply (char a, char b) {
	if (a > 0 && b > 0)
		return operations[a - 1][b - 1];
	else if (b > 0)
		return -operations[-a - 1][b - 1];
	else if (a > 0)
		return -operations[a - 1][-b - 1];
	else
		return operations[-a - 1][-b - 1];
}

int main() {
	ifstream fin ("dijkstra.in");
	ofstream fout ("dijkstra.out");

	int T;
	fin >> T;

	f0(caseno, T) {
		cout << "C:" << caseno << endl;
		int L, X;
		fin >> L >> X;

		char text[L * X];
		f0(i, L) {
			char letter;
			fin >> letter;
			f0(j, X) 
				text[i + j * L] = (letter - 'i' + 2);
		}

		vector <int> start;
		vector <int> finish;
		char value = 1;
		f0(i, L*X) {
			value = multiply(value, text[i]);
			if (value == 2)
				start.push_back(i);
		}
		cout << start.size() << endl;
		/*
		f0(i, start.size())
			cout << start[i] << ",";
		cout << endl;
		*/

		value = 1;
		for (int i = L*X - 1; i >= 0; i--) {
			value = multiply(text[i], value);
			if (value == 4)
				finish.push_back(i);
		}
		cout << finish.size() << endl;
		/*
		f0(i, finish.size())
			cout << finish[i] << ",";
		cout << endl;
		*/

		bool found = false;

		f0(i, start.size()) {
			if (finish.size() == 0 || finish[0] <= start[i])
				break;

			int counter;
			for(counter = finish.size() - 1; counter >= 0 && finish[counter] <= start[i]; counter--);;

			char value = 1;
			for (int j = start[i] + 1; j < finish[0]; j++) {
				value = multiply(value, text[j]);
				if (j == finish[counter] - 1) {
					if (value == 3) {
						found = true;
						break;
					}
					counter--;
					if (counter < 0)
						break;
				}
			}

			/*
			f0(j, finish.size()) {
				if (start[i] < finish[j]) {
					char value = 1;
					for (int k = start[i] + 1; k < finish[j]; k++)
						value = multiply(value, text[k]);
					if (value == 3) {
						found = true;
						break;
					}
				}
			}
			*/
			if (found)
				break;
		}


		/*
		char dp[L * X][L * X];
		f0(i, L*X)
			f0(j, L*X - i)
				if (i == 0)
					dp[j][j + i] = text[j];
				else
					dp[j][j + i] = multiply(dp[j][j + i - 1], text[j + i]);

		bool found = false;
		f0(i, L * X) {
			if (dp[0][i] == 2)
				for (int j = i + 1; j < L*X; j++)
					if (dp[i + 1][j] == 3 && dp[j + 1][L*X - 1] == 4) {
						found = true;
						break;
					}
			if (found)
				break;
		}
		*/

		fout << "Case #" << caseno + 1 << ": " << (found ? "YES" : "NO") << endl;
	}

	return 0;
}