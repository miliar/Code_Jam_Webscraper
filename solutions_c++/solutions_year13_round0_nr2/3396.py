#include <iostream>
#include <string>
#include <fstream>

using namespace std;

struct Grass{
    int height;
    bool done;
    Grass(): height(0), done(false){}
};


struct Lawn{
    Grass grass[100][100];
    int n, m;

    Lawn(int numRows, int numColumns)
    : n(numRows), m(numColumns){}

    void read(ifstream& in){
        for(int row = 0; row < n; ++row){
            for(int col = 0; col < m; ++col){
                in >> grass[row][col].height;
            }
        }
    }

    bool compute(){
        int init;
        int numDone = 0;
        //checks horizontal paths
        for(int row = 0; row < n; ++row){
            init = grass[row][0].height;
            for(int col = 0; col < m; ++col){
                if(grass[row][col].height > init){
                    init = grass[row][col].height;
                }
            }
            for(int col = 0; col < m; ++col){
                if(grass[row][col].height == init){
                    grass[row][col].done = true;
                    ++numDone;
                }
            }
        }
        //checks verticals
        for(int col = 0; col < m; ++col){
            init = grass[0][col].height;
            for(int row = 0; row < n; ++row){
                if(grass[row][col].height > init){
                    init = grass[row][col].height;
                }
            }
            for(int row = 0; row < n; ++row){
                if(!grass[row][col].done 
                    && grass[row][col].height == init){
                    grass[row][col].done = true;
                    ++numDone;
                }
            }
        }
        if(numDone == n*m){
            return true;
        }
        else return false;
    }
};


int main(){
    ifstream in;
    string inputString = "B-large.in";
    in.open(inputString.c_str());
    int numCases;
    in >> numCases;
    int numRows, numCols;
    for(int i = 0; i < numCases; ++i){{
        in >> numRows >> numCols;
        Lawn test(numRows, numCols);
        test.read(in);
        if(test.compute()){
            cout << "Case #" << i+1 << ": " << "YES\n";
        }
        else cout << "Case #" << i+1 << ": " << "NO\n";
    }}
    
    in.clear();
    in.close();
    return 0;
}

