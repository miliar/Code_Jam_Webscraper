// main.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <time.h>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <set>
#include <fstream>
using namespace std;

int gcd(int m, int n) { 
    if(n == 0) 
        return m; 
    else 
        return gcd(n, m % n); 
}
string answer(int P, int Q){
    int g = gcd(P,Q);
    P=P/g;
    Q=Q/g;

    int num_P=0,num_Q=0;
    while(P >0){
        
        P/=2;
        num_P ++;
    }
    while(Q >0){
        
        Q /=2;
        if(Q > 1 && Q% 2 == 1)
            return "impossible";
        num_Q ++;
    }

    stringstream ss;
    ss << (num_Q -num_P);

    return ss.str();
}
int _tmain(int argc, _TCHAR* argv[])
{
    time_t timer_begin,timer_end;
    timer_begin = time(NULL);

    string folder = "C:\\temp\\q1\\";
    freopen((folder+ "test.in").c_str(), "r", stdin);

    fstream fout;
	fout.open(folder + "outfile.txt",fstream::out);

    int T,P,Q;


    vector<vector<int>> matrix;
    vector<string> s;

    scanf("%d", &T);
    for (int c = 1; c <= T; c++) {
        int m;
        scanf("%d/%d", &P, &Q);
       
        cout<< P << "\t" << Q << "\n";
        //cout.precision(7);
        //cout.setf( ios::fixed, ios::floatfield );
        fout << "Case #" << c << ": " << answer(P,Q) << "\n";


    }


    timer_end = time(NULL);

    cout  << '\n' << difftime(timer_end,timer_begin);


    freopen("con", "r", stdin);

    system("PAUSE");



    return 0;
}



