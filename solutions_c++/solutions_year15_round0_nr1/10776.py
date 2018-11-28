#include <iostream>
#include <fstream>

using namespace std;

int T, Smax;

ifstream ifs("in.txt");
ofstream ofs("out.txt");

// 3 0001
//   0123
int main()
{
    ifs >> T;
    char ch;    
    for (int i = 0; i < T; ++i)
    {
        ifs >> Smax;
        int res = 0, total = 0, tmp = 0;        
        for (int j = 0; j < Smax + 1; ++j)
        {
            ifs >> ch;
            tmp =  max(0, j - total);
            res += tmp;
            total += ch - 48 + tmp;            
        }
        ofs << "Case #" << i+1 <<": " << res << endl;
    }    
    return 0;
}
