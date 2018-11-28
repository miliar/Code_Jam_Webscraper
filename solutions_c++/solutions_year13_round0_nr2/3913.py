#include<iostream>
#include<fstream>
#include<sstream>
#include<string>

using namespace std;

string convertInt(int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

int main(){
	int num, n, m, val;
	int board[100][100];
	string temp;
	char letter;
	bool poss, row, col;
	ifstream inFile;
	ofstream outFile;
	inFile.open("input.in");
    outFile.open("output.out");
    if(!inFile){
        cerr << "Unable to DIE";
    }
    inFile >> num;
	
	for(int i=0; i<num; i++){
		inFile >> n;
		inFile >> m;
		for(int j=0; j<n; j++){
			for(int k=0; k<m; k++){
				inFile >> board[j][k];
			}
		}
		outFile << "Case #" << convertInt(i+1) + ": ";
		
		poss = true;
		//Look for any 1 in the same row and col as a 2.
		for(int j=0; j<n; j++){
			for(int k=0; k<m; k++){
				row = false;
				col = false;
				val = board[j][k];
				for(int q=0; q<m; q++){
					if(board[j][q] > val){
						row = true;
					}
				}
				for(int q=0; q<n; q++){
					if(board[q][k] > val){
						col = true;
					}
				}
				if(row && col){
					poss = false;
				}
			}
		}
		
		if(poss){
			outFile << "YES\n";
		}
		else{
			outFile << "NO\n";
		}
		
	}
	
	inFile.close();
	outFile.close();
	return 1;
}