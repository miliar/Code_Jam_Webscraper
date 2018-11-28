#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

struct cell{
    int height;
    bool visit;
};

bool scan(vector<vector<cell*> > grid){
    bool con = true;
    for(int i = 0; i < grid.size(); i++){
        for(int j = 0; j < grid[0].size(); j++){
            if(grid[i][j]->visit){
                continue;
            }
            bool row = true;
            bool col = true;
            for(int k = 0; k < grid.size(); k++){
                if(i == k){
                    continue;
                }
                //cout << grid[i][j] << " " << grid[k][j] << " HAI" << endl;
                if(grid[i][j]->height < grid[k][j]->height){
                    col = false;
                }
            }
            for(int k = 0; k < grid[0].size(); k++){
                if(j == k){
                    continue;
                }
                //cout << grid[i][j] << " " << grid[i][k] << " HAI2" << endl;
                if(grid[i][j]->height < grid[i][k]->height){
                    row = false;
                }
            }
            if(col){
                for(int k = 0; k < grid.size(); k++){
                    if(grid[i][j]->height == grid[k][j]->height){
                        grid[k][j]->visit = true;
                    }
                }
            }
            if(row){
                for(int k = 0; k < grid[0].size(); k++){
                    if(grid[i][j]->height == grid[i][k]->height){
                        grid[i][k]->visit = true;
                    }
                }
            }
            if(!(row || col)){
                con = false;
                return con;
            }
        }
    }
    return con;
}

int main(){
    ofstream fout ("lawnmower.out");
    ifstream fin ("lawnmower.in");
    int N;
    fin >> N;
    for(int i = 0; i < N; i++){
        int temp1, temp2;
        fin >> temp1 >>temp2;
        vector<vector<cell*> > grid;
        for(int j = 0; j < temp1; j++){
            vector<cell*> temp3;
            for(int k = 0; k < temp2; k++){
                int temp4;
                fin >> temp4;
                cell* temp5 = new cell;
                temp5->visit = false;
                temp5->height = temp4;
                temp3.push_back(temp5);
            }
            grid.push_back(temp3);
        }
        if(scan(grid)){
            fout << "Case #" << (i + 1) << ": YES" << endl;
        } else{
            fout << "Case #" << (i + 1) << ": NO" << endl;
        }
    }
    //system("PAUSE");
}
