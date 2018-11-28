#include <iostream>
#include <string>
#include <sstream>

using namespace std;


int main()
{
    string input = "";



    int t, count;
    cin >> t;

    for (int i = 1; i <= t; i++)
    {
        count = 0;
        cin >> input;

        char last = ' ';

        for(std::string::iterator it = input.begin(); it != input.end(); ++it) {
            if ((*it == '-' && last != '-') || (*it == '-' && last == ' '))
            {
                last = '-';

                count++;
            }
            else if (*it == '+' && last != '+')
            {
                last = '+';

                count++;
            }
        }

        if(last == '+')
        {
            count--;
        }

        cout << "Case #" << i << ": " << count << endl;

    }



}






