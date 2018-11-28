#include <iostream>
#include <stdio.h>

using namespace std;

void init(char** &g, int r, int c);
void mark(char** g, int r, int c);

const char mine = '*';
const char space = '.';
const char choose = 'c';

int marked;
int R, C, M;


int main() {
  int T;
  cin >> T;
  for (int test=1; test <= T; test++) {
  	int r, c, m;
  	char **g = NULL;
		bool found = false;
		int placed = 0;
		
  	cin >> r >> c >> m;
  	R = r;
  	C = c;
  	M = m;
  	
  	init(g, R, C);
  
  	marked = 0;
 		while (1) {
	  	if (M == R*C - 1) {
				marked = 1;
				break;	
			}
			int moves[][2] = { {0,0}, {1,0}, {0,1}, {1,1},
												{2,0}, {2,1}, {0,2}, {1,2}, {2,2},
												{3,0}, {3,1}, {3,2}, {0,3}, {1,3}, {2,3}, {3,3} };		
 			try {
				for (int i=0; i < 16; i++)
					mark(g, moves[i][0], moves[i][1]);
			}
			catch(int n) {
				break;
			}

			break;		
		}
		if (M+marked == R*C)
			found = true;

		//////////////
		if (!found) {
	    if (g != NULL)
	    	delete g;
	  	init(g, R, C);
	  	marked = 0;
	 		while (1) {
				int moves[][2] = { {0,0}, {1,0}, {0,1}, {1,1},
													{2,0}, {0,2}, {2,1}, {1,2}, {2,2},
													{3,0}, {0,3}, {3,1}, {3,2}, {1,3}, {2,3}, {3,3} };													
	 			try {
					for (int i=0; i < 16; i++)
						mark(g, moves[i][0], moves[i][1]);
				}
				catch(int n) {
					break;
				}
				break;		
			}
			if (M+marked == R*C)
				found = true;			
		}
		
		//////////////		
		if (!found) {
	    if (g != NULL)
	    	delete g;

	  	init(g, R, C);
	  	marked = 0;
	 		while (1) {
				int moves[][2] = { {0,0}, {1,0}, {0,1}, {1,1},
													{2,0}, {0,2}, {2,1}, {1,2},
													{3,0}, {0,3}, {3,1}, {1,3}, {2,2}, {3,2}, {2,3}, {3,3} };
	 			try {
					for (int i=0; i < 16; i++)
						mark(g, moves[i][0], moves[i][1]);
				}
				catch(int n) {
					break;
				}
				break;		
			}
			
			if (M+marked == R*C)
				found = true;			
		}

		//////////////	
		if (!found) {
	    if (g != NULL)
	    	delete g;
	  	init(g, R, C);
	  	marked = 0;
	 		while (1) {
				int moves[][2] = { {0,0}, {1,0}, {0,1},
													{2,0}, {0,2}, {1,1}, {2,1}, {1,2}, {2,2},
													{3,0}, {0,3}, {3,1}, {1,3}, {3,2}, {2,3}, {3,3} };
	 			try {
					for (int i=0; i < 16; i++)
						mark(g, moves[i][0], moves[i][1]);
				}
				catch(int n) {
					break;
				}
				break;		
			}
			if (M+marked == R*C)
				found = true;			
		}		

		//////////////	
		if (!found) {
	    if (g != NULL)
	    	delete g;
	  	init(g, R, C);
	  	marked = 0;
	 		while (1) {
				int moves[][2] = { {0,0}, {1,0}, {2,0}, {3,0},
													{0,1}, {1,1}, {0,2}, {1,2}, {2,2},
													{2,1}, {0,3}, {3,1}, {1,3}, {3,2}, {2,3}, {3,3} };
	 			try {
					for (int i=0; i < 16; i++)
						mark(g, moves[i][0], moves[i][1]);
				}
				catch(int n) {
					break;
				}
				break;		
			}
			if (M+marked == R*C)
				found = true;			
		}		

		//////////////	
		if (!found) {
	    if (g != NULL)
	    	delete g;
	  	init(g, R, C);
	  	marked = 0;
	 		while (1) {
				int moves[][2] = { {0,0}, {0,1}, {0,2}, {0,3},
													{1,0}, {1,1}, {2,0}, {2,1}, {2,2},
													{1,2}, {3,0}, {3,1}, {1,3}, {3,2}, {2,3}, {3,3} };
	 			try {
					for (int i=0; i < 16; i++)
						mark(g, moves[i][0], moves[i][1]);
				}
				catch(int n) {
					break;
				}
				break;		
			}
			if (M+marked == R*C)
				found = true;			
		}

    
		cout << "Case #" << test << ":\n";
		if (!found)
			cout << "Impossible\n";
		else {
			g[0][0] = choose;
			for (int i=0; i < R; i++) {
				for (int j=0; j < C; j++) {
					cout << g[i][j];
					if (j == C-1)
						cout << endl;	
				}
			}
		}
    
    if (g != NULL)
    	delete g;
	}

  return 0;
}


void mark(char** g, int r, int c) {
	int count = 0;
	for (int i=r; i <= r+1; i++) {
		for (int j=c; j <= c+1; j++) {
			if (i < R && j < C && g[i][j] == mine) {
				g[i][j] = space;
				count++;
			}
		}
	}
	marked += count;
	
	if (marked + M >= R*C)
		throw marked;
}


void init(char** &g, int r, int c) {
	g = new char*[r];
	for (int i=0; i < r; i++)
    g[i] = new char[c];
    
	for (int i=0; i < r; i++)	
		for (int j=0; j < c; j++)
			g[i][j] = mine;
}

