#include <iostream>
#include <math.h>
#include <sstream>
#include "Untitled1.h">
#include <fstream>
using namespace std;
int main()

{
    ofstream outfile;
    outfile.open("output.txt");
int t;
cin >> t;
int cop(0);
for (cop=0;cop<t;cop++){
int A,B,total(0);
cin >> A >> B;
for (;A<=B;A++){
    int a(0);
    a=sqrt(A);int j=a*a;
    if (A==j){
        int uop;uop=check(A);
        total=total+uop;

    }

}
outfile << "Case #" << cop+1 << ": " << total << endl;
}
return 0;
}


