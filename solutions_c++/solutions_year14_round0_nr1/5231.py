#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <list>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

string int_to_string(int a)
{
    string tt;
    while(a!=0)
    {
        char rr = (a%10) + '0';
        tt = tt + rr;
        a = a/10;
    }

    string ret;
    for(int i = tt.length() - 1; i >= 0; i--)
        ret = ret + tt[i];
    return ret;
}

int main()
{
    ofstream out("output.txt");
    int testcases;
    cin >> testcases;
    string rez[testcases];

    for(int k = 0; k < testcases; k++)
    {
        int a1[4][4], a2[4][4], temp1[4], temp2[4];
        int row1, row2;

        cin >> row1;
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            cin >> a1[i][j];

    cin >> row2;
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            cin >> a2[i][j];

    for(int i = 0; i < 4; i++)
        temp1[i] = a1[row1 - 1][i];
     for(int i = 0; i < 4; i++)
        temp2[i] = a2[row2 - 1][i];

    int counter = 0;
    int cc;
    for(int i = 0; i < 4; i++)
    {
        for(int j = 0; j < 4; j++)
        if(temp1[i] == temp2[j]){ cc = temp1[i]; counter++;}
    }

    if(counter == 1){ rez[k] = int_to_string(cc);}
    else if(counter > 1)rez[k] = "Bad magician!";
    else if(counter == 0)rez[k] = "Volunteer cheated!";
    }

    for(int i = 0; i < testcases; i++)
            out <<"Case #" << i + 1 << ": " << rez[i] << endl;
}
