#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

int main ()
{
    ifstream in ("input.txt");
    ofstream out ("output.txt");
    int n;
    int a;
    int b;
    int i;
    int j;
    int k;
    int v[1000];
    int num;
    int cifre;
    bool s;
    int solution;
    in >> n;
    for (i = 0; i < n; i++)
        {
        in >> a >> b;
        solution = 0;
        for (j = a; j <= b; j++)
            {
            s = true;
            cifre = 0;
            num = j;
            while (num != 0)
                  { 
                  v[cifre] = num%10;
                  num /= 10;
                  cifre++;
                  };
            for (k = 1; k <= cifre/2; k++) 
                {
                if (v[k-1] != v[cifre-k])
                   {
                   s = false;      
                   };
                };
            num = sqrt(j);
            if ((num*num) != j)
               {
               s = false;      
               };
            cifre = 0;
            while (num != 0)
                  { 
                  v[cifre] = num%10;
                  num /= 10;
                  cifre++;
                  };
            for (k = 1; k <= cifre/2; k++) 
                {
                if (v[k-1] != v[cifre-k])
                   {
                   s = false;      
                   };
                };
            if (s)
               {
               solution++;   
               };
            };
        out << "Case #" << i+1 << ": " << solution;
        if (i+1 != n)
           {
           out << "\n";
           };
        };
    return 0; 
}
