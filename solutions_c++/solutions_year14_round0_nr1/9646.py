#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

int num[10][10];
int ans1[10];
int ans2[10];
int temp;

int getEqualNum(){
    int equal = 0;
    for(int i = 1;i <= 4;i++){
        for(int j = 1;j <= 4;j++){
            if(ans1[i] == ans2[j]){
                equal++;
                temp = ans1[i];
            }
        }
    }
    return equal;
}

int main(){
    ifstream input("A-small-attempt0.in");
    ofstream output;
    output.open("output.txt");
    int t,row;
    input >> t;
    for(int cas = 1;cas <= t;cas++){
        input >> row;
        for(int i = 1;i <= 4;i++){
            for(int j = 1;j <= 4;j++){
                input >> num[i][j];
            }
        }
        for(int i = 1;i <= 4;i++){
            ans1[i] = num[row][i];
        }
        input >> row;
        for(int i = 1;i <= 4;i++){
            for(int j = 1;j <= 4;j++){
                input >> num[i][j];
            }
        }
        for(int i = 1;i <= 4;i++){
            ans2[i] = num[row][i];
        }
        int equal = getEqualNum();
        output << "Case #" << cas << ": ";
        if(equal == 1){
            output << temp << endl;
        }else if(equal > 1){
            output << "Bad magician!" << endl;
        }else if(equal < 1){
            output << "Volunteer cheated!" << endl;
        }
    }
    input.close();
    output.close();
    return 0;
}
