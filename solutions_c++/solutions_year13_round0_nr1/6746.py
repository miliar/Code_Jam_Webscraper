#include <iostream>
#include <fstream>

using namespace std;

unsigned int n;
char board[4][4];
int x_row[4];
int x_col[4];
int x_diag[2];
int o_row[4];
int o_col[4];
int o_diag[2];

int main(int argc, char *argv[]) {
    //cout << argv[0] << " " << argv[1] <<  " " << argv[2] << endl;

    ifstream fin (argv[1]);
    ofstream fout (argv[2]);

    fin >> n;

    for(unsigned int i=0; i<n; i++) {
        //cout << "NEW CASE " << i << endl;
        unsigned int empty_cell = 0;

        for(unsigned int j=0; j<16; j++) {
            //Get the board
            fin >> board[j/4][j%4];

            if(board[j/4][j%4] == 'X' || board[j/4][j%4] == 'T') {
                x_row[j/4] += 1;
                x_col[j%4] += 1;
                if(j/4 == j%4) {
                    x_diag[0] += 1;
                }
                
                if(j/4 == 4 - j%4 - 1) {
                    x_diag[1] += 1;
                }
            }
            
            if(board[j/4][j%4] == 'O' || board[j/4][j%4] == 'T') {
                o_row[j/4] += 1;
                o_col[j%4] += 1;
                if(j/4 == j%4) {
                    o_diag[0] += 1;
                }
                
                if(j/4 == 4 - j%4 - 1) {
                    o_diag[1] += 1;
                }
            }

            if(board[j/4][j%4] == '.') {
                empty_cell = 1;
            }
        }

        unsigned int win_x = 0;
        unsigned int win_o = 0;

        if(x_diag[0] == 4 || x_diag[1] == 4) {
           win_x = 1; 
        }
        
        if(o_diag[0] == 4 || o_diag[1] == 4) {
           win_o = 1; 
        }

        //cout << x_diag << endl;
        //cout << o_diag << endl;

        for(unsigned int j=0; j<4 && !win_x && !win_o; j++) {
            if(x_row[j] == 4 || x_col[j] == 4) {
                win_x = 1;
            }
            if(o_row[j] == 4 || o_col[j] == 4) {
                win_o = 1;
            }

            //cout << x_row[j] << " " << x_col[j] << endl;
            //cout << o_row[j] << " " << o_col[j] << endl;
        }

        if(!win_x && !win_o && empty_cell) {
            fout << "Case #" << i+1 << ": Game has not completed" << endl;
        }
        
        if(!win_x && !win_o && !empty_cell) {
            fout << "Case #" << i+1 << ": Draw" << endl;
        }
        
        
        if(win_x) {
            fout << "Case #" << i+1 << ": X won" << endl;
        }
        
        if(win_o) {
            fout << "Case #" << i+1 << ": O won" << endl;
        }

        
        x_diag[0] = 0;
        o_diag[0] = 0;
        x_diag[1] = 0;
        o_diag[1] = 0;

        for(unsigned int j=0; j<4; j++) {
            x_row[j] = 0;
            x_col[j] = 0;
            o_row[j] = 0;
            o_col[j] = 0;
        }
    }

    /*unsigned int * positions = new unsigned int[n];

    for(unsigned int i=0; i<n; i++) {
        positions[i] = 0;
    }
    
    for(unsigned int col=0; col<n; col++) {
        process_cell(0, col);
    }

    unsigned int l = m < 3 ? m : 3;

    for(unsigned int i=0; i<l; i++) {
        for(unsigned int col=0; col<n; col++) {
            if(col > 0) {
                fout << " ";
            }
            fout << gpos[i][col]+1;
        }
        fout << "\n";
    }
    fout << m << "\n";*/

    return 0;
}
