#include <iostream>
#include <map>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    fstream f;
    fstream o;
    f.open("A-small-attempt0.in", ios::in);
    o.open("output.txt", ios::out);
    int T, N, b;
    f >> T;
    for(int i(1); i <= T; i++)
    {
        f >> N;
        int tab[3][2] = {{0, 0}};
        o << "Case #" << i << ": " ;
        for(int a(0); a < N; a++)
        {
            f >> tab[a][0];
            tab[a][1] = a;
        }
        for(int c(0); c < N; c++)
        {
            for(int d(c+1); d < N; d++)
            {
                if(tab[c][0] < tab[d][0])
                {
                    int w = tab[c][0];
                    int z = tab[c][1];
                    tab[c][0] = tab[d][0];
                    tab[c][1] = tab[d][1];
                    tab[d][0] = w;
                    tab[d][1] = z;
                }
            }
        }
        for(int a(0); a < N; a++)
        {
            cout << tab[a][0] << ' ';
            cout << tab[a][1] << endl;
        }
        cout << endl;
        while(tab[0][0] / (tab[1][0]+tab[2][0]) > 2)
        {
            char test = 65 + tab[0][1];
            cout << test << test << ' ';
        }
        while(tab[0][0] / (tab[1][0]+tab[2][0]) > 1)
        {
            char test = 65 + tab[0][1];
            cout << test << test << ' ';
        }
        while(tab[0][0] > 1)
        {
            char test = 65 + tab[0][1];
            char test1 = 65 + tab[1][1];
            tab[0][0] = tab[0][0] - 1; 
            tab[1][0] = tab[1][0] - 1; 
            o << test << test1 << ' '; 
            for(int c(0); c < N; c++)
            {
            for(int d(c+1); d < N; d++)
                {
                if(tab[c][0] < tab[d][0])
                {
                    int w = tab[c][0];
                    int z = tab[c][1];
                    tab[c][0] = tab[d][0];
                    tab[c][1] = tab[d][1];
                    tab[d][0] = w;
                    tab[d][1] = z;
                }
                }
            }
        }
        if(N > 2 && tab[2][0] > 0)
        {    
            char test = 65 + tab[0][1];
            o << test << ' ';
            test = 65 + tab[1][1];
            char test1 = 65 + tab[2][1];
            o << test << test1 << endl;
        }
        else if(tab[2][0] == 0)
        {
            char test = 65 + tab[0][1];
            char test1 = 65 + tab[1][1];
            o << test << test1 << endl;
        }
        else
        {
            char test = 65 + tab[0][1];
            char test1 = 65 + tab[1][1];
            o << test << test1 << endl;
        }
    }
    f.close();
    o.close();
}