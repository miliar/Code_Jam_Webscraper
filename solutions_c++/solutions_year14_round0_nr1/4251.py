#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>

using namespace std;

int F[5];
int S[5];
int T;
int main(){
    fstream in,out;
    in.open("input.in",ios::in);
    out.open("output.txt",ios::out);
    in >> T;
    for(int test = 1; test <= T; ++test){
        int x; int y;
        in >> x;
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
                if(i+1 == x) in >> F[j]; else in >> y;
        in >> x;
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
                if(i+1 == x) in >> S[j]; else in >> y;
        int cc = 0;
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
                if(F[i] == S[j])
                    cc++;
        out << "Case #" << test << ": ";
        if(cc == 0)
            out << "Volunteer cheated!";

        else if(cc == 1){
          for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
                if(F[i] == S[j])
                    out << F[i];
        }

        else out << "Bad magician!";
        out << endl;

    }
}
