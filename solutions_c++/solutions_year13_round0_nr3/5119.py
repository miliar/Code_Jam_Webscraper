
#include <math.h>

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

vector<unsigned long> num;

void loop(ifstream *ifile) {

    unsigned long b,e;
    *ifile >> b >> e;

    int res = 0 ;
    for(int i = 0; i < num.size(); i++) {
            if ( num[i] >= b && num[i] <= e )
                res++;
    }
    cout << res;
}

bool check_palindorome(unsigned long a){

    unsigned long b = 0;

    if ( a % 10 == 0 ) return false;

    while (a>=b)
    {
        if (a == b) return true;
        b = 10 * b + a % 10;
        if (a == b) return true;
        a = a / 10;
    }
    return false;

}

bool chk_palin_sq( unsigned long n){

    if ( check_palindorome(n) ) {
        if(num.size() < 1 ) return true;

        unsigned long a = sqrt(n);
        if( num[num.size()-1] < a || check_palindorome(a)) {
            return true;
        }
    }

    return false;
}

int main(){

    for (unsigned long i = 1; i < 100000000; i++ ) {
        unsigned long n = i*i;
        if ( chk_palin_sq(n) ) {
            num.push_back(n);
        }
    }


    ifstream ifile("input.txt");

    int testcasenum;
    ifile >> testcasenum;

    for(int i = 0; i < testcasenum ; i++ ) {
        cout << "Case #" << i+1 << ": ";
        loop(&ifile);
        cout <<  endl;
    }

    return 0;

}


