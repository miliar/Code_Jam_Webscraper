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
        double c, f, x;
        fscanf(readFile, "%lf%lf%lf", &c, &f, &x);
        double ans = x;
        double plus = 2.0;
        double cur_time = 0.0;
        while (cur_time < ans)
        {
            if(ans > (x/plus + cur_time))
                ans = (x/plus + cur_time);
            double add_time = c/plus;
            cur_time += add_time;
            plus += f;
        }
        fprintf(writeFile, "Case #%d: %lf\n", tt + 1,  ans);
    }
    return 0;
}




