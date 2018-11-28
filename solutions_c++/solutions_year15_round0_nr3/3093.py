/*
g++ -O2 -o tst dijkstra.cpp
cat in | ./tst > out
*/


#include <iostream>     // std::cin, std::cout, std::hex
#include <fstream>      // std::fstream
#include <algorithm>    // std::reverse
#include <vector>       // std::vector

using namespace std;

int mult[4][4] = {
    {1, 2, 3, 4},
    {2,-1, 4,-3},
    {3,-4,-1, 2},
    {4, 3,-2,-1}
};

int multab( int a, int b)
{
    return mult[a-1][b];
}


int main ()
{
    int numTests;
    int testNum = 0;

    cin >> numTests;

    while( ++testNum <= numTests) {
        int L,X;

        cin >> L;
        cin >> X;
        string oo;
        getline(cin, oo);

//        cout << "L " << L << " X " << X << endl;

        string line;
        getline(cin, line);
//        cout << line << endl;

        int find = 2;
        int prod = 1;
        int neg = 1;

        for(int x = 0; x < X; x++) {
            char * p = (char *)line.c_str();
            for(int l=0; l < L; l++, p++) {
                prod = multab(prod, *p-'i'+1);
                if(prod < 0) {
                    prod = -prod;
                    neg = -neg;
                }
                if(neg==1 && prod == find) {
//                    cout << "Found " << find << " pos " << l << " " << x << endl;
                    find++;
                    prod = 1;
                }
            }
        }
        string resp("NO");
        if(find == 5 && (prod*neg) ==1) {
            resp = string("YES");
        }
//        cout << "Case #" << testNum <<": " << resp << " prod " << prod *neg << endl;
        cout << "Case #" << testNum <<": " << resp << endl;
    }

    cout << endl;

    return 0;
}


