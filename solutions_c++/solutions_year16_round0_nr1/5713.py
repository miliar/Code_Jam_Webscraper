

#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>

using namespace std;
ofstream out("codejam.out");

set < int > Sol;

int T;

void prelucrateNumber(long long x)
{
    long long nr = x;
    while(nr)
    {
        Sol.insert(nr%10);
        nr/=10;
    }
}

void popHeap()
{
    while(!Sol.empty())
    {
        Sol.erase(Sol.begin());
    }
}
int main()
{
    ifstream in("codejam.in");
    in >> T;
    for(int test = 1; test <= T; ++test)
    {
        out << "Case " << "#" << test << ":" << " ";
        long long nr;
        popHeap();
        in >> nr;
        int i = 1;
        for(i = 1; i<=100; ++i)
        {
            long long secNumber = nr*i;
            prelucrateNumber(secNumber);
            if(Sol.size() == 10)
            {
                out << secNumber << '\n';
                break;
            }
        }
        if( i > 100)
        {
            out << "INSOMNIA" << '\n';
        }
    }

    return 0;

}
