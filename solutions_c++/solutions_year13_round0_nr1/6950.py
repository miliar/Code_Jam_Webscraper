#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define fr(i, n) for(i = 0; i < (n); i++)
#define fr2(i, s, n) for(i = (s); i < (n); i++)


static bool hasWon(int sum) {

    if (sum == 1) {
        cout << "O won";
        return true;
    } else if (sum == 2) {
        cout << "X won";
        return true;
    }
    
    return false;
}

static void solver(int t, const vector< vector<int> > &m) {
    cout<< "Case #" << t+1 << ": ";
    int sum = 1;
    bool complete = true;

    int i, j;
    
    fr(i, 4) {
        sum = 3;
        fr(j, 4) {
            if (m[i][j] == 0) {
                complete = false;
            }
            
            sum &=m[i][j];
        }
        
        if (hasWon(sum)) return;
    }
    
    // check columns
    fr(i, 4) {
        sum = 3;
        fr(j, 4) {
            sum &=m[j][i];
        }
        
        if (hasWon(sum)) return;
    }
    
    //check diagonal from top left to buttom right
    sum = 3;
    fr(i, 4) {
        sum &= m[i][i];
    }
    if (hasWon(sum)) return;
    
    //check other  diagonal
    sum = 3;
    fr(i, 4) {
        sum &= m[i][3-i];
    }
    if (hasWon(sum)) return;
    
    if (!complete) {
        cout << "Game has not completed";
        return;
    }
    
    cout << "Draw";
}


static int encode(char a) {
    return (a == 'O') ? 1 : (a == 'X') ? 2 : (a == 'T') ? 3 : 0;
}

/*
static void printMatrix(const vector< vector<int> > &m) {
    cout << endl;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}
*/

int main(int argc, const char * argv[])
{
    //ifstream fin("input.txt");
    //ofstream fout("output.txt");
    
    int T = 0;
    cin >> T;
    char a;
    char b;
    char c;
    char d;
    int t, i;

    fr(t, T) {
        vector<vector<int>> matrix(4, vector<int>(4, 0));
        fr(i, 4) {
            cin >> a >> b>> c >> d;
            
            matrix[i][0] = encode(a);
            matrix[i][1] = encode(b);
            matrix[i][2] = encode(c);
            matrix[i][3] = encode(d);
        }
        //printMatrix(matrix);
        solver(t, matrix);
        cout << endl;
    }
    
    return 0;
}

