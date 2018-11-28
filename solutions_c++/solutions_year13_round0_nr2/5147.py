#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int isPossible(int **, int, int);

int main() {
    string inputFile, line;
    const char * iF;
    ifstream input;
    ofstream output;
    int ** yard;
    int cases, rows, columns;
    
    cout << "Enter Input File: ";
    getline(cin, inputFile);
    iF = inputFile.c_str();
    input.open(iF);
    output.open("Lawnmower_Output_large.txt");
    if (!input.is_open()) {
        while (!input.is_open()) {
            cout << "Failed to open input file\n";
            input.open(iF);
        }
    }
    cout << "Input File Open\n";
    if (!output.is_open()) {
        while (!output.is_open()) {
            cout << "Failed to open output file\n";
            output.open("Lawnmower_Output.txt");
        }
    }
    cout << "Output File Open\n";
    getline(input, line);
    cases = atoi(line.c_str());
    for (int c = 1; c <= cases; c++) {
        input >> rows;
        input >> columns;
        yard = (int **)malloc(rows * sizeof(int *));
        for (int i = 0; i < rows; i++) {
            yard[i] = (int *)malloc(columns * sizeof(int));
            for (int j = 0; j < columns; j++) {
                input >> yard[i][j];
            }
        }
        cout << "made yard\n";
        fflush(stdout);
        if (isPossible(yard, rows, columns)) {
            output << "Case #" << c << ": YES";
        } else {
            output << "Case #" << c << ": NO";
        }
        if (c < cases)
            output << "\n";
        cout << "freeing\n";
        fflush(stdout);
        for (int i = 0; i < rows; i++)
            free(yard[i]);
        free(yard);
        cout << "freed\n";
        fflush(stdout);
    }
    input.close();
    output.close();
    return 0;
}

int rowLonger(int ** yard, int row, int columns, int value) {
    for (int i = 0; i < columns; i++) {
        if (yard[row][i] > value)
           return 1;
    }
    return 0;
}

int columnLonger(int ** yard, int column, int rows, int value) {
    for (int i = 0; i < rows; i++) {
        if (yard[i][column] > value)
           return 1;
    }
    return 0;
}

int isPossible(int ** yard, int rows, int columns) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            if (rowLonger(yard, i, columns, yard[i][j]) && columnLonger(yard, j, rows, yard[i][j]))
               return 0;
        }
    }
    return 1;
}
        
               
