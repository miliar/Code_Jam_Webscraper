#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
    double c,x,f,s,t;
    int n;
    ifstream inp("input.txt");
    ofstream out("output.txt");
    inp >> n;
    for (int i=1; i<=n; i++)
    {
        inp >> c >> f >> x;
        s=2;
        t=0;
        if (c<x)
        {
            t=(double)c/s;
            while ((double)(x/(s+f))<(double)((x-c)/s))
            {
                s+=(double)f;
                t+=(double)c/s;
            }
            t+=(double)((x-c)/s);
        } else t= (double)x/s;
        out << "Case #" << i << ": " << t << endl;
    }
    return 0;
}
