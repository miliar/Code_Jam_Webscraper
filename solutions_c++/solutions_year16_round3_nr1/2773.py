#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, char * argv[])
{
    int tests = 0;
    ifstream fin("A-large.in");
    ofstream fout("output.txt");

    int parties = 0;
    int left = 0;

    int most = 0, partner = 0;

    int * senators = NULL;

    if(fin.is_open())
    {
        //cout << "File Open!" << endl;

        fin >> tests;

        for(int test = 1; test <= tests; test++)
        {
            fout << "Case #" << test << ": ";

            fin >> parties;
            left = parties;

            senators = new int[parties];
            for(int read = 0; read < parties; read++)
            {
                fin >> senators[read];
            }

            while(left)
            {
                most = 0;
                partner = -1;
                for(int majority = 1; majority < parties; majority++)
                {
                    if(senators[most] <= senators[majority])
                    {
                        partner = most;
                        most = majority;
                    }
                }
                if(left % 2 == 0 && partner != -1)
                {
                    senators[partner]--;
                    if(senators[partner] == 0)
                    {
                        left--;
                    }
                    fout << (char)(partner + 'A');
                }
                senators[most]--;
                if(senators[most] == 0)
                {
                    left--;
                }
                fout << (char)(most + 'A');
                fout << " ";
            }
            fout << endl;
            delete[] senators;
        }
        fin.close();
        fout.close();
    }
    else
    {
        //cout << "Could not open file!" << endl;
    }
    return 0;
}
