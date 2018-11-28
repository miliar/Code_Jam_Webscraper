#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <sstream>

void resetBoard(char board[][100]) {
    for(int i=0; i < 10; i++) {
        for(int j=0; j < 10; j++) {
            board[i][j] = 0;
        }
    }
}

void resetBoard(int board[][100]) {
    for(int i=0; i < 10; i++) {
        for(int j=0; j < 10; j++) {
            board[i][j] = 0;
        }
    }
}

std::vector<std::string> split( const std::string &s, char delim ) {
    std::vector<std::string> elems;
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

int main(int argc, char* argv[]) {

    std::ifstream myFile(argv[1]);
    std::ofstream outFile("out.txt");
    std::string line;
    std::getline(myFile,line);
    int cases = atoi(line.c_str());
    int board[100][100];
    char ok[100][100];
    for(int c=1; c <= cases; c++) {
        resetBoard(board);
        resetBoard(ok);
        std::getline(myFile,line);
        std::vector<std::string> sizeLawn = split(line,' ');
        int m = atoi(sizeLawn.at(0).c_str());
        int n = atoi(sizeLawn.at(1).c_str());
        for(int i=0; i < m; i++) {
            std::getline(myFile,line);
            std::vector<std::string> row = split(line,' ');
            for(int j=0; j < row.size(); j++) {
                board[i][j] = atoi( row.at(j).c_str() );
            }

        }
        bool possible = true;
        bool rowWrong;
        bool colWrong;
        for(int i=0; i < m && possible; i++) {
            for(int j=0; j < n && possible; j++) {

                rowWrong = false;
                colWrong = false;
                
                for(int k=0; k < m; k++) {
                    if( board[k][j] > board[i][j] ) { rowWrong = true;

                    }
                }
                
                for(int k=0; k < n;  k++) {
                    if( board[i][k] > board[i][j] ) { colWrong = true;
                    }
                }
                
                if( rowWrong && colWrong ) {
                    possible = false;
                }
            }
        }

        
        if( possible ) {
            outFile << "Case #" << c << ": YES\n";
        } else {
            outFile << "Case #" << c << ": NO\n";
        }
        
    }

    myFile.close();
    outFile.close();

}
