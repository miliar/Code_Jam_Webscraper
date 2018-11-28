#include <iostream>
#include <fstream>

using namespace std;
ifstream in;
ofstream out;
int m,n;
int board[100][100];
int maxRow[100];
int maxColumn[100];

void read(){
    in >> n >> m;
    for(int i=0; i<n; i++){
        for(int j = 0; j < m; j++){
            in >> board[i][j];
        }
    }
}

int solve(){
    for(int i = 0; i<n; i++){
        maxRow[i]=0;
        for(int j = 0; j<m; j++){
            if(board[i][j]>maxRow[i]){
                maxRow[i]=board[i][j];
            }
        }
    }
    for(int j = 0; j<m; j++){
        maxColumn[j]=0;
        for(int i = 0; i<n; i++){
            if(board[i][j]>maxColumn[j]){
                maxColumn[j]=board[i][j];
            }
        }
    }
    for(int i = 0; i<n; i++){
        for(int j = 0; j<m; j++){
            if(board[i][j]<maxRow[i] && board[i][j]<maxColumn[j]){
                return 2;
            }
        }
    }
    return 1;
}

void print(int caseNumber, int solutionNumber){
    out << "Case #" << caseNumber << ": ";
    if(solutionNumber == 1){
        out << "YES" << endl;
    }
    if(solutionNumber == 2){
        out << "NO" << endl;
    }
}

int main()
{
    out.open("out.txt");
    in.open("B-large.in");
    int T;
    in >> T;
    for(int i=1; i<=T; i++){
        read();
        print(i,solve());
    }
    out.close();
    in.close();
    return 0;
}
