#include <iostream>
#include <set>
#include <fstream>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

ifstream fin("A-small-attempt1.in");
ofstream fout ("out.txt");
//int gcd (int a, int b)
//{
//    while (a != 0 && b != 0)
//    {
//        if (a > b)
//        {
//            a %= b;
//        } else
//        {
//            b %= a;
//        }
//    }
//    return (a == 0) ? b : a;
//}
//
//const int INF = (int) 1e9+42;

int main()
{
    int t;
    fin >> t;
    for (int k = 0; k < t; k++)
    {
        int row1, row2, cards1[4][4], cards2[4][4];
        fin >> row1;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                fin >> cards1[i][j];
            }
        }
        fin >> row2;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                fin >> cards2[i][j];
            }
        }
        int counter = 0, number;
        row1--; row2--;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                if (cards1[row1][i] == cards2[row2][j])
                {
                    counter++;
                    number = cards1[row1][i];
                }
            }
        }
        fout << "Case #" << k+1 << ": ";
        if (counter > 1)
        {
            fout << "Bad magician!" << endl;
            continue;
        }
        if (counter == 0)
        {
            fout << "Volunteer cheated!" << endl;
            continue;
        }
        fout << number << endl;
    }
    return 0;
}
