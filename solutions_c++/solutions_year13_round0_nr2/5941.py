#include <iostream>
#include <vector>
using namespace std;

void echo(vector < vector <int> > map, int r, int c)
{
	for (int i = 0; i < r; i++) {
		for (int j = 0 ; j < c; j++)
			cout << map[i][j] << " ";
		cout << "\n";
	}
}

int main()
{
	int test;
	cin >> test;
	
	for (int t = 1; t <= test; t++) {
		vector < vector<int> > lwn, map;
		int r, c;
		cin >> r >> c;

		for (int i = 0; i < r; i++) {
			vector <int> a, b;
			int h;
			for (int j = 0; j < c; j++) {
				cin >> h;
				a.push_back(h);
				b.push_back(0);
			}
			map.push_back(b);
			lwn.push_back(a);
		}
		//from left and right
		
		for (int i = 0; i < r; i++) {
			int m = 0;
			for (int j = 0; j < c; j++) 
				if (m < lwn[i][j])
					m = lwn[i][j];
			for (int j = 0; j < c; j++)
				if (lwn[i][j] == m)
					map[i][j] = 1;
		}
		//from top and bottom
	
		for (int i = 0; i < c; i++) {
			int m = 0;
			for (int j = 0; j < r; j++)
				if (m < lwn[j][i])
					m = lwn[j][i];
			for (int j = 0; j < r; j++)
				if (lwn[j][i] == m)
					map[j][i] = 1;
		}	
		
		int stat = 1;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++)
				if (map[i][j] == 0) {
					stat = 0;
					break;
				}
			if (!stat) break;
		}
		if (stat) 
			cout << "Case #" << t << ": YES\n";
		else	
			cout << "Case #" << t << ": NO\n";
	}
}
