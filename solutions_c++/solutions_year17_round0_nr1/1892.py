#include <iostream>
#include <fstream>
using namespace std;
ifstream ka("A-large.in");
ofstream ki("output.out");
int t, k;
string s;

char invers(char c)
{
    if(c == '+')
        return '-';
    else
        return '+';
}

int main()
{
    ka >> t;
    //ka.get();
    for(int caz = 1; caz <= t; caz++)
    {
        ka >> s >> k;
        int sol = 0;
        bool mere = true;
        for(int i = 0; i < s.size() && mere; i++)
        {
            if(s[i] == '-')
            {
                if(i + k <= s.size())
                {
                    sol++;
                    for(int j = i; j < i + k; j++)
                        s[j] = invers(s[j]);
                }
                else
                    mere = false;
            }
        }
        ki << "Case #" << caz << ": ";
        if(mere)
            ki << sol;
        else
            ki << "IMPOSSIBLE";
        ki << '\n';
    }
}
