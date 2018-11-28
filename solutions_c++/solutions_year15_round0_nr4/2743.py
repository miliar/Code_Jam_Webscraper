#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>
using namespace std;
int main(){
    int t;
    int tt=1;

    ifstream fin("InputFilea.txt");
    ofstream fout("output.txt");

 fin>>t;
    int X,R,C;
    while(t--){
        fin>>X>>R>>C;
        fout<<"Case #"<<tt<<": ";
        if((R*C)%X){
            fout<<"RICHARD\n";
        }
        else{
            if(R>(X-2) && C>(X-2)){
                fout<<"GABRIEL\n";
            }
            else{
                fout<<"RICHARD\n";
            }

        }

        tt++;
    }
    fin.close();
    fout.close();
    return 0;
}

