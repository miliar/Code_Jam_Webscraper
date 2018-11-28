#include <iostream>
#include <algorithm>
using namespace std;

int R[2],G[2][5][5],M[17];
	
int main() {
	int T; 
	cin >> T;
	for(int Z = 1; Z <= T; Z++) {
		for(int i = 1; i <= 16; i++)
			M[i] = 0;
			
		for(int k = 0; k < 2; k++) {
			cin >> R[k];
			for(int r = 1; r <= 4; r++)
				for(int c = 1; c <= 4; c++)
					cin >> G[k][r][c];
		}
		
		for(int k = 0; k < 2; k++)
			for(int i = 1; i <= 4; i++)
				M[G[k][R[k]][i]]++;
		
		int result = 0;
		for(int i = 1; i <= 16; i++) {
			if(M[i] == 2) {
				for(int j = i+1; j<= 16; j++)
					if(M[j]==2)
						result = -1;
				if(result != -1)
					result = i;
			}
		}
		sort(M,M+17);
		if(M[16] != 2)
			cout << "Case #" << Z << ": Volunteer cheated!" << endl;
		else if(result == -1)
			cout << "Case #" << Z << ": Bad magician!" << endl;
		else
			cout << "Case #" << Z << ": " << result << endl;
	}
}