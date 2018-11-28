#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int t;

int main()
{
    ifstream in("in.in");
    ofstream out("out.out");
    in >> t;
    int test = 0;
    while(test < t)
    {
        int r1;
        int a[4][4];
        int r2;
        int b[4][4];
        in >> r1;
        r1--;
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                in >> a[i][j];
            }
        }
        in >> r2;
        r2--;
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                in >> b[i][j];
            }
        }
        int count = 0;
        int card;
        for(int i = 0; i < 4; i++)
        {
            for(int j= 0; j < 4; j++)
            {
                if(a[r1][i] == b[r2][j])
                {
                    count++;
                    card = a[r1][i];
                }
            }
        }
        out << "Case #" << test + 1 << ": ";
        if(count == 1)
            out << card << endl;
        else if(count == 0)
        {
            out << "Volunteer cheated!" << endl;
        }
        else
            out << "Bad magician!" << endl;
        test++;
    }
}
