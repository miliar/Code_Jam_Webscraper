#include <fstream>
#include <vector>
#include <iostream>

using namespace std;

void solve_one(int caseNo);
bool check_card(int y, int guess, int temp, vector<int>& row);

ifstream fin("A-small-attempt0.in");
ofstream fout("magicout.txt");

int main(int argc, char* argv[]){
    int t;
    fin >> t;
    for(int i = 0; i < t; i++){
        solve_one(i + 1);
    }
}

void solve_one(int caseNo){
    vector<int> row;
    int out = 0;
    int guess;
    fin >> guess;
    
    //read in the first guess
    for(int y = 1; y <= 4; y++){
        for(int x = 1; x <= 4; x++){
            int temp;
            fin >> temp;
            if(y == guess){
                row.push_back(temp);
            }
        }
    }
    
    //read in the second guess and compare it for duplicates in the guess row
    fin >> guess;
    for(int y = 1; y <= 4; y++){
        for(int x = 1; x <= 4; x++){
            int temp;
            fin >> temp;
            if(check_card(y,guess,temp,row)){
                if(out) out = -1;
                else out = temp;
            }
        }
    }

    //output
    fout << "Case #" << caseNo << ": ";
    if(!out) fout << "Volunteer cheated!";
    else if(out == -1) fout << "Bad magician!";
    else fout << out;
    fout << '\n';
    return;
}

bool check_card(int y, int guess, int temp, vector<int>& row){
    if(y != guess){
        return false;
    }else{
        for(int i = 0; i < 4; i++){
            if(row[i] == temp) return true;
        }
        return false;
    }
}
