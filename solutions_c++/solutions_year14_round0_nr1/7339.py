#include <iostream>
#include <fstream>

using namespace std;

void compare(int case_no, int *row1, int *row2, ostream &out) {
    unsigned int equal_count = 0;
    int number = 0;
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            if(row1[i] == row2[j]) {
                equal_count++;
                number = row1[i];
            }
        }
    }
    out << "Case #" << case_no << ": ";
    if(equal_count == 0) {
        out << "Volunteer cheated!";
    } else if(equal_count > 1) {
        out << "Bad magician!";
    } else {
        out << number;
    }
}

int main(int argc, char *argv[]) {
    if(argc != 3) {
        cout << "Usage: " << argv[0] << " <input file name> <output file name>" << endl;
        return 1;
    }
    ifstream in(argv[1]);
    ofstream out(argv[2]);
    if( !in.is_open() ) {
        cout << "Unable to read the file: " << argv[1] << endl;
        return 1;
    }
    int T;
    in >> T;
    cout << "T: " << T << endl;
    for(int t = 0; t < T; t++) {
        if(t!=0 && t!=T) {
            out << endl;
        }
        int r1;
        in >> r1;
        cout << "r1: " << r1 << endl;
        int *row1 = new int[4];
        int temp;
        cout << "matrix1: " << endl;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                if(i+1 == r1) {
                    in >> row1[j];
                    cout << row1[j] << ' ';
                }
                else {
                    in >> temp;
                    cout << temp << ' ';
                }
            }
            cout << endl;
        }
        cout << endl;
        int r2;
        in >> r2;
        cout << "r2: " << r2 << endl;
        int *row2 = new int[4];
        cout << "matrix2: " << endl;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                if(i+1 == r2) {
                    in >> row2[j];
                    cout << row2[j] << ' ';
                }
                else {
                    in >> temp;
                    cout << temp << ' ';
                }
            }
            cout << endl;
        }
        compare(t+1, row1, row2, out);
        cout << endl;
    }
    return 0;
}
