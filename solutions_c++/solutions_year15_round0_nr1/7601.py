#include<iostream>
#include<algorithm>
#include<stack>
#include<queue>
#include <iostream>
#include <fstream>
#include<stdio.h>
#include <string.h>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

int main(){

    int t;
    fin >> t;
    for( int c = 1; c <= t; c++ ){

        int len;
        fin >> len;
        string str;
        fin >> str;
        int totP = 0;
        int ext = 0;
        for( int i = 0; i <= len; i++ ){
            int val = str[ i ] - '0';
            if( val == 0 ) continue;
            if( totP < i ){
                ext += i - totP;
                totP += i - totP;
            }
            totP += val;
        }

        if( c > 1 ) fout << endl;
        fout << "Case #" << c << ": " << ext;
    }


    return 0;
}
