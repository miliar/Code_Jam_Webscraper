#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <cmath>
#include <vector>
#include <algorithm>
#include <time.h>
#define MAX 100
#define test(a) cout << "TEST " << a << endl;
#define go(a,b) for(int a=0; a<b; a++)
#define case(a) fout << "Case #"<< a << ": " <<

using namespace std;
ofstream fout ("output.txt");
ifstream fin ("input.txt");

int main()
{
    int a, c, f, g;
    char e;
    fin >> a;
    go(b,a){
        f=0;
        g=0;
        fin >> c;
        go(d,c+1){
            fin >> e;
            f+=e-'0'-1;
            if(f==-1){
                f++;
                g++;
            }
        }
        case(b+1) g << endl;

    }

}

