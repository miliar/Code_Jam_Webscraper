#include <iostream>
#include <fstream>
#include <string>
using namespace std;
ifstream in("A-small-attempt0.in");
ofstream out("asmall.out");
const char vowels[] = {'a','e','i','o','u'};
int T;
int n;
string s;

int inv(char c)
{
    for (int i = 0; i < 5; ++i)
        if (c == vowels[i]) return 1;
    return 0;
}

int calc(int a,int b)
{
    int k = 0;
    for (int i = a; i < b; ++i){
        if ( !inv(s[i]) ) ++k;
        else k = 0;
        if ( k >= n ) return 1;
    }
    return 0;
}

int main()
{
    in >> T;
    for (int test = 1; test <= T; ++test)
    {
        in >> s;
        in >> n;
        int k = 0;
        for (int i = 0; i < s.size(); ++i)
            for (int j = i+n; j <= s.size(); ++j)
                if ( calc(i,j) ) k += 1;

        out << "Case #" << test << ": " << k << '\n';
    }
    return 0;
}
