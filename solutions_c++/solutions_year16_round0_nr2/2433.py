#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

int w,t,i,j,nr,k;
string s;

void sw(char &x)
{
    if (x=='-')
        x='+';
    else x='-';
}

int main()
{
    ifstream f("in.txt");
    ofstream g("out.txt");
    f >> t;
    for (w=1;w<=t;w++)
    {
        g << "Case #" << w << ": ";
        nr=0;
        f >> s;
        for (i=s.size()-1;i>=0;i--)
            if (s[i]=='-')
            {
                if (s[0]=='+')
                {
                    nr++;
                    j=0;
                    while (s[j+1]=='+')
                        j++;
                    for (k=0;k<=j;k++)
                        sw(s[k]);
                }
                nr++;
                for (j=0;j<=i;j++)
                {
                    sw(s[j]);
                }
                for (j=0;j<=i/2;j++)
                    swap(s[j],s[i-j]);
            }
        g << nr << "\n";
    }
    return 0;
}
