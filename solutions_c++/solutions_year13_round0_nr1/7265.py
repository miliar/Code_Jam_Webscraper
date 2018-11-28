#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

enum status {
    XWON,   // "X won"
    OWON,   // "O won"
    DRAW,   // "Draw"
    INCOMPLETE
};

void print(char field[][4]) {
    for (int i = 0; i < 4; ++i) {
        for (int k = 0; k < 4; ++k) {
            cout << field[i][k];
        }
        cout << endl;
    }
}

void read(char field[][4], ifstream& in) {
    string line;

    for (int row = 0; row < 4; ++row) {
        getline(in, line);
        for (int col = 0; col < 4; ++col) {
            field[row][col] = line[col];
        }
    }

    // skip empty line
    getline(in, line);
}

status statusOf(char array[4]) {
    int countX = 0;
    int countO = 0;
    int countT = 0;
    int countEmpty = 0;

    for (int i = 0; i < 4; ++i) {
        if (array[i] == 'X') {
            ++countX;
        } else if (array[i] == 'O') {
            ++countO;
        } else if (array[i] == 'T') {
            ++countT;
        } else if (array[i] == '.') {
            ++countEmpty;
        } else {
            std::cout << "unexpected field value: " << array[i] << "\n";
        }
    }

    if (countEmpty > 0) {
        return INCOMPLETE;
    } else if ((countX + countT) == 4) {
        return XWON;
    } else if ((countO + countT) == 4) {
        return OWON;
    } else {
        return DRAW;
    }
}

status statusRow(int row, char field[][4]) {
    return statusOf(field[row]);
}

status statusCol(int col, char field[][4]) {
    char array[4];
    for (int i = 0; i < 4; ++i) {
        array[i] = field[i][col];
    }

    return statusOf(array);
}

status statusUpwardDiagonal(char field[][4]) {
    char diagonal[4];
    for (int i = 0; i < 4; ++i) {
        diagonal[i] = field[3-i][i];
    }

    return statusOf(diagonal);
}

status statusDownwardDiagonal(char field[][4]) {
    char diagonal[4];
    for (int i = 0; i < 4; ++i) {
        diagonal[i] = field[i][i];
    }

    return statusOf(diagonal);
}

string solve(char field[][4]) {
    string solution = "";
    int row = 0;
    int col = 0;
    int rowsDraw = 0;

    while (solution.empty() && row < 4) {
        switch (statusRow(row, field)) {
        case XWON :
            solution = "X won";
            break;
        case OWON :
            solution = "O won";
            break;
        case DRAW :
            ++rowsDraw;
            break;
        default :
            /*ignore*/ ;
            break;
        }

        ++row;
    }

    while (solution.empty() && col < 4) {
        switch (statusCol(col, field)) {
        case XWON :
            solution = "X won";
            break;
        case OWON :
            solution = "O won";
            break;
        default :
            /*ignore*/ ;
            break;
        }

        ++col;
    }

    if (solution.empty()) {
        switch (statusUpwardDiagonal(field)) {
        case XWON :
            solution = "X won";
            break;
        case OWON :
            solution = "O won";
            break;
        default :
            /*ignore*/ ;
            break;
        }
    }

    if (solution.empty()) {
        switch (statusDownwardDiagonal(field)) {
        case XWON :
            solution = "X won";
            break;
        case OWON :
            solution = "O won";
            break;
        default :
            /*ignore*/ ;
            break;
        }
    }

    if (solution.empty()) {
        if (rowsDraw == 4) {
            solution = "Draw";
        } else {
            solution = "Game has not completed";
        }
    }

    return solution;
}

int main()
{
    ifstream inStream("../A-large.in");
//    ostream& outStream = cout;
    ofstream outStream("../A-large.out");

    string line;
    getline(inStream, line);
    int numCases = atoi(line.c_str());

    for (int i = 1; i <= numCases; ++i) {
        char field[4][4];
        read(field, inStream);
        string solution = solve(field);
        outStream << "Case #" << i << ": " << solution << endl;
    }

    inStream.close();
    outStream.close();

    return 0;
}
