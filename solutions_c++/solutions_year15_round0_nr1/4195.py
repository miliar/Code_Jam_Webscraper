#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input ("input.in");
    if (input.is_open())
    {
        int T;
        int Smax;
        ofstream output ("output.out");
        input >> T;
        for (int i = 0; i < T; i++)
        {
            input >> Smax;
            int totalppl = 0;
            int requiredppl = 0;
            for (int k = 0; k <= Smax; k++)
            {
                if (totalppl < k)
                {
                    requiredppl += k - totalppl;
                    totalppl = k;
                }
                char c;
                input >> c;
                int n = c - '0';
                totalppl += n;
            }
            output << "Case #" << i + 1 << ": " << requiredppl << endl;
        }
    input.close();
    output.close();
    }
    return 0;
}

