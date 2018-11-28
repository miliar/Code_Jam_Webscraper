#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#define MAXLEN 110
using namespace std;

int main()
{
    int t, a, b, count = 1, tmp;
    vector <int> x(4, 0), y(4, 0);
    ifstream fin("A-small-attempt2.in");
    ofstream fout("A2.out");
    
    fin >> t;
    
    while (t--)
    {
        fin >> a;
        
        for (int i = 0; i < 16; i++)
        {
            fin >> tmp;
            if (i >= (a - 1) * 4 && i < a * 4)
                x[i - (a - 1) * 4] = tmp;
        }
            
        fin >> b;
        
        for (int i = 0; i < 16; i++)
        {
            fin >> tmp;
            if (i >= (b - 1) * 4 && i < b * 4)
                y[i - (b - 1) * 4] = tmp;
        }
            
        sort(x.begin(), x.end());
        sort(y.begin(), y.end());
        
        int i = 0, j = 0, n = 0, res;
        
        while (i < 4 && j < 4)
        {
            if (x[i] < y[j])
                i++;
            else if (x[i] > y[j])
                j++;
            else
            {
                res = x[i];
                i++;
                j++;
                n++;               
            }
        }
        
        fout << "Case #" << count++ << ": "; 
            
        if (n == 0)
            fout << "Volunteer cheated!" << endl;
        else if (n == 1)
            fout << res << endl;
        else
            fout << "Bad magician!" << endl;
            
        //system("pause");
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
