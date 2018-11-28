#include<iostream>
#include <fstream>

using namespace std;

int main() {
    int T, caso=0, N, M, mat[100][100], opciones;
    bool lad1,lad2;
    string pos[2];
    pos[0]="YES";
    pos[1]="NO";
    ofstream myfile;
    ifstream myReadFile;
    myReadFile.open("B-large.in");
    myfile.open ("Boutput.txt");
    myReadFile>>T;
    while(T--) {
        opciones=0;
        myReadFile>>N>>M;
        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                myReadFile>>mat[i][j];
            }
        }
        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                lad1=true;
                lad2=true;
                for(int k=0; k<N; k++) {
                    if(mat[i][j]<mat[k][j]) {
                        lad1=false;
                    }
                }
                for(int k=0; k<M; k++) {
                    if(mat[i][j]<mat[i][k]) {
                        lad2=false;
                    }
                }
                if(!lad1&&!lad2) {
                    i=N;
                    j=M;
                    opciones=1;
                }
            }
        }
        caso++;
        myfile<<"Case #"<<caso<<": "<<pos[opciones]<<endl;
    }
    myfile.close();
    return 0;
}
