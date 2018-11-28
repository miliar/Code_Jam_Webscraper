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
    int a, c, f,g, mi, h, mih;
    double n;
    double e[1000];
    fin >> a;
    go(b,a){
        fin >> c;
        go(d,c){
            fin >> f;
            e[d]=f;
        }
        mi=1000000;
        mih=0;
        for(g=1; g<mi; g++){
            h=g;
            go(d,c){
                n=ceil(e[d]/g);
                h+=n-1;
            }
            if(h<mi){
                mi=h;
                mih=g;
            }
        }
        case(b+1) mi << endl;

    }

}

