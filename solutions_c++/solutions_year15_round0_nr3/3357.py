#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int table[4][4] = {{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};

int GetINT(char L){
    if (L == '1'){ return 1; };
    if (L == 'i'){ return 2; };
    if (L == 'j'){ return 3; };
    if (L == 'k'){ return 4; };
}

int Multiply(int a, int b){
    int signo = 1;
    if (a < 0){ a = abs(a); signo *= -1; };
    if (b < 0){ b = abs(b); signo *= -1; };
    int res = signo * table[a-1][b-1];
    return res;
}

bool CheckIfCorrect(const char* array,int size){
    int act = 1;
    for (int x = 0; x < size; x++){
        act = Multiply(act,GetINT(array[x]));
    }
    return act == -1;
}

void Solve(){
    int L,X; cin>>L>>X;
    string read; cin>>read;
    string read2 = read;
    for (int y = 1; y < X; y++){ read += read2; };
    const char* array = read.c_str();
    if (CheckIfCorrect(array,read.length())) {
        int ant = 1;
        bool yes = false;
        int size = L * X;
        for (int y = 0; y < size - 2; y++) {
            ant = Multiply(ant, GetINT(array[y]));
            if (ant == 2) {
                int ant2 = 1;
                for (int w = y + 1; w < size - 1; w++) {
                    ant2 = Multiply(ant2, GetINT(array[w]));
                    if (ant2 == 3) {
                        int ant3 = 1;
                        for (int z = w + 1; z < size; z++) {
                            ant3 = Multiply(ant3, GetINT(array[z]));
                        }
                        if (ant3 == 4) {
                            cout << "YES" << endl;
                            yes = true;
                        }
                    }
                    if (yes) { break; };
                }
            }
            if (yes) { break; };
        }
        if (!yes) {
            cout << "NO" << endl;
        }
    }else{
        cout<<"NO"<<endl;
    }
}

int main() {
    freopen("C-small-attempt5.in","r",stdin);
    freopen("dijkstra.out","w",stdout);

    int cases; cin>>cases;
    for (int x = 0; x < cases; x++){
        cout<<"Case #"<<x+1<<": ";
        Solve();
    }
    return 0;
}