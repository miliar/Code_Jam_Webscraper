
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input("input.in", std::ifstream::in);
    ofstream output("output.out", std::ofstream::out);

    int nTest;
    input >> nTest;

    int Smax, maxStanding = 0, standing = 0, invited = 0;
    char Si[2048];

    for (int i = 0; i < nTest; i++)
    {
        input >> Smax;
        input >> Si;
        //cout << "Si = " << Si << endl;


        for (int j = 0; j <= Smax; j++)
            maxStanding += (int)Si[j] - 48;
        //cout << "maxStanding = " << maxStanding << endl;

        for (int j = 0; j <= Smax; j++)
        {
            //cout << standing << " " << j << endl;
            do
            {
                if (standing >= j)
                {
                    standing += (int)Si[j] - 48;
                    break;
                }
                else
                {
                    invited++;
                    standing++;
                    maxStanding++;
                }
            }while(true);
        }
        //cout << "invited = " << invited << endl;
        output << "Case #" << i+1 << ": " << invited << endl;
        invited = 0;
        standing = 0;
        maxStanding = 0;
    }

    input.close();
    output.close();
    return 0;
}
