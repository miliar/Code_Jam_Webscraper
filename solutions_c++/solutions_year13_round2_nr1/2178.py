#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <stdlib.h>
#include <math.h>
#include <iomanip>
#include <fstream>
using namespace std;

int binaryTree(vector<int>moles, int moves, int absorbed, int start){

    while(absorbed != moles.size()){
            if(start > moles.at(absorbed)){
                start += moles.at(absorbed);
                absorbed++;
            } else {
                if(start == 1){
                    return moles.size()-absorbed;
                }
                //decide which operation
                int copy = start;
                copy += start-1;
                int addPath = binaryTree(moles, moves+1, absorbed, copy);
                moles.pop_back();
                int deletePath = binaryTree(moles, moves+1, absorbed, start);
                if(addPath <= deletePath)
                    moves = addPath;
                else
                    moves = deletePath;
                break;
            }
    }
    return moves;
}

int main() {
    ifstream is;
    is.open("A-small-attempt0.in");
    ofstream os;
    os.open("answer.txt");
    int test = 0;
    is >> test;
    for(int i = 1; i <= test; i++){
        int start;
        is >> start;
        int n;
        is >> n;
        vector<int> moles;
        for(int j = 0; j < n; j++){
            int s; is >> s;
            moles.push_back(s);
        }
        sort(moles.begin(), moles.begin()+n);
        //operation begins =)
        int moves = 0;
        int absorbed = 0;
        moves = binaryTree(moles, moves, absorbed, start);
        os << "Case #" << i << ": " << moves << endl;
    }
    return 0;
}
