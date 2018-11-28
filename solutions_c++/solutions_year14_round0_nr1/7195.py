#include <iostream>
#include <vector>
#include <fstream>
using namespace std;


int main()
{
    fstream f("input2.in");
    fstream o("output1.txt");
    int t;
    f >> t;
    for(int i = 1; i <= t; i++)
    {
        int s, d;
        int a[4][4];
        int b[4][4];
        f >> s;
        for(int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++){
                f >> a[j][k];
            }
        }
        f >> d;
        for(int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++){
                f >> b[j][k];
            }
        }
        int cnt = 0;
        int num;
        for(int j = 0; j < 4; j++){
            for(int k = 0; k < 4; k++){
             //   o << a[s-1][j] << " " << b[d-1][k] << endl;
                if(a[s-1][j] == b[d-1][k]){
                    num = a[s-1][j];
                    cnt++;
                }
            }
        }
        if(cnt == 1){
            o << "Case #" << i << ": " <<num << endl;
        }
        else if(cnt > 1){
            o << "Case #" << i << ": " <<"Bad magician!"<< endl;
        }
        else if(cnt == 0){
            o << "Case #" << i << ": " <<"Volunteer cheated!"<< endl;
        }
    }
    return 0;
}
