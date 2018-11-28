#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    fstream fin, fout;
    fin.open("B-large.in");
    fout.open("c2.txt");
    double F, X, C;
    //C = 500.0; F = 4.0; X = 2000.0;
    fout.setf(ios::fixed);
    fout.precision(7);
    int N, k, i; double time;
    fin >> N;
    for (k=1; k<= N; k++)
    {
        time =0;
        fin >> C >> F >> X; i = -1;
        while (i!=-2)
        {
            if (C/(2+((i+1)*F))+ X/(2+((i+2)*F)) < X/(2+((i+1)*F)))
            {
                time+=C/(2+((i+1)*F)); i++;
            }
            else
            {
                time+=X/(2+((i+1)*F)); i=-2;
            }
            //cout << i << endl; cout << "#" << k << endl;

        }
        fout << "Case #"<< k << ": " << time << endl;
    }
    fout.close();
    fin.close();
    return 0;
}
