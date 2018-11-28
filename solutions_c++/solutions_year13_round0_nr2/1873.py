#include<vector>
#include<fstream>
#include<assert.h>

using namespace std;

void parseBoard(vector<vector<int> > &board, ifstream &infile){
    int N = (int)board.size();
    int M = (int)board[0].size();
    for(int i=0; i<N; ++i){
        for(int j=0; j<M; ++j){
            infile >> board[i][j];
        }
    }
}

bool scanHor(const vector<vector<int> > &board, int r, int c){
    int N = (int)board.size();
    //int M = (int)board[0].size();
    // UP
    int i=r-1, j=c, cur = board[r][c];
    while(i>=0){
        if(board[i][j]>cur) return false;
        --i;
    }
    i= r+1;
    while(i<N){
        if(board[i][j]>cur) return false;
        ++i;
    }
    return true;
}

bool scanVer(const vector<vector<int> > &board, int r, int c){
    //int N = (int)board.size();
    int M = (int)board[0].size();
    // UP
    int i=r, j=c-1, cur = board[r][c];
    while(j>=0){
        if(board[i][j]>cur) return false;
        --j;
    }
    j=c+1;
    while(j<M){
        if(board[i][j]>cur) return false;
        ++j;
    }
    return true;
}

bool checkValid(const vector<vector<int> > &board, int r, int c){
    if(scanHor(board, r, c)||scanVer(board, r, c)) return true;
    return false;
}

bool solve(const vector<vector<int> > &board){
    assert(board.size()>0 && board[0].size()>0);
    int N = (int)board.size();
    int M = (int)board[0].size();
    if(N==1 || M==1) return true;

    for(int i=0; i<N; ++i){
        for(int j=0; j<M; ++j){
            if(!checkValid(board, i, j)) return false;
        }
    }
    return true;
}

int main(){
    //ifstream infile("test.txt");
    //ofstream outfile("out.txt");
    ifstream infile("B-large.in");
    ofstream outfile("B-large.out");
    int T;
    infile >> T;
    for(int i=0; i<T; ++i){
        int N, M;
        infile >> N >> M;
        vector<vector<int> > board(N, vector<int>(M, 0));
        parseBoard(board, infile);
        bool result = solve(board);
        outfile << "Case #" << i+1 << ": ";
        if(result)
            outfile << "YES";
        else
            outfile << "NO";
        outfile << endl;
    }
    infile.close();
    outfile.close();
    return 0;
}
