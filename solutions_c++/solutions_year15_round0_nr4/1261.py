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
    int a, x,r,c;
    fin >> a;
    go(b,a){
        fin >> x;
        fin >> r;
        fin >> c;
        if(r*c%x!=0||x-r>1||x-c>1){
            case(b+1) "RICHARD" << endl;
        }
        else{
            case(b+1) "GABRIEL" << endl;
        }

    }

}

