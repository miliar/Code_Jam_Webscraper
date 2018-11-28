#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream input_file("A-large.in", ios::in);
    ofstream output_file("Alarge.out", ios::out);
    int t, needed = 0, standing = 0, smax, temp, temp1;
    char a[10000];
    input_file>>t;
    for (int i = 1; i <= t; i++)
    {
        input_file>>smax;
        input_file>>a;
        for (int j = 0; j <= smax; j++)
        {
            temp = int(a[j])-48;
            if (standing >= j)
            {
                standing += temp;
            }
            else
            {
                temp1 = j - standing;
                needed += temp1;
                standing += temp + temp1;
            }
        }
        output_file<<"Case #"<<i<<": "<<needed<<"\n";
        standing = needed = 0;
    }
}
