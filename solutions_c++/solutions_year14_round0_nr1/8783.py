#include <iostream>
#include <sstream>
#include "stdio.h"
using namespace std;



int main(){

int n, answer1, answer2, resn, cnt, arr1[4][4], arr2[4][4];
string res;

cin >> n;

for (int i=0;i<n;i++){

    cin >> answer1;
    for(int r=0;r<4;r++)
        for(int c=0;c<4;c++)
            cin >> arr1[r][c];

    cin >> answer2;
    for(int r=0;r<4;r++)
        for(int c=0;c<4;c++)
            cin >> arr2[r][c];

    cnt = 0;
    for(int a=0;a<4;a++){
        for(int b=0;b<4;b++){
            //cout << arr1[answer1-1][a] << " " << arr2[answer2-1][b] << endl;
            if (arr1[answer1-1][a] == arr2[answer2-1][b]){
                cnt++;
                resn = arr1[answer1-1][a];
                ostringstream convert;
                convert << resn;
                res = convert.str();
            }
        }
    }


    if (cnt == 0)
        res = "Volunteer cheated!";
    else if (cnt > 1)
        res = "Bad magician!";

    cout << "Case #" << i+1 << ": " << res << endl;



}





}
