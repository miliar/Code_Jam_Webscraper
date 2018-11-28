
#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <fstream>

using namespace std;

int main(){

    ifstream infile;
    infile.open("InputB1.in");
    ofstream outfile;
    outfile.open("outputBrandan.txt");

    int t =0;
    int people =0;
     int check = 0;
    char a;
    infile >> t;

    for (int i = 1;i<=t; i++)
    {
        int c =0;

        infile >> c;
        int r[c+1];

        for(int j =0; j<=c; j++)
        {
            infile >> a;
                r[j] = a - '0';
                people += r[j];

        }

        int needed =0;
        int q =0;
        int up =0;


        for(int x =0; x<=c; x++)
        {

            if(up < x)
            {
                int difference = x - up;
                needed += difference;
                up += difference;

            }

            up += r[x];

        }




            cout << "Case #" << i << ": " << needed << "\n";
            outfile << "Case #" << i << ": " << needed << "\n";

    }
    infile.close();
    outfile.close();

}
