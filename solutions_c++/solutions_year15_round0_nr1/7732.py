#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int main(int ac, char **av)
{
    //cout << "Program started" << endl;
    int case_counter = 0;
    while(cin.good())
    {
        string s;
        getline(cin, s);
        string::size_type i = s.find(" ");
        if (i != string::npos)
        {
            //cout << s << endl;
            string max = s.substr(0, i);
            string audience = s.substr(i + 1, s.length());
            //cout << "max: " << max << " audience: " << audience << endl;
            istringstream isstr(max);
            int max_level; isstr >> max_level;
            int friends = 0;
            int other_people = 0;
            int all = 0;
            for(int level = 0; level < audience.length(); level++)
            {
                int at_level = audience.at(level) - '0';
                //cout << "at_level = " << at_level << " level: " << level << " ";
                if (level > all)
                {
                    int additional = level - all;
                    all += additional;
                    friends += additional;
                }
                all += at_level;
                //cout << "friends: " << friends << " all: " << all << endl;
            }
            //cout << "sum: " << sum << " friends: " << max_level - sum << endl;
            cout << "Case #" << case_counter << ": " << friends << endl;
        }
        case_counter++;
    }
    return 0;
}