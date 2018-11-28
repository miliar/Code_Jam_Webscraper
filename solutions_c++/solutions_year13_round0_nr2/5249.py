#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORI(i,b) FOR(i,0,b)


int main()
{
    ifstream input("input.in",ifstream::in);
    ofstream output("output.out",ofstream::out);

    int t;
    input >> t;
    FORI(i,t)
    {
        int n,m;
        input >> n;
        input >> m;
        int lawn[n][m];
        char tmp;
        input.get(tmp);
        FORI(j,n)
        {
            FORI(k,m)
            {
                input >> lawn[j][k];
            }
            input.get(tmp);
        }

        bool b=true;
        FORI(j,n)
        {
            FORI(k,m)
            {
                bool bw=true;
                int imaxl = 0;
                int imaxc = 0;
                FORI(l,m)
                {
                    if(lawn[j][l]>imaxl)
                        imaxl = lawn[j][l];
                }
                FORI(l,n)
                {
                    if(lawn[l][k]>imaxc)
                        imaxc = lawn[l][k];
                }
                if(imaxl > lawn[j][k] && imaxc > lawn[j][k])
                {
                    b = false;
                    break;
                }
            }
            if(!b) break;
        }
        char a[4];
        if(b) strcpy(a,"YES");
        else  strcpy(a,"NO");
        output << "Case #" << i+1 << ": " << a << endl;
    }
    return 0;
}
