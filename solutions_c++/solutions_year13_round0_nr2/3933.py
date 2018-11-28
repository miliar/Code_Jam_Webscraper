/*
ID: zachary11
PROG: calfflac
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <set>

using namespace std;

template <typename Type>
string toString(Type t){
	stringstream ss;
        string s;
	ss << t;
        ss >> s;
        return s;
}

void columnLimit( vector<vector<int> > &field, int limit, int column){
    for(int i=0; i<field.size(); i++){
        if(field[i][column] > limit) field[i][column] = limit;
    }
}

int columnMax(vector<vector<int> > field, int column){
    int max = 0;
    for(int i=0; i<field.size(); i++){
        if(field[i][column] > max) max = field[i][column];
    }
    return max;
}

int rowMax(vector<int> row){
    int max = 0;
    for(int i=0; i<row.size(); i++){
        if(row[i] > max) max = row[i];
    }
    return max;
}

vector<vector<int> > mow(vector<vector<int> > model){
    vector<vector<int> > myField;
    int width = model[0].size();
    for(int row=0; row<model.size(); row++){
        int max = rowMax(model[row]);
        vector<int> myRow;
        for(int i=0; i<width; i++) myRow.push_back(max);
        myField.push_back(myRow);
    }
    for(int i=0; i<width; i++){
        columnLimit( myField, columnMax(model, i), i);
    }
    return myField;
}

bool fieldEquals(vector<vector<int> > a, vector<vector<int> > b){
    for(int x=0; x<a.size(); x++){
        for(int y=0; y<a[0].size(); y++){
            //cout << a[x][y] << " " << b[x][y] << endl;
            if(a[x][y] != b[x][y]) return false;
            //cout << b[x][y];
        }
        //cout << endl;
    }
    return true;
}

string mowFull(vector<vector<int> > model){
    if(fieldEquals(model, mow(model))) return "YES";
    else return "NO";
}

int main() {
    ofstream fout("codeJam.out");
    ifstream fin("codeJam.in");
    int caseNumber=0;
    fin >> caseNumber;
    for(int i=1; i<=caseNumber; i++){
        
        int x,y;
        fin >> x >> y;
        vector<vector<int> > field;
        for(int j=0; j<x; j++){
            vector<int> row;
            for(int k=0; k<y; k++){
                int element;
                fin >> element;
                row.push_back(element);
            }
            field.push_back(row);    
        }
        
        string solution = mowFull(field);
        fout << "Case #" << i << ": " << solution << endl;
        cout << "Case #" << i << ": " << solution << endl;
    }
    
    return 0;
}
