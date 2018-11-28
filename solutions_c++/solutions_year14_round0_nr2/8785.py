#include <iostream>
#include <sstream>
#include "stdio.h"
using namespace std;



int main(){

int n;
double c, f, x, a, b, ab, curr, total;
cout.setf(ios::fixed);
cout.precision(6);
cin >> n;

for (int i=0;i<n;i++){

    cin >> c >> f >> x;
    //stop = false;
    curr = 2;
    total = 0;

    while (1){
        a = c/curr;
        b = x / (curr + f);
        ab = x / curr;

        if ((a+b) >= ab){
            total +=ab;
            break;
        }
        else{
            total += a;
            curr += f;
        }
    }


    cout << "Case #" << i+1 << ": " << total << endl;



}





}
