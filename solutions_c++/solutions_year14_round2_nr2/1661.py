// prlblem2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <limits>
#include <algorithm>

using namespace std; 

int _tmain(int argc, _TCHAR* argv[])
{
    ifstream inf(argv[1]); 
    // ifstream inf("D:\\codejam\\prlblem2\\Debug\\test.txt"); 

    int n = 0; 
    inf >> n; 
    for (int ca=1; ca<=n; ca++) {
        int a, b, k;
        inf >> a >> b >> k;

        int num = 0; 
        for (int i=0; i<a; i++)
            for (int j=0; j<b; j++) 
                if ((i & j) < k) num++;

        cout << "Case #" << ca << ": " << num << endl; 
    }

	return 0;
}

