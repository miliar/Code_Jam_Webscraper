#include <iostream>
#include <fstream>
#include <vector>
#include <map>
using namespace std;

int findMin(vector< vector<int> > grid){
    int minValue = grid[0][0];
    for(int i = 0; i < grid.size(); i++){
        for(int j = 0; j < grid[i].size(); j++) minValue = min(minValue,grid[i][j]);
    }
    return minValue;
}

int findRow(vector< vector<int> > grid, int value){
    map<int,int> count;
    for(int i = 0; i < grid.size(); i++){
        count[value] = 0;
        for(int j = 0; j < grid[i].size(); j++) count[grid[i][j]]++;
        if(count[value] == grid[i].size()) return i;
    }
    return -1;
}

int findCol(vector< vector<int> > grid, int value){
    map<int,int> count;
    for(int i = 0; i < grid[0].size(); i++){
        count[value] = 0;
        for(int j = 0; j < grid.size(); j++) count[grid[j][i]]++;
        if(count[value] == grid.size()) return i;
    }
    return -1;
}


int main(){
    ifstream inputFile("A-large.in");
    ofstream outputFile("googleCodeJamOUTPUTlarge.txt");
    int numExamples;
    inputFile >> numExamples;
    for(int i = 0; i < numExamples; i++){
        int N,M;
        inputFile >> N;
        inputFile >> M;
        vector< vector<int> > grid;
        for(int j = 0; j < N; j++){
            vector<int> tempVec;
            for(int k = 0; k < M; k++){
                int inputValue;
                inputFile >> inputValue;
                tempVec.push_back(inputValue);
            }
            grid.push_back(tempVec);
        }
        
        while(grid.size() > 0 && grid[0].size() > 0){
            int minHeight = findMin(grid);
            int row = findRow(grid,minHeight);
            int col = findCol(grid,minHeight);
            
            if(row != -1){
                //remove the row
                grid.erase(grid.begin() + row);
            }
            
            if(col != -1){
                //remove the column
                for(int j = 0; j < grid.size(); j++) grid[j].erase(grid[j].begin() + col);
            }
            
            if(row == -1 && col == -1) break;
        }
        
        
        if(grid.size() > 0 && grid[0].size() > 0){
            outputFile << "Case #" << i+1 << ": NO" << endl;
        } else{
            outputFile << "Case #" << i+1 << ": YES" << endl;
        }
    }
    return 0;
}
