#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main () {
    
    int T;
    int i,j,k,x,y;
    int n,m;
    int M[100], N[100];
    int A[100][100];
    int cortable = 1;
    int cortaH,cortaV = 1;
    k = 0;
    string linea;
    string caso;
    cin >> T;
    
    while (k < T) {
	cin >> n >> m;
	cin.ignore();
	for (i=0; i<n; i++) {
	    getline(cin, linea);
	    istringstream iss(linea);
	    j = 0;
	    do
	    {
		iss >> A[i][j];
		j++;
	    } while (j<m);
	}
	
	cortable = 1;
	i = 0;
	while (i<n && cortable == 1) {
	    j = 0;
	    while (j<m && cortable == 1) {
		cortaH = 1;
		x = 0;
		while (x<m && cortaH == 1) {
		    if ((A[i][j] < A[i][x])) {
			cortaH = 0;
		    }
		    x++;
		}	
		cortaV = 1;
		y = 0;
		while (y<n && cortaV == 1) {
		    if ((A[i][j] < A[y][j])) {
			cortaV = 0;
		    }
		    y++;
		}
		if (cortaH == 0 && cortaV == 0) {
		    cortable = 0;
		}
		j++;
	    }
	    i++;
	}
	if (cortable == 0) {
	    caso = "NO";
	} else {
	    caso = "YES";
	}
	cout << "Case #" << k+1 << ": ";
	cout << caso << "\n";
	k++;
    }
}