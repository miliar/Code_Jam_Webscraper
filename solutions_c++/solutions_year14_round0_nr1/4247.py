#include <iostream>
#include <fstream>
#include <cstdio>
#include <ctime>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

string fin = "//Users//Roman//Documents//GoogleCodeJam//input.txt";
FILE * readFile = fopen (fin.c_str(),"r+");
string fout = "//Users//Roman//Documents//GoogleCodeJam//output.txt";
FILE * writeFile = fopen (fout.c_str(),"w+");


int main()
{
    //freopen( "output.txt", "w+" ,stdout);
    int t, tt;
    fscanf(readFile, "%d",  &t);
    
    for(tt = 0; tt < t; ++tt)
    {
        int ans1, ans2;
        fscanf(readFile, "%d",  &ans1);
        vector < int > x(17, 0);
        for(int i = 0; i < 4; ++i)
        {
            int a,b,c,d;
            fscanf(readFile, "%d%d%d%d",  &a, &b, &c, &d);
            if(ans1 == i + 1)
            {
                x[a] += 1;
                x[b] += 1;
                x[c] += 1;
                x[d] += 1;
            }
        }
        fscanf(readFile, "%d",  &ans2);
        int ans = -1;
        for(int i = 0; i < 4; ++i)
        {
            int a,b,c,d;
            fscanf(readFile, "%d%d%d%d",  &a, &b, &c, &d);
            if(ans2 == i + 1)
            {
                x[a] += 1;
                x[b] += 1;
                x[c] += 1;
                x[d] += 1;
            }
        }
        for(int i = 1; i <= 16; ++i)
        {
            if(ans == -1 && x[i] == 2)
            {
                ans = i;
            }
            else
            {
                if(ans > 0 && x[i] == 2)
                {
                    ans = -2;
                }
            }
        }
        if(ans > 0)
        {
            fprintf(writeFile, "Case #%d: %d\n", tt + 1, ans);
        }
        if(ans == -2)
        {
            fprintf(writeFile, "Case #%d: Bad magician!\n" , tt + 1);
        }
        if(ans == -1)
        {
            fprintf(writeFile, "Case #%d: Volunteer cheated!\n", tt + 1);
        }
    }
    return 0;
}




