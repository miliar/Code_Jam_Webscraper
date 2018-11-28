#include <iostream>
#include <fstream>
using namespace std;

fstream file;
fstream output;

char tab[1009];

int main()
{
    file.open("in.in");
    output.open("out1.txt");

    int t, n, a;
    file >> t;
    for(int i = 0; i < t; i ++)
    {
        int ans = 0; int ppl = 0;
        file >> n;
        file >> tab;
        for(int j = 0; j <= n; j++)
        {
            if(ppl < j)
            {
                ppl += 1;
                ans += 1;
            }
            ppl += tab[j] - '0';
        }
        output << "Case #" << i+1 << ": " << ans << "\n";
    }
    return 0;
}
