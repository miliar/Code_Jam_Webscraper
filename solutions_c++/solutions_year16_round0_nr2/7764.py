#include <iostream>
#include <string>

using namespace std;

void flip(string &s, string::size_type n);

int main()
{
    unsigned short T;
    cin >> T;
    for (unsigned short t = 1; t <= T; ++t)
    {
        string s;
        cin >> s;
        unsigned int flips = 0;
        string::size_type p1 = 0;
        while ((p1 = s.find_first_of("-")) != string::npos)
        {
            string::size_type p2 = s.find_first_of("+", p1+1);
            p2 = (p2 == string::npos)? s.size() : p2;
            flip(s, p2);
            ++flips;
        }
        cout << "Case #" << t << ": " << flips << '\n';
    }
}

void flip(string &s, string::size_type n)
{
    for (string::size_type i = 0; i < n; ++i)
        s[i] = static_cast<char>(88 - static_cast<int>(s[i]));
}

