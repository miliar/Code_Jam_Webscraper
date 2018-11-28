#include<iostream>
#include<fstream>
#include<stdint.h>

#include<queue>

using namespace std;

struct grid {
    int row;
    int col;
    int val;

    grid(int r = -1, int c = -1, int v = -1) {
	row = r; col = c; val = v;
    }
};

ostream & operator << (ostream & os, const grid & g) {
    os <<"[ "<< g.row <<" "<<g.col <<" " << g.val<<" ]";
    return os;
}

class compare {
    public:
	bool operator () (const grid & lhs, const grid & rhs) const {
	    return lhs.val > rhs.val;
	}
};

typedef priority_queue<grid, vector<grid>, compare> pqueue;

int main(int argc, char ** argv) {
    //read
    ifstream file(argv[1]);
    //ifstream file("input.txt");
    ofstream ofile("output.txt");
    int numT;
    file>>numT;

    for(int i=0; i<numT; i++) {
	int rows, cols;
	file>>rows>>cols;

	int ** lawn = new int * [rows];
	for(int j=0; j<rows; j++)
	    lawn[j] = new int[cols];

	for(int r=0; r<rows; r++)
	    for(int c=0; c<cols; c++)
		file >> lawn[r][c];

	pqueue pq;

	for(int r=0; r<rows; r++)
	    for(int c=0; c<cols; c++) {
		pq.push(grid(r,c,lawn[r][c]));
	    }

	bool possible = true;
	while(!pq.empty()) {
	    grid g = pq.top();
	    pq.pop();
	    // keep the row number
	    bool goodrow = true;
	    for(int c = 0; c<cols; c++) {
		 goodrow = goodrow && (g.val>=lawn[g.row][c]);
	    }
	    
	    // keep the col number
	    bool goodcol = true;
	    for(int r = 0; r<rows; r++) {
		goodcol = goodcol && (g.val >= lawn[r][g.col]);
	    }

	    if(!goodrow && !goodcol) {
		possible = false;
		break;
	    }
	}
	ofile << "Case #"<<(i+1)<<": ";
	if(possible)
	    ofile << "YES"<<endl;
	else 
	    ofile << "NO"<<endl;
    }

    return 0;
}
