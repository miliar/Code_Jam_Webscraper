#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input ("input.in");
    if (input.is_open())
    {
        int T, X, R, C;
        ofstream output ("output.out");
        input >> T;
        for (int i = 0; i < T; i++)
        {
            string result = "GABRIEL";
            input >> X >> R >> C;
            if ( (X > 6) || ( ( (R*C) % X) != 0) ||
                 ( !(((R >= X) && (C >= X - 1)) || ((R >= X - 1) && (C >= X)) ) ) )
                result = "RICHARD";

            output << "Case #" << i + 1 << ": " << result << endl;
        }
    input.close();
    output.close();
    }
    return 0;
}

