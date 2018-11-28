#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char** argv){
    ifstream fIn;
    ofstream fOut;
    
    int T;
    int N;
    int M;
    
    vector<vector<int> >* lawn;
    vector<int>* row;
    vector<int>* col;

    bool possible;

    fIn.open("input.dat", ifstream::in);
    fOut.open("output.dat", ofstream::out);

    if(fIn.is_open() && fOut.is_open()){
	fIn >> T;

	for(int i=0; i<T; i++){
	    fIn >> N;
	    fIn >> M;
    
	    lawn = new vector<vector<int> >(N,vector<int>(M));
	    row = new vector<int>(N,0);
	    col = new vector<int>(M,0);
	    
	    for(int j=0; j<N; j++){
		for(int k=0; k<M; k++){
		    fIn >> (*lawn)[j][k];
		    (*row)[j] += (*lawn)[j][k];
		    (*col)[k] += (*lawn)[j][k];
		}
	    }
	    
	    possible = true;
	    for(int j=0; j<N; j++){
                for(int k=0; k<M; k++){
                    if((*row)[j] > (*lawn)[j][k]*M && (*col)[k] > (*lawn)[j][k]*N) possible=false;
                }
            }

	    fOut << "Case #" << i+1 << ": "; 
	    if(possible) fOut << "YES";
	    else fOut << "NO";
	    fOut << "\n";

	    delete lawn;
	    delete row;
	    delete col;
	}

	fIn.close();
	fOut.close();
    }
}
