#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <cstring>

using namespace std;

int main(void){

    ifstream fin("B-small-attempt0.in");
    ofstream fout("B-small-attempt0.out");

    int test;
    fin>>test;
    for ( int t = 1; t <= test; ++t ){
        int a;
        int b;
        int c;
        fin>>a>>b>>c;
        int ans = 0;
        int temp = a;
        if ( a > b){
            temp = a;
            a = b;
            b = temp;
        }
        for ( int i = 0; i < a; ++i)
        for ( int j = 0; j < b; ++j){
            if ( (i & j) < c)
                ++ans;
        }
        fout<<"Case #"<<t<<": "<<ans<<"\n";
    }


    return 0;
}

