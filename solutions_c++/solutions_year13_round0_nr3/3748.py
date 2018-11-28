#include <iostream>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cstdlib>
#include <cmath>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("C-small-attempt0.txt", ios::in);
    if (!fin.is_open())
    {
        cerr << "Unable to open file" << endl;
        exit(10);
    }

    fout.open("C-small solution.txt", ios::out);
    if(!fout.is_open())
    {
        cerr << "Unable to open file" << endl;
        exit(10);
    }

    int testCases;
    fin >> testCases;

    int start, end, i(1);

    for (i; i < testCases+1; i++)
    {
        fin >> start;
        fin >> end;
int count(0);


        for (start; start <= end; start++)
        {

            int startCopy = start;
            int reverse(0), lastDigit(0);

            while (startCopy > 0)
            {
                lastDigit = startCopy%10;
                reverse = reverse*10 + lastDigit;
                startCopy = startCopy/10;
            }

            if (reverse == start)
            {
                int squareRoot = sqrt(start);
                //cout << squareRoot << " ";
                if(squareRoot*squareRoot >= start)
                {
                    int squareRootCopy = squareRoot;
                    reverse =0;
                    while (squareRootCopy > 0)
                    {
                        lastDigit = squareRootCopy%10;
                        reverse = reverse*10 + lastDigit;
                        squareRootCopy = squareRootCopy/10;
                    }

                    if (reverse == squareRoot)
                    {
                        count++;
                    }
                }
            }


        }
        //cout << endl;
        fout << "Case #" << i << ": " << count << endl;

    }

    fin.close();
    fout.close();

    return 0;
}
