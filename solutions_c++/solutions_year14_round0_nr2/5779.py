#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int t;
    fin >> t;
    fout.setf(ios::fixed,ios::floatfield);
    fout.precision(7);
    for(int ctr = 1; ctr <= t;ctr++)
    {
            double c,f,x,c_t = 0,c_r = 2;
            fin >> c >> f >> x;
            while((x/c_r) > ((c/c_r)+(x/(c_r+f))))
            {
                          c_t += c/c_r;
                          c_r += f;
            }
            c_t += x/c_r;
            fout << "Case #" << ctr << ": " << c_t << endl;
    }
    return 0;
}
