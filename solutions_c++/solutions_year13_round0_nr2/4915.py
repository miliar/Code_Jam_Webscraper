#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int tCase;
int currCase;
vector<vector<int> > lawn;
int lawnRow, lawnCol;
ifstream fin;

void globInit(char** argv);
void input();
void dump();
void clean();
bool check();
bool checkVert(int row, int col);
bool checkHoriz(int row, int col);
int main(int argc, char** argv){
    globInit(argv);
    for(currCase = 0; currCase < tCase; currCase ++){
        input();
        //cerr << "case: " << currCase+1 << endl;
        //dump();
        check();
        clean();
    }
}
bool check(){
    for(int row = 0; row < lawnRow; row ++){
        for(int col = 0; col < lawnCol; col ++){
            //cerr <<"row: "<< row << endl;
            if(checkVert(row, col) || checkHoriz(row, col)){

            }else{
                cout << "Case #" << currCase + 1 <<": NO" << endl;//" row: " << row << " col: " << col <<endl;;
                return false;
            }
        }
    }
    cout << "Case #" << currCase + 1 << ": YES" << endl;;
    return true;
}

bool checkVert(int row, int col){
    bool goodUp = true;
    bool goodDown = true;
    for(int rowUp = row - 1; rowUp >= 0; rowUp --){
        if(lawn[rowUp][col] > lawn[row][col]){
            goodUp = false;

            break;
        }
    }
    for(int rowDown = row + 1; rowDown < lawnRow; rowDown ++){
        if(lawn[rowDown][col] > lawn[row][col]){
            goodDown = false;
            break;
        }
    }
    return goodUp && goodDown;
}
bool checkHoriz(int row, int col){
    bool goodLeft = true;
    bool goodRight = true;;
    for(int colLeft = col - 1; colLeft >= 0; colLeft --){
        if(lawn[row][colLeft] > lawn[row][col]){
            goodLeft = false;
            break;
        }
    }
    for(int colRight = col + 1; colRight < lawnCol; colRight ++){
        if(lawn[row][colRight] > lawn[row][col]){
            goodRight = false;
            break;
        }
    }
    return goodLeft && goodRight;
}
void globInit(char** argv){
    fin.open(argv[1]);
    fin >> tCase;
}
void input(){
    fin >> lawnRow >> lawnCol;
    for(int row = 0; row < lawnRow; row ++){
        vector<int> lawnStrip;
        int temp;
        for(int col = 0; col < lawnCol; col ++){
            fin >> temp;
            lawnStrip.push_back(temp);
        }
        lawn.push_back(lawnStrip);
    }
}
void dump(){
    for(int row = 0; row < lawn.size(); row ++){
        for(int col = 0; col < lawn[row].size(); col ++){
            cout << lawn[row][col];
        }
        cout << endl;
    }
}
void clean(){
    lawn.clear();
}
