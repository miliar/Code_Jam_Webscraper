#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

class Board {
public:
    Board(char* FileName);
    ~Board();
    void do_the_magic();
    int get_total(){return total;};
private:
    ifstream input;
    ofstream output;
    int trash;
    int cards1[4];
    int cards2[4];
    int answer;
    int total;
    int case_atual;
};

Board::Board(char* FileName) {
    input.open(FileName, ios::in);
    input >> total;
    output.open ("Output.txt", ios::out);
    case_atual = 1;
}

Board::~Board() {
    input.close();
    output.close();
}

void Board::do_the_magic() {
    input >> answer;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if ((i+1) == answer) {
                input >> cards1[j];
            }
            else {
                input >> trash;
            }
        }
    }
    input >> answer;
    for (int i =0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if ((i+1) == answer) {
                input >> cards2[j];
            }
            else {
                input >> trash;
            }
        }
    }

    int aux = 0;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (cards1[i] == cards2[j]) {
                answer = cards1[i];
                aux++;
            }
        }
    }
    if (aux == 0) {
        output << "Case #" << case_atual << ": Volunteer cheated!" << endl;
    }
    else if (aux == 1) {
        output << "Case #" << case_atual << ": " << answer << endl;
    }
    else if (aux > 1) {
        output << "Case #" << case_atual << ": Bad magician!" << endl;
    }
    case_atual++;
    total--;
}

int main () {
Board magic ("teste.in");
while (magic.get_total() > 0) {
    magic.do_the_magic();
}
return 0;
}
