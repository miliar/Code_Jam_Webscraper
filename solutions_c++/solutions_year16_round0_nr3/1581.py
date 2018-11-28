//
// Created by Yuxiang LI on 09/04/16.
//

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int T;
int N,J;
vector<int> r(100);

void push(int l){
    int i = l-1;
    while(r[i] == 1)
        i--;
    r[i] = 1;
    for(int j = i+1; j < l; j++)
        r[j] = 0;
}

int main(){
    ifstream in("input.in");
    ofstream out("output.out");
    in >> T;
    for(int cases = 1; cases <= T; cases++){
        in >> N >> J;
        out << "Case #" << cases << ": " << endl;
        int l = (N-4)/2;
        for(int i = 0; i < l; i++)
            r[i] = 0;
        for(int i = 0; i < J; i++){
            for(int j = 0; j < 2; j++){
                out << 1;
                for (int t = 0; t < l; t++)
                    out << r[t];
                out << 1;
            }
            for (int j = 2; j <= 10; j++){
                long long k = j;
                long long s = 1;
                for(int t = l-1; t>=0; t--){
                    s += k*r[t];
                    k *= j;
                }
                s += k;
                out << ' ' << s;
            }
            out << endl;
            push(l);
        }
    }
    return 0;
}