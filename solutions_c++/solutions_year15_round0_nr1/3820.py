#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

const int MAX_S = 1001;
const int MAX_SEQ = 101;
int main()
{
    int T;
    int Smax[MAX_SEQ];
    char seq[MAX_SEQ][MAX_S];
//    int seq_int[MAX_S];

    fstream o;
    o.open("D:\\MyProject\\QtCPP\\GCJ2015\\0411A\\a.in", ios::in);
    o>>T;

    for (int i=0;i < T;i++)
    {

        o>>Smax[i];
        o>>seq[i];

    }
    o.close();

    fstream f("D:\\MyProject\\QtCPP\\GCJ2015\\0411A\\a.out", ios::out);

    for (int i=0;i < T;i++)
    {

        if (Smax[i] == 0)
            f<<"Case #"<<i+1<<": "<<0;
        else
        {
            int zero = int(seq[i][0]) - 48;
            int key = zero;
            int ans = 0;
            int max = Smax[i];
            if (zero >= max)
                f<<"Case #"<<i+1<<": "<<0;
            else
            {
                for (int j=1;j <= max;j++)
                {
                    int s;
                    s = int(seq[i][j]) - 48;
                    if (s > 0)
                    {
                        if (key < j)
                        {
                            ans = ans + (j - key);
                            key = s + j;
                        }
                        else
                            key = key + s;
                    }
                }
                f<<"Case #"<<i+1<<": "<<ans;
            }
        }
        f<<endl;
    }
    f.close();

//    for (int i=0;i < T;i++)
//    {
//        for (int j=0;j <= Smax[i];j++)
//            cout<<seq[i][j]<<" ";
//        cout<<endl;
//    }
}
