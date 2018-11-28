#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;

int main(int argc, char *argv[]){
    int n;
    char a[4];
    ifstream fin(argv[1]);
    ofstream fout("output.txt");
    fin.getline(a,4);
    n = atoi(a);
    for(int test=1;test<=n;test++){
        char sstr[1500];
        fin.getline(sstr,1500);
        char *st;
        st = strtok(sstr," ");
        int s = atoi(st);
        char string[s+3];
        st = strtok(NULL," ");
        strcpy(string,st);
        int needed = 0,standing = string[0] - 48;
        for(int l = 1;string[l]!='\0';l++){
            if(standing < l){
                needed += (l - standing);
                standing += (l-standing);
            }
            standing += string[l] - 48;
        }
        fout<<"Case #"<<test<<": "<<needed;
        if(test!=n) fout<<endl;
    }
    return 0;
}