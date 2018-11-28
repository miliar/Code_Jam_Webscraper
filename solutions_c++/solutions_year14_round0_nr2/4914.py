#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iomanip>

#define MAX 100
#define test(a) cout << "TEST " << a << endl;
#define go(a,b) for(int a=0; a<b; a++)
#define case(a) fout << "Case #"<< a << ": " <<
using namespace std;




int main()
{

    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    long double n,c,s,f,x,t;
    fin >> n;
    fout << fixed;
    go(a,n){
        fin >> c >> f >> x;
        s=2;
        for(t=0; (x-c)/(c)>=(s)/(f); t+=c/s, s+=f){}
        t+=x/s;
        case(a+1) setprecision(7) << t << endl;
    }

   }




