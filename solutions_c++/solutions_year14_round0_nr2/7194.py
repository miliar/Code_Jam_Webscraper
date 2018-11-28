#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std;

int main()
{
    int t ,p;
    double c, f, x;
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");
    fin >> t;

    for(p = 1; p <= t; p++)
    {
        double sum1 = 0, sum = 0, temp, g = 2.0;
        fin >> c >> f >> x;
        for(;;)
        {
            temp = sum;
            sum = sum + x/g;

            sum1 = temp + c/g + x/(g+f);

            if(sum < sum1)
            {
                break;
            }
            sum = temp + c/g;
            g = g+f;
        }
        fout << setprecision(7) << fixed;
        fout <<"Case #" << p << ": " << sum;
        fout << "\n";


    }
    fin.close();
    fout.close();
}
