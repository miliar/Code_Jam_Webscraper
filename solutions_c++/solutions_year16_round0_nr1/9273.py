#include <iostream>
#include <fstream>
#include <list>
#include <algorithm>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
    ifstream f_in;
    ofstream f_out;
    f_in.open("input.txt");
    f_out.open("output.txt", ios_base::trunc );

    string temp;
    getline(f_in, temp);
    int T = stoi(temp);
    int N;
    string::size_type s;

    for(int i=1; i<T+1; i++)
    {
        getline(f_in, temp);
        N = stoi(temp);

        if ( N == 0 )
        {
            cout << "Case #" << i << ": INSOMNIA" << endl;
            f_out << "Case #" << i << ": INSOMNIA" << endl;
        }
        else
        {
            list<char> digits= {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
            int j = 0;
            string Ni;

            while( !digits.empty() )
            {
                j++;
                Ni = to_string(j * N);

                for( auto c : Ni )
                    digits.remove(c);
            }

            cout << "Case #" << i << ": " << Ni << endl;
            f_out << "Case #" << i << ": " << Ni << endl;
        }
    }

    f_in.close();
    f_out.close();
    return 0;
}
