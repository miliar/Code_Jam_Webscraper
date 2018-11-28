#include <iostream>
#include <fstream>
#include <string>

using namespace std;


fstream in, out;


void solve()
{
    int A, B, K;
    int res = 0;

    in >> A >> B >> K;
    for(int i = 0; i < A; ++i)
        for(int j = 0; j < B; ++j)
            if ((i & j) < K) ++res;

    out << res;
}

int main()
{
    in.open("in.txt");
    out.open("out.txt");

    int T;
    in >> T;

    for(int i = 0; i < T; ++i)
    {
        out << "Case #" << (i +1) << ": ";
        solve();
        out << endl;
    }

    return 0; 
}
