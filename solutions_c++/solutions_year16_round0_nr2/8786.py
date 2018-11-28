#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    fstream f;
    fstream o;
    f.open("B-large.in", ios::in);
    o.open("output.txt", ios::out);
    int T(0);
    string N;
    f >> T;
    for(int a(1); a <= T; a++)
    {
        f >> N;
        int b = 0, ref = 0;
        int sum = 1;
        while(b < N.length())
        {
            if(N[ref] != N[b])
            {
                sum ++;
                ref = b;
            }
            b++;
        }
        if(N[N.length()-1] == '+')
                sum --;
        o << "Case #" << a << ": " << sum << endl;
    }
    f.close();
    o.close();
}