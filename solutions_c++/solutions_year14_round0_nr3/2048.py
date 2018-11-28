#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

void recblock(vector<vector<char> > board, set<int>& legalfree ,int oldsize, int maxdim, int height, int maxheight, int rows, int freecells, int cols, int& printed, ofstream& outfile){
    //cout<<"{"<<height<<"}" ;
    if (height<maxheight){
        //cout<<"{"<<height<<"}" ;
        ++height;
        for(int j=0; j <= maxdim;j++){
            if (cols>rows){
                board[rows-height][0]='.';
                board[rows-height][1]='.';
                for (int l=0; l<j;l++){
                    board[rows-height][j+1]='.';
                }
            }
            else{
                board[rows-1][height-1]='.';
                board[rows-2][height-1]='.';
                for (int l=0; l<=j;l++){
                    board[rows-(2+l)][height-1]='.';
                }
            }
            if (freecells == (oldsize +2+j) && printed == 0){
                board[rows-1][0]='c';
                
                for (int j = 0; j < rows; ++j){
                    
                    for (int k = 0; k < cols; ++k){
                        outfile << board[j][k];
                    }
                    outfile <<endl;
                }
                //cout<<endl;
                //cout<<"["<< oldsize<<","<<oldsize +2+j<<","<< height <<" "<<maxheight <<"]" ;
                printed=1;
            }
            legalfree.insert(oldsize +2+j);
            
            recblock(board, legalfree, (oldsize +2 +j),j,height,maxheight, rows, freecells, cols, printed, outfile);
        }
    }
}

int main (int argc, char* args[]){
    ifstream infile;
    ofstream outfile;
    
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        infile.open("small.in");
        outfile.open("small.out");
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
        infile.open("large.in");
        outfile.open("large.out");
    }
    
    int cases;
    infile >> cases;
    cout << cases << endl ;
    
    //algorithm
    
    int rows;
    int cols;
    int mines;
    int freecells;
    int impossible;
    vector<vector<char> > board;
    int printed;
    
    for (int i=0; i<cases; ++i) {
        outfile << "Case #" << i+1 << ":" << endl ;
        // read from file
        printed =0;
        infile >> rows;
        infile >> cols;
        infile >> mines;
        
        impossible = 1;
        freecells = rows*cols - mines;
        board.resize(rows);
        for (int j = 0; j < rows; ++j)
            board[j].resize(cols);
        
        for (int j = 0; j < rows; ++j)
                for (int k = 0; k < cols; ++k)
                    board[j][k]='*';
        /*
        cout<<endl;
        for (int j = 0; j < rows; ++j){
            cout <<endl;
            for (int k = 0; k < cols; ++k){
                cout << board[j][k];
            }
        }
        */
        int mindim = min(rows,cols);
        int maxdim = max(rows,cols);
        
        set<int> legalfree;
        
        legalfree.insert(1);
        
        if (freecells == 1 && printed == 0){
            board[rows-1][0]='c';
            
            for (int j = 0; j < rows; ++j){
                
                for (int k = 0; k < cols; ++k){
                    outfile << board[j][k];
                }
                outfile <<endl;
            }
            
            printed = 1;
        }

        
        
        //cout<<freecells<<" legal: ";
        
        if (mindim == 1){
            for(int j=0; j < maxdim-1; ++j){
                legalfree.insert(2 + j);
                if (cols<rows){
                    board[rows-1][0]='.';
                    board[rows-2][0]='.';
                    for (int l=0; l<=j;l++){
                        board[rows-(2+l)][0]='.';
                    }
                }
                
                if (cols>rows){
                    board[0][0]='.';
                    board[0][1]='.';
                    for (int l=0; l<j;l++){
                        board[0][2+l]='.';
                    }
                }
                
                
                if (freecells == 2 + j && printed == 0){
                    board[rows-1][0]='c';
                    
                    for (int j = 0; j < rows; ++j){
                        
                        for (int k = 0; k < cols; ++k){
                            outfile << board[j][k];
                        }
                        outfile <<endl;
                    }
                    
                    printed = 1;
                }

                
                
                
                
                
            }
                

        }
        else{
            for(int j=0; j < maxdim-1; ++j){
                if (cols>rows){
                    board[rows-1][0]='.';
                    board[rows-2][0]='.';
                    board[rows-1][1]='.';
                    board[rows-2][1]='.';
                    for (int l=0; l<j;l++){
                        board[rows-1][l+2]='.';
                        board[rows-2][l+2]='.';
                    }
                }
                else{
                    board[rows-1][0]='.';
                    board[rows-2][0]='.';
                    board[rows-1][1]='.';
                    board[rows-2][1]='.';
                    for (int l=0; l<j;l++){
                        board[rows-(3+l)][0]='.';
                        board[rows-(3+l)][1]='.';
                    }
                }
                legalfree.insert(2*2+2*j);
                if (freecells == 2*2+2*j && printed == 0){
                    board[rows-1][0]='c';
                    
                    for (int j = 0; j < rows; ++j){
                        
                        for (int k = 0; k < cols; ++k){
                            outfile << board[j][k];
                        }
                        outfile <<endl;
                    }
                    //outfile<<endl;
                    printed = 1;
                }
                recblock(board,legalfree,2*2+2*j,j,2,mindim,rows,freecells,cols,printed,outfile);
            }
        }
        
        /*
        set<int>::iterator iter;
        for(iter=legalfree.begin(); iter!=legalfree.end();++iter) {
            cout<< *iter << " ";
        }
        cout << endl;
        */
        // algorithm
       
        
        
        if (legalfree.find(freecells) != legalfree.end()) impossible = 0;
        if (impossible==1) outfile << "Impossible" << endl;
        //if (impossible==1) cout << "Impossible" << endl;

        /*
        else{
            for (int j=0; j<4; ++j) {
                for (int k=0; k<4; ++k) {
                    if(possibles[j]==results[k]){
                        count++;
                        card = possibles[j];
                    }
                }
            }
        }
        */
    }
    
    infile.close();
    outfile.close();
    
    return 0;
}
