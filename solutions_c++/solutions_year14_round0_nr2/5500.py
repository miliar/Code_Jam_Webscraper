#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>

#define INF ~(1 << 31)

using namespace std;
/*
double find_time(double C, double F, double X)
{
    double time = X/2.0;
    double sum;
    int n = 1;
    while (true)
    {
        //calculate next time...
        sum = 0.0;
        for (int i = 0; i < n; i++)
            sum += C/(2 + i*F);
        sum += X/(2 + n*F);
        if (sum > time)
            break;
        else time = sum;
        n++;
        
    }
    return time;
}
*/
double find_time_quick(double C, double F, double X)
{
    double prev_time, cur_time;
    int n = 2;
    prev_time = X/2.0;
    cur_time = C/2.0 + X/(2.0 + F);
    while (cur_time < prev_time)
    {
        prev_time = cur_time;
        cur_time = prev_time - X/(2 + (n-1)*F) + C/(2 + (n-1)*F) + X/(2 + n*F);
        n++;
    }
    return prev_time;
}

int main(int argc, char *argv[]) {
    
    ifstream fin("cookie.in");
    ofstream fout("cookie.out");
    
    int T; fin >> T;
    double C, F, X; 
    for (int i = 1; i <= T; i++)
    {
        fin >> C >> F >> X;
        fout << "Case #" << i << ": " << fixed << setprecision(7) << find_time_quick(C, F, X) << "\n";
    }
    
    fin.close();
    fout.close();
    return 0;
}