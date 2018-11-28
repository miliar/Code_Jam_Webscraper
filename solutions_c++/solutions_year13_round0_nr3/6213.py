#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <math.h>
#include <algorithm>
#include <sstream>

using namespace std;

bool isSq(int x){
    double d_sqrt = sqrt(x);
    int i_sqrt = d_sqrt;
    if (d_sqrt == i_sqrt)
        return true;
    else
        return false;

}

bool isPalindrome(int x){
    if (x<10 && x >=0)
        return true;
    int num = x;
    int rev = 0;
    int dig = 0;
    while (num > 0)
    {
        dig = num % 10;
        rev = rev * 10 + dig;
        num = num / 10;
    }
    if (x == rev)
        return true;
    else
        return false;
}

int main() {
    ifstream fin; ofstream fout;
    fin.open("input.in", ios::in); fout.open("output.out",ios::out);
    int amtTestCase = 0;
    fin >> amtTestCase;
    int a,b,fairAmt,ji;

    for(int i=0;i<amtTestCase;i++){
        fairAmt =ji = 0;
        fin >> a; fin >> b;
        for(int j = a;j<=b;j++){
            if (isPalindrome(j) && isSq(j) && isPalindrome(int(sqrt(j)))){cout << j << " " << j*j << " \n";fairAmt++;}
        }
        fout << "Case #" << i+1 << ": " << fairAmt << "\n";
    }
	return 0;
}
