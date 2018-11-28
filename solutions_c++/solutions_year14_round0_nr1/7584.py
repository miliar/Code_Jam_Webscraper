#include <iostream>
#include <fstream>
using namespace std;

#define foreach(i, container) for(auto i=(container).begin(); i!=(container).end(); i++)
#define fortime(i,n) for(auto i=((n)-(n)); i<(n); i++)

int main() {
	ifstream input("input");
	ofstream output("output");
	int T;
	input >> T;
	fortime(i, T)
	{
		int row1, row2;
		int cards1[4][4], cards2[4][4];
		input >> row1;
		fortime(j, 4)
			fortime(k, 4)
				input >> cards1[j][k];
		input >> row2;
		fortime(j, 4)
			fortime(k, 4)
				input >> cards2[j][k];
		///////////////////////////////
		int cnt = 0;
		int result;
		fortime(j, 4){
			int find;
			find = cards1[row1 - 1][j];
			fortime(k, 4){
				if (find == cards2[row2 - 1][k]){
					result = find;
					cnt++;
				}
			}
		}
		///////////////////////////////
		if (cnt == 0)
			output << "Case #" << i+1 << ": Volunteer cheated!\n";
		else if (cnt == 1)
			output << "Case #" << i+1 << ": "<< result<<"\n";
		else 
			output << "Case #" << i+1 << ": Bad magician!\n";
	}
	return 0;
}