#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main()
{
    ifstream file_reader("large_input.in");
    ofstream file_writer("large_answer.txt");

    int t;
    file_reader >> t;

    for (int c = 1; c<=t; ++c)
    {
        int n;
        file_reader >> n;

        if(n==0)
        {
            file_writer << "Case #" << c << ": INSOMNIA" << endl;
        }
        else
        {
            bool digits[10];
            for (int i = 0; i<10; ++i)
                digits[i] = false;
            int mulitplier = 1;
            long long m_n = n;
            int n_digits = 0;
            while(true)
            {
                m_n = n*mulitplier;
                stringstream ss;
                ss << m_n;
                for (int i = 0; i<ss.str().size(); ++i)
                {
                    if(digits[ss.str()[i]-'0'] == false)
                    {
                        ++n_digits;
                        digits[ss.str()[i]-'0'] = true;
                    }
                }
                if(n_digits==10)
                    break;
                ++mulitplier;
            }
            file_writer << "Case #" << c << ": " << n*mulitplier << endl;
        }
    }
}
