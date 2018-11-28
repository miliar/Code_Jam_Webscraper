#include <iostream>
#include <fstream>
#include <cassert>
#include <cctype>

using namespace std;

int main()
{
    fstream in,out;
    in.open("large.in",fstream::in);
    out.open("large.out",fstream::out|fstream::app);
    int num;
    in >> num;
    for(int i = 0;i != num; ++i)
    {
        int max_s = 0;
        in >> max_s;
        int result = 0, sum = 0;
        for(int j = 0; j <= max_s; ++j)
        {
            char c;
            in >> c;
            assert(isdigit(c));
            int order = c - '0';
            sum += order;
            if(j + 1 - sum >result) result = j + 1 - sum;
        }
        out << "Case #" << i+1 << ": " << result <<endl;

    }
    return 0;
}
