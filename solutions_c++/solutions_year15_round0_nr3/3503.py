#include <iostream>
using std::cin;
using std::cout;
using std::endl;

#include <fstream>
using std::ifstream;

#include <string>
using std::string;

#include <stdlib.h>

#include <cassert>

class Quaternion
{
    bool negative;
    char check;

public:
    Quaternion(char c)
        : negative(false), check(c) {}

    bool same(char c1, char c2)
    {
        if (c1 == c2)
            return true;
        return false;
    }

    char next(char c)
    {
        switch (c)
        {
            case 'i': return 'j';
            case 'j': return 'k';
            case 'k': return 'i';
        }
    }

    char multiply(char current, char next_c)
    {
        if (current == next_c)
        {
            check = '1';
            negative = !negative;
        }

        else if (current == '1')
            check = next_c;

        else if (next_c == next(current))
            check = next(next_c);

        else
        {
            check = next(current);
            negative = !negative;
        }
    }

    char get_char()
    {
        return check;
    }

    bool get_neg()
    {
        return negative;
    }

    void set_char()
    {
        check = '1';
    }

    void set_neg()
    {
        negative = false;
    }
};

int main(int argc, char* argv[])
{
    // Open file
    char* filename;
    filename = argv[1];
    ifstream fs(filename);
    assert(fs.is_open());

    // Get number of cases
    int N_cases;
    fs >> N_cases;

    // Ignore trailing whitespace
    fs.ignore();

    // For every case...
    for (int y = 0; y < N_cases; ++y)
    {
        string result;

        long long string_size, repeats;
        fs >> string_size >> repeats;
        //cout << string_size << " " << repeats << endl;
        if (string_size * repeats < 3) result = "NO";

        string str;
        fs >> str;

        /*for (int m = 0; m < repeats; ++m)
        {
            cout << str;
        }
        cout << endl;*/

        if (string_size == 3)
        {
            if (str == "ijk") result = "YES";
            else result = "NO";
        }

        else
        {
            Quaternion q(str.at(0));

            long long total_chars = string_size * repeats;
            //cout << "total_chars: " << total_chars << endl;
            //int current_char = 0;
            long long str_index = 1;

            bool i = false;
            bool j = false;
            bool k = false;

            if (q.get_char() == 'i')
            {
                i = true;
                q.set_char();
                q.set_neg();
            }
            //cout << q.get_char() << endl;

            // find i, j, k
            for (long long x = 0; x < total_chars - 1; ++x)
            {
                if (str_index == str.size()) str_index = 0;

                //cout << q.get_char() << "*" << str.at(str_index) << endl;
                q.multiply(q.get_char(), str.at(str_index));
                //cout << q.get_char() << endl;
                if (i == true)
                {
                    if (j == true)
                    {
                        if (x == (total_chars - 2) 
                            && q.get_char() == 'k'
                            && q.get_neg() == false)
                        {
                            k = true;
                            //cout << "k is true" << endl;
                        }
                    }
                    else
                    {
                        if (q.get_char() == 'j' && q.get_neg() == false)
                        {
                            j = true;
                            q.set_char();
                            q.set_neg();
                            //cout << "j is true " << q.get_char() << endl;
                        }
                    }
                }
                else
                {
                    if (q.get_char() == 'i' && q.get_neg() == false)
                    {
                        i = true;
                        q.set_char();
                        q.set_neg();
                        //cout << "i is true " << q.get_char() << endl;
                    }
                }
                ++str_index;
            }

            if (i == true
                && j == true
                && k == true) 
                result = "YES";
            else result = "NO";
        }

        // Print case number
        cout << "Case #" << y + 1 << ": ";
        cout << result << endl;
        //cout << endl;
    }

    return 0;
}
