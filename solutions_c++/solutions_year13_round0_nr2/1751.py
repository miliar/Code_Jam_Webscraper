#include <iostream>
using namespace std;

// per ogni cella, se c'è almeno una cella con altezza maggiore
// sulla stessa riga, ed almeno una con altezza maggiore sulla stessa
// colonna, allora lo schema è impossibile. <- NE SONO CERTO
// Altrimenti è possibile <- UN PO' MENO CERTO

int lawn[100][100];

int main() {
	
	int T, N, M;
	bool found, row_higher, col_higher;
	
	cin >> T;
	for (int test_case = 0; test_case < T; test_case++) {
		
		// Input
		cin >> N >> M;
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				cin >> lawn[r][c];
			}
		}
		
		// Solving
		found = false;
		for (int r = 0; r < N && !found; r++) {
			for (int c = 0; c < M && !found; c++) {
				row_higher = false;
				col_higher = false;
				for (int rr = 0; rr < N; rr++) {
					if (lawn[rr][c] > lawn[r][c]) {
						row_higher = true;
						break;
					}
				}
				for (int cc = 0; cc < M; cc++) {
					if (lawn[r][cc] > lawn[r][c]) {
						col_higher = true;
						break;
					}
				}
				if (row_higher && col_higher) {
					found = true;
				}
			}
		}
		
		// Output
		if (found) cout << "Case #" << test_case + 1 << ": NO" << endl;
		else cout << "Case #" << test_case + 1 << ": YES" << endl;
	}
	
	return 0;
}
