#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");

    int t, i, j;
    fin >> t;

    for(j = 1; j <= t; j++)
    {
        int reqNo = 0, currNo = 0, len;

        string s;
        fin >> len;
        fin >> s;

        for(i = 0; i <= len; i++)
        {
            //((int)(s[i] - '0'))
            int noOfShyAti = ((int)(s[i] - '0'));
            if( i > currNo )
            {
                reqNo = reqNo + (i - currNo);
                currNo = currNo + (i - currNo);
            }
            currNo = currNo + noOfShyAti;
        }
        fout << "Case #" << j << ": " << reqNo;
        if(j != t) fout << "\n";
    }
    return 0;
}
