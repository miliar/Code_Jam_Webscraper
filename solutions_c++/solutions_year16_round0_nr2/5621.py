#include <fstream>
using namespace std;
ifstream ka("B-large.in");
ofstream ki("revenge.out");
int t;
string s;
int main()
{
    ka >> t;
    ka.get();
    for(int i = 1; i <= t; i++)
    {
        getline(ka, s);
        int sol = 0;
        for(int j = 1; j < s.size(); j++)
        {
            if(s[j] != s[j - 1])
                sol++;
        }
        if(s[s.size() - 1] == '-')
            sol++;
        ki << "Case #" << i << ": " << sol << '\n';
    }
}
