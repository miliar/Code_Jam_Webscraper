#include <iostream>
#include <vector>

using namespace std;

int m1[5][5], m2[5][5];
vector < int > v;

int main( int argc, char ** argv)
{
	int t, res1, res2;

	cin >> t;
	for(int x = 1; x <= t; x++) {

		cin >> res1;
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++)
				cin >> m1[i][j];
			
		cin >> res2;
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++)
				cin >> m2[i][j];

		for(int i = 1; i <= 4; i++) {

			for(int j = 1; j <= 4; j++) {

				if(m1[res1][i] == m2[res2][j]) {
					v.push_back(m1[res1][i]);
				}
			}
		}

		cout << "Case #" << x << ": ";

		if(v.size() == 0)
			cout << "Volunteer cheated!\n";
		else if(v.size() > 1)
			cout << "Bad magician!\n";
		else 
			cout << v[0] << "\n";

		v.clear();
	}

	return 0;
}
