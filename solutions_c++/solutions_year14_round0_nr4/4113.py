#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cstring>
using namespace std;
int T; int N;
double A[10005];
double B[10005];

int main(){
    fstream in,out;
    in.open("input.in",ios::in);
    out.open("output.txt",ios::out);
    in >> T;
    for(int test = 1; test <= T; ++test){
        in >> N;
        for(int i = 0; i < N; ++i)
            in >> A[i];
        for(int i = 0; i < N; ++i)
            in >> B[i];
        sort(A,A+N);
        sort(B,B+N);

        int pos = N-1;
        int z = 0;
        for(int i = N-1; i >= 0; i--){
            if(A[i] > B[pos])
                ++z;
            else --pos;
        }


        pos = N-1;
        int y = 0;
        for(int i = N-1; i >= 0; i--){
            if(A[i] > B[pos]){
                ++y; --pos;
            }
            else{
                    while( A[i] < B[pos] && pos >= 0)
                        --pos;
                    if(pos >= 0){ ++y; --pos;}

            }
            if(pos < 0) break;
        }
        out << "Case #" << test << ": " << y << " " <<  z << endl;
        //for(int i = 0; i < N; ++i)cout << A[i] << " ";cout << endl;for(int i = 0; i < N; ++i)cout << B[i] << " ";cout << endl;getchar();
    }

}
