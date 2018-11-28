#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int T = 1; T <= n; T++) {
    	int R;
    	int C;

    	cin >> R >> C;

    	char grid[100][100];

    	for (int r = 0; r < R; r++) {
    		for (int c = 0; c < C; c++) {
    			cin >> grid[r][c];

    		}
    	}

    	int change = 0;

    	//top down
    	for (int c = 0; c < C; c++) {
    		for (int r = 0; r < R; r++) {
    			if (grid[r][c] != '.') {

    				if (grid[r][c] == '^') {
    					//need to change
    					int found = 0;
    					for (int c1 = 0; c1 < C; c1++) {
    						if (c1 == c) {continue;}
    						if (grid[r][c1] != '.') {
    							found = 1;
    						}
    					}
    					for (int r1 = 0; r1 < R; r1++) {
    						if (r1 == r) {continue;}
    						if (grid[r1][c] != '.') {
    							found = 1;
    						}
    					}

    					if (!found) {change = -999999;}
    					change++;
    				}

    				break;
    			}
    		}
    	}

    	//bottom up    	
    	for (int c = 0; c < C; c++) {
    		for (int r = R-1; r >= 0; r--) {
    			if (grid[r][c] != '.') {

    				if (grid[r][c] == 'v') {
    					//need to change
    					int found = 0;
    					for (int c1 = 0; c1 < C; c1++) {
    						if (c1 == c) {continue;}
    						if (grid[r][c1] != '.') {
    							found = 1;
    						}
    					}
    					for (int r1 = 0; r1 < R; r1++) {
    						if (r1 == r) {continue;}
    						if (grid[r1][c] != '.') {
    							found = 1;
    						}
    					}

    					if (!found) {change = -999999;}
    					change++;
    				}

    				break;
    			}
    		}
    	}

    	//left to right 	
    	for (int r = 0; r < R; r++) {
    		for (int c = 0; c < C; c++) {
    			if (grid[r][c] != '.') {

    				if (grid[r][c] == '<') {
    					//need to change
    					int found = 0;
    					for (int c1 = 0; c1 < C; c1++) {
    						if (c1 == c) {continue;}
    						if (grid[r][c1] != '.') {
    							found = 1;
    						}
    					}
    					for (int r1 = 0; r1 < R; r1++) {
    						if (r1 == r) {continue;}
    						if (grid[r1][c] != '.') {
    							found = 1;
    						}
    					}

    					if (!found) {change = -999999;}
    					change++;
    				}

    				break;
    			}
    		}
    	}

    	//right to left
    	for (int r = 0; r < R; r++) {
    		for (int c = C-1; c >= 0; c--) {
    			if (grid[r][c] != '.') {

    				if (grid[r][c] == '>') {
    					//need to change
    					int found = 0;
    					for (int c1 = 0; c1 < C; c1++) {
    						if (c1 == c) {continue;}
    						if (grid[r][c1] != '.') {
    							found = 1;
    						}
    					}
    					for (int r1 = 0; r1 < R; r1++) {
    						if (r1 == r) {continue;}
    						if (grid[r1][c] != '.') {
    							found = 1;
    						}
    					}

    					if (!found) {change = -999999;}
    					change++;
    				}

    				break;
    			}
    		}
    	}

    	if (change >= 0) {
    		cout << "Case #" << T << ": " << change << endl;
    	} else {
    		cout << "Case #" << T << ": " << "IMPOSSIBLE" << endl;
    	}
    }
    return 0;
}