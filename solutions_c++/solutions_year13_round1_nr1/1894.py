#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <ctime>
#include <map>
#include <cmath>
#include <fstream>
#include <iterator>
#include <cstring>
#include <algorithm>
#include <set>
#include <cassert>
#include <list>
#define LL long long
#define ULL unsigned long long
#define UI unsigned int
#define MOD 1000000007
using namespace std;

int testCases;
ULL r,t;

ULL form(ULL r, ULL diskNo)
{
    return 2*r + 4*(diskNo-1) + 1;
}

int solve()
{
    int i=1, cnt=0;
    while(true){
        //cout << form(r,i) << " " << t << endl;
        if(t>=form(r,i)){

            t -= form(r,i);
            i++;
            cnt++;
        }else
            return cnt;
    }
}

int main ()
{
    ofstream fout;
    ifstream fin;
    fin.open("testFile.txt");
    fout.open("output.txt");

    fin >> testCases;

    for(int i=0;i<testCases;i++){

        fin >> r >> t;

        fout << "Case #" << i+1 << ": " << solve() << endl;

    }


    fin.close();
    fout.close();
}
