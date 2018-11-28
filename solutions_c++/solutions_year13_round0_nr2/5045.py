#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <algorithm>
using namespace std;

vector<int> getNumber(string str){
    vector<int> ret;
    string numS = "";
    for(int i=0; i<str.size(); i++){
	if(str[i] == ' ' && numS!=""){
	    ret.push_back( atoi(numS.c_str()) );
	    numS = "";
	}else
	    numS += str[i];
    }
    if(numS!="")
	ret.push_back( atoi(numS.c_str()) );

    return ret;
}

bool checkLawn(vector<vector<int> > &board, int N, int M){
    for(int n=0; n<N; n++){
	for(int m=0; m<M; m++){
	    int height = board[n][m];
	    bool possible = true;

	    // check up
	    for(int i=0; i<N; i++){
		if(board[i][m] > height){
		    possible = false;
		    break;
		}
	    }
	    if(possible) continue;

	    // check left
	    possible = true;
	    for(int j=0; j<M; j++){
		if(board[n][j] > height){
		    possible = false;
		    break;
		}
	    }

	    if(!possible) return false;
	}
    }
    return true;
}

int main(){
    ifstream input_file("B-large.in");
    ofstream output_file("B-large.out");
    string buff;
    vector<string> text;

    getline(input_file, buff);
    int total = atoi(buff.c_str());
    int caseCount = 0;

    while(getline(input_file, buff)){
	caseCount++;
	vector<int> init = getNumber(buff);
	int N = init[0];
	int M = init[1];

	vector< vector<int> > board;
	for(int i=0; i<N; i++){
	    getline(input_file, buff);
	    board.push_back( getNumber(buff) );
	}

	string result = checkLawn( board, N, M ) ? "YES" : "NO";
	output_file << "Case #" << caseCount << ": " << result << endl;
    }
    input_file.close();
    output_file.close();
    return 0;    
}
