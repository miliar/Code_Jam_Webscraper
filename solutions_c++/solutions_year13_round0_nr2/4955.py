#include <iostream>
#include <string>

using namespace std;

//global
int lawn[100][100];
int Nr;
int Mc;

/*
bool winrow(char c)
{
	for(int k=0; k<4; k++)
		if ( board[k][0] == c && 
		     board[k][1] == c && 
			 board[k][2] == c && 
			 board[k][3] == c)
			return true;
	
	return false;
}


bool wincol(char c)
{
	for(int k=0; k<4; k++)
		if ( board[0][k] == c && 
		     board[1][k] == c && 
			 board[2][k] == c && 
			 board[3][k] == c)
			return true;
	
	return false;
}

bool windiag(char c)
{
	if ( board[0][0] == c && 
		 board[1][1] == c && 
		 board[2][2] == c && 
		 board[3][3] == c)
			return true;
			
	if ( board[0][3] == c && 
		 board[1][2] == c && 
		 board[2][1] == c && 
		 board[3][0] == c)
			return true;
	
	return false;
}
*/


//true if cell could is compatible with row... 
// no higher lawn
bool testrow(int r, int c){
	int baseline = lawn[r][c];
	for(int k=0; k<Mc; k++){
		if ( lawn[r][k] > baseline )
			return false;
	}
	return true;
}


//true if cell could is compatible with column
// no higher lawn
bool testcol(int r, int c){
	int baseline = lawn[r][c];
	for(int k=0; k<Nr; k++){
		if ( lawn[k][c] > baseline )
			return false;
	}
	return true;
}


// true if cell is good.
bool testcell(int r, int c)
{
	return testcol(r,c) || testrow(r,c) ;
}


// true if possible
bool testlawn(){
	for(int k=0; k<Nr; k++)
		for(int j=0; j<Mc; j++){
			if (!testcell(k,j)){
				return false;
			}
		}
		
	return true;
}



int main () 
{
  int T;
    
  cerr << "Hello World" << endl;
  cin >> T;
  
  cerr << T << " test cases" << endl;

  //MAIN PROCESS LOOP
  for(int i=1; i<=T; i++)  
  {
	cerr << "Case #" << i << endl;
	// read input
	cin >> Nr >> Mc;
	
	for (int k=0; k<Nr; k++){
		for (int j=0; j<Mc; j++){
			cin >> lawn[k][j];
		}
	}

	// output input
	for (int k=0; k<Nr; k++){
		for (int j=0; j<Mc; j++){
			cerr << lawn[k][j] << " ";
		}
		cerr << endl;
	}
	

	// Process
	cout << "Case #" << i << ": ";

	bool ans = testlawn();
	
	if (ans){
		cout << "YES" << endl;
	}
	else
	{
		cout << "NO" << endl;
	}


	// answer
    cerr << endl;
  }
}
