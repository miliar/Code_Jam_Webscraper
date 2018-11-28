#include <fstream>
#include <iostream>
#include <string.h>
using namespace std;
int main()
{
    int t, l, ans, count, i, c, m;
    int x[26], y[10];
    string a, temp;
    ofstream op;
    op.open("output.in");

    ifstream ip;
    ip.open("A-large.in");

    ip>>t;
    for(c=1;c<=t;c++)
    {
        ip>>a;
        l = a.size();
        temp = "";
        for(i=0;i<26;i++)
            x[i] = 0;
        for(i=0;i<l;i++)
        {
            m = (int)(a[i])-65;
            x[m]++;
        }
        //for(i=0;i<26;i++)
          //  cout<<x[i]<<" ";
        y[0] = x[25];
        if(x[25] != 0)
        {
            x[4] = x[4] - x[25];
            x[17] = x[17] - x[25];
            x[14] = x[14] - x[25];
            x[25] = 0;
        }

        y[2] = x[22];
        if(x[22] != 0)
        {
            x[19] = x[19] - x[22];
            x[14] = x[14] - x[22];
            x[22] = 0;
        }

        y[4] = x[20];
        if(x[20] != 0)
        {
            x[5] = x[5] - x[20];
            x[14] = x[14] - x[20];
            x[17] = x[17] - x[20];
            x[20] = 0;
        }

        y[5] = x[5];
        if(x[5] != 0)
        {
            x[8] = x[8] - x[5];
            x[21] = x[21] - x[5];
            x[4] = x[4] - x[5];
            x[5] = 0;
        }

        y[6] = x[23];
        if(x[23] != 0)
        {
            x[18] = x[18] - x[23];
            x[8] = x[8] - x[23];
            x[23] = 0;
        }

        y[8] = x[6];
        if(x[6] != 0)
        {
            x[4] = x[4] - x[6];
            x[8] = x[8] - x[6];
            x[7] = x[7] - x[6];
            x[19] = x[19] - x[6];
            x[6] = 0;
        }
        y[1] = x[14];
        y[3] = x[19];
        y[7] = x[21];
        y[9] = x[8];

        for(i=0;i<10;i++)
        {
            while(y[i]--)
            {
                temp += char(i+48);
            }
        }
        op<<"Case #"<<c<<": "<<temp<<"\n";
    }
    ip.close();
    op.close();
    return 0;
}
