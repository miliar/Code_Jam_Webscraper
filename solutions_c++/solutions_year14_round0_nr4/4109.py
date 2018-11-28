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
        int n;
        fscanf(readFile, "%d", &n);
        vector < double > x(n,0);
        vector <bool> all(1001, true);
        for(int i = 0; i < n; ++i)
        {
            double temp;
            fscanf(readFile, "%lf", &temp);
            x[i] = temp;
            
        }
        vector < double > y(n,0);
        for(int i = 0; i < n; ++i)
        {
            double temp;
            fscanf(readFile, "%lf", &temp);
            y[i] = temp;
            //all[y[i]] = false;
        }
        sort(x.begin(), x.end());
        sort(y.begin(), y.end());
        int check = 0;
        //for(int  i = 0; i < n; ++i)
        //{
         //   if(x[i] > y[i])
         //       check++;
        //}
        int ans = n;
        vector < bool > xu(n, true);
        vector < bool > yu(n, true);
        for(int i = 0; i < n; ++i)
        {
            double k = x[i];
            for(int j = 0; j < n; ++j)
            {
                if(y[j] > k && yu[j] )
                {
                    ans--;
                    yu[j] = false;
                    break;
                }
            }
        }
        for(int i = 0; i < n; ++i)
        {
            yu[i] = true;
        }
        for(int i = 0; i < n; ++i)
        {
            double k = x[i];
            double ymin = 1020;
            int jmin = 0;
            for(int j = 0; j < n; ++j)
            {
                if(y[j] < ymin && yu[j])
                {
                    ymin = y[j];
                    jmin = j;
                }
            }
            if(k > ymin)
            {
                double ymax = -1;
                int jmax = 0;
                for(int j = 0; j < n; ++j)
                {
                    if(y[j] > ymax && yu[j])
                    {
                        ymax = y[j];
                        jmax = j;
                    }
                }
                if(ymax >= 1.0)
                {
                    yu[jmax] = false;
                }
                else
                {
                    yu[jmin] = false;
                    check++;
                }
                
            }
        }
        fprintf(writeFile, "Case #%d: %d %d\n", tt + 1, check, ans);
    }
    return 0;
}




