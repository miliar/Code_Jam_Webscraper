#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cmath>
using namespace std;

int main() {

    ifstream ifile("C-small-attempt0.in");
    ofstream ofile("example.txt");
    if (ifile.is_open()) {
            int test;
            ifile >> test;
            for(int k = 0; k < test;k++){
                int arrA[7] = {1,4,9,121,484,10201,1002001};
                int a, b;
                ifile >> a;
                ifile >> b;
                int sum = 0;
                for(int i = 0; i < 7;i++){
                        if(arrA[i]>=a && arrA[i]<=b)
                            sum++;
                }
                ofile << "Case #" << k+1 << ": " << sum << endl;
            }

            ifile.close();
    }
    return 0;
}

