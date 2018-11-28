#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input("C:/Users/Utente/Documents/Workspace/C/Counting Sheep/bin/Debug/input.in");
    ofstream output("C:/Users/Utente/Documents/Workspace/C/Counting Sheep/bin/Debug/output.txt");

    bool digits[10];
    int T;

    input >> T;

    cout << T << endl;

    for(int j = 0; j < T; j++)
    {
        for(int i = 0; i < 10; i++)
        {
            digits[i] = false;
        }

        int N, M;

        input >> N;

        bool stop = false;
        bool insomnia = false;

        if(N == 0)
        {
            stop = true;
            insomnia = true;
        }

        for(int k = 1; !stop; k++)
        {
            M = N * k;

            int n = M;

            while(n > 0)
            {
                digits[n % 10] = true;
                n = (n - (n % 10)) / 10;
            }

            stop = true;
            for(int h = 0; h < 10; h++)
            {
                if(digits[h] == false)
                {
                    stop = false;
                }
            }
        }

        if(insomnia)
        {
            output << "Case #" << j+1 << ": INSOMNIA" << endl;
            cout << "Case #" << j+1 << ": INSOMNIA" << endl;
        }
        else
        {
            output << "Case #" << j+1 << ": " << M << endl;
            cout << "Case #" << j+1 << ": " << M << endl;
        }
    }

    return 0;
}
