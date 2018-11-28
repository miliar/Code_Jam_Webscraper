#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    int a[4][4], t, x, r, c;
    /*for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            a[i][j] = 0;
        }
    }*/
    ifstream input_file("D-small-attempt0.in", ios::in);
    ofstream output_file("D-output.out", ios::out);
    input_file>>t;
    for (int i = 1; i <= t; i++)
    {
        input_file>>x>>r>>c;
        if (x == 1)
        {
            output_file<<"Case #"<<i<<": "<<"GABRIEL"<<"\n";
        }
        else if (x == 2)
        {
            if ((r*c) % 2 == 0)
                output_file<<"Case #"<<i<<": "<<"GABRIEL"<<"\n";
            else
                output_file<<"Case #"<<i<<": "<<"RICHARD"<<"\n";
        }
        else if (x == 3)
        {
            if ((r*c) % 3 == 0 and ((r >= 2 and c >= 3) or (r >= 3 and c >= 2)))
                output_file<<"Case #"<<i<<": "<<"GABRIEL"<<"\n";
            else
                output_file<<"Case #"<<i<<": "<<"RICHARD"<<"\n";
        }
        else
        {
            if ((r*c) % 4 == 0 and ((r >= 4 and c >= 3) or (r >= 3 and c >= 4)))
                output_file<<"Case #"<<i<<": "<<"GABRIEL"<<"\n";
            else
                output_file<<"Case #"<<i<<": "<<"RICHARD"<<"\n";
        }
    }
}
