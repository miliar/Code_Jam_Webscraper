#include <iostream>
#include <vector>
#include <list>
#include <deque>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <cassert>
#include <string>

using namespace std;

const int kSize = 4;

struct TTTT {
    enum State{Blank, X, O, T};
    enum Winner{Draw, WinnerX, WinnerO, Incomplete};
    
    State board[kSize][kSize];
    int Tx,Ty; //Stores the location of 'T' on the Board
    
    TTTT():Tx(-1),Ty(-1) {
        // Do Nothing
    }

    bool ReadGameInput(){
        string line;

        for (int i = 0; i<kSize; i++) {
            getline(cin,line);
            assert(line.size() == kSize);
            for (int j = 0; j < kSize; j++) {
                //cin >> c;
                board[i][j] = GetState(line[j]);
                if(board[i][j] == T){
                    Tx = i;
                    Ty = j;
                }
            }
        }
        getline(cin,line);
        assert(line.empty());
        if(line.empty()){
            return true;
        }
        return false;
    }
    
    void UpdateBoard(State s){
        if(Tx == -1 && Ty == -1) //No T in the input
            return;
        assert(Tx >= 0 && Tx < kSize);
        assert(Ty >= 0 && Ty < kSize);
        board[Tx][Ty] = s;
    }
    
    State GetState(char c){
        State s;
        switch (c) {
            case '.': s = Blank;
                break;
            case 'O': s = O;
                break;
            case 'X': s = X;
                break;
            case 'T': s = T;
                break;
            default:
                assert(false);// Should not reach here!
                break;
        }
        return s;
    }
    
    // Return can be State:
    // X,O   -> Winner is either 'X' or 'O'
    // Blank -> Denotes that no Row can have a winner
    // T     -> Game needs to continue further
    //          Atleast one Row can have a winner
    State RowWinner(){
        
        bool RowFlags[kSize] = {true,true,true,true};
        
        for (int row = 0; row <= kSize - 1; ++row) {
            bool xflag = false;
            bool oflag = false;
            if (board[row][0] != Blank) {
                int col = 1;
                while (col <=kSize -1
                       && board[row][col-1] == board[row][col])
                {
                    col++;
                }
                if (col == kSize) {
                    //All elements in the Row are same
                    //Winner
                    return board[row][0];
                }
            }
            for (int c = 0; c<kSize; c++) {
                if(board[row][c] == X) xflag = true;
                if(board[row][c] == O) oflag = true;
            }
            if (xflag && oflag) {
                RowFlags[row] = false;
            }
        }
        
        for (int rfi = 0; rfi<kSize; rfi++) {
            if (RowFlags[rfi] == true) {
                return T;
            }
        }
        
        return Blank;
    }
    
    // Return can be State:
    // X,O   -> Winner is either 'X' or 'O'
    // Blank -> Denotes that no Columb can have a winner
    // T     -> Game needs to continue further
    //          Atleast one Column can have a winner
    State ColWinner(){
        
        bool ColFlags[kSize] = {true,true,true,true};
       
        for (int col = 0; col <= kSize - 1; ++col) {
            bool xflag = false;
            bool oflag = false;
            if (board[0][col] != Blank) {
                int row = 1;
                while (row <=kSize -1
                       && board[row-1][col] == board[row][col])
                {
                    row++;
                }
                if (row == kSize) {
                    //All elements in the Row are same
                    //Winner
                    return board[0][col];
                }
            }
            for (int r = 0; r<kSize; r++) {
                if(board[r][col] == X) xflag = true;
                if(board[r][col] == O) oflag = true;
            }
            if (xflag && oflag) {
                ColFlags[col] = false;
            }

        }
        
        for (int cfi = 0; cfi<kSize; cfi++) {
            if (ColFlags[cfi] == true) {
                return T;
            }
        }
        
        return Blank;
    }
    
    // Return can be State:
    // X,O   -> Winner is either 'X' or 'O'
    // Blank -> Denotes that no one is winner
    //          Both Diagonal are can't have winner
    // T     -> Game needs to continue further
    //          Atleast one Diagonal can have a winner
    State DiagWinner(){
       
        int left = 0, right  = kSize -1;
        int top  = 0, bottom = kSize -1;

        // Check top-left to bottom-right diagonal.
        if (board[top][left] != Blank) {
            int rowcol = 1;
            while (rowcol <= bottom &&
                   board[rowcol][rowcol] == board[top][left]) {
                rowcol++;
            }
            if (rowcol == kSize) {
                return board[top][left];
            }
        }
        
        // Check top-right to bottom-left diagonal.
        
        if (board[top][right] != Blank) {
            int i = 1;
            while (i <= kSize -1 && board[top+i][right-i] == board[top][right]) {
                i++;
            }
            if (i == kSize) {
                return board[top][right];
            }
        }
        
        bool Diag1Flag = true;
        bool Diag2Flag = true;

        bool xflag = false;
        bool oflag = false;
        
        for (int i = 0; i<kSize; i++) {
            if(board[i][i] == X) xflag = true;
            if(board[i][i] == O) oflag = true;
        }
        if (xflag && oflag) {
            Diag1Flag = false;
        }
        
        xflag = false;
        oflag = false;
        for (int i = 0; i<kSize; i++) {
            if(board[top+i][right-i] == X) xflag = true;
            if(board[top+i][right-i] == O) oflag = true;
        }
        if (xflag && oflag) {
            Diag2Flag = false;
        }
        
        if(Diag1Flag || Diag2Flag){
            //One of the diagonal is still playable
            return T;
        }
        
        return Blank;
    }

    State findWinner()
    {
        // Blank => denotes a Draw
        // O     => denotes 'O' wins
        // X     => denotes 'X' wins
        // T     => denotes game not finished
        
        State rwin = RowWinner();
        State cwin = ColWinner();
        State dwin = DiagWinner();
        
        if(rwin == X || cwin == X || dwin == X) {
            return X; //std::string("X won");
        }
        else if (rwin == O || cwin == O || dwin == O) {
            return O; // std::string("O won");
        }
        else if (rwin == Blank && cwin == Blank && dwin == Blank) {
            return Blank; //std::string("Draw");
        }
        else {
            return T; //std::string("Game has not completed");
        }
    
    }
    
};

int main(int argc, const char * argv[])
{
    
    int TestCases;
    
    cin >> TestCases;
    getchar();
    
    for (int t=1; t<=TestCases; t++) {
        
        cout << "Case #" <<t << ": ";
        TTTT ttt;
        if (ttt.ReadGameInput()){
            TTTT x(ttt);
            TTTT o(ttt);
            x.UpdateBoard(TTTT::X);
            o.UpdateBoard(TTTT::O);
            
            TTTT::State xstate = x.findWinner();
            TTTT::State ostate = o.findWinner();
            
            if (xstate == TTTT::X) {
                cout << std::string("X won") << endl;
            }
            else if (ostate == TTTT::O) {
                cout << std::string("O won") << endl;
            }
            else if (ostate == TTTT::Blank && xstate == TTTT::Blank) {
                cout << std::string("Draw") << endl;
            }
            else if (ostate == TTTT::T || xstate == TTTT::T) {
                cout << std::string("Game has not completed") << endl;
            }
            else{
                cout << "Debug Buddy o=" << ostate << " x=" <<xstate << endl;
            }
        }
        else
            assert("Read input failed");
        
    }

    // insert code here...
    //std::cout << "Hello, World!\n";
    
    return 0;
}

