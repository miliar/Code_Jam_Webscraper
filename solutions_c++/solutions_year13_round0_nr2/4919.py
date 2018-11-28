#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

int check(vector<int> vec, int num) {
    
    vector<int>::iterator it;
    for (it = vec.begin(); it < vec.end(); it++) {
        if ((*it) > num)
            return 0;
    }
    return 1;
}


int extract(int* array[], int rows, int cols, int i, int j) {
    
    vector<int> row;
    for (int c = 0; c < cols; c++) {
        row.push_back(array[i][c]);
    }
    
    vector<int> col;
    for (int r = 0; r < rows; r++) {
        col.push_back(array[r][j]);
    }
    
    return (check(row, array[i][j]) || check(col, array[i][j]));
    
}

int process(int* array[], int rows, int cols) {
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (!extract(array, rows, cols, r, c)) return 0;
        }
    }
    return 1;
}


int main() {
    
    ifstream myReadFile;
    myReadFile.open("B-large.in");
    
    ofstream myWriteFile;
    myWriteFile.open("output.out");
    
    int testCases;
    string buffer;
    
    
    if (myReadFile.is_open()) {
        
        getline(myReadFile , buffer);
        testCases = atoi(buffer.c_str());
        

        
        for (int i = 0; i<testCases; i++) {
            
            int rows, cols;
            
            getline(myReadFile , buffer);
            istringstream stream(buffer);
            
            stream >> rows >> cols;
            
            int* array[rows];
            for (int it = 0; it < rows; it++)
                array[it] = new int[cols];
            
            
            for (int r = 0; r < rows; r++) {
                getline(myReadFile , buffer);
                istringstream stream(buffer);
                for (int c = 0; c <cols; c++)
                    stream >> array[r][c];
            }
            
            string result;
            
            (process(array, rows, cols))? (result = "YES") : (result = "NO");
            
            myWriteFile<<"Case #"<<i+1<<": "<<result<<endl;
            
        }
    }
    myReadFile.close();
    myWriteFile.close();
    return 0;
}
