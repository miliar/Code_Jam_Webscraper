#include <iostream>
#include <fstream>
#include <list>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
    ifstream f_in;
    ofstream f_out;
    f_in.open("input.txt");
    f_out.open("output.txt", ios_base::trunc );

    string temp;
    getline(f_in, temp);
    int T = stoi(temp);
    string N;

    for(int i=1; i<T+1; i++)
    {
        int result = 0;
        getline(f_in, N);
        bool previousMinus = false;

        if( N[0] == '-' )
        {
            result++;
            previousMinus = true;
        }
        for( int j=1; j<N.length(); j++ )
        {
            if( N[j] == '-' && !previousMinus)
            {
                result += 2;
                previousMinus = true;
            }
            else if ( N[j] == '+' )
                previousMinus = false;
        }

        cout << "Case #" << i << ": " << result << endl;
        f_out << "Case #" << i << ": " << result << endl;
    }

    f_in.close();
    f_out.close();
    return 0;
}
