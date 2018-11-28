#include <fstream>
#include <cstring>

using namespace std;

int main()
{
    int t;
    ifstream f1("in.in");
    ofstream f2("out.out");
    f1>>t;
    for(int c=1;c<=t;c++)
    {
        char intrare[101], lc;
        int i, ans=0;
        f2 << "Case #" << c << ": ";

        f1 >> intrare;


        if(intrare[strlen(intrare)-1] == '-')
            ans = 1;
        lc = intrare[strlen(intrare)-1];
        for(i=strlen(intrare)-2; i>=0; i--)
        {
            if(intrare[i] != lc)
            {
                ans ++;
                lc=intrare[i];
            }
        }

        f2 << ans << "\n";
    }
    return 0;
}
