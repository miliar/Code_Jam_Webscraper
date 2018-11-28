#include <iostream>
#include <cstring>
#include <fstream>
#define cin fin
#define cout fout
using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("output.txt");

int main()
{
    int c, n, t, tmp, finish=0;
    cin >> c;
    bool flag[10];
    for (int i=1; i<=c; i++)
    {
        finish=0;
        memset(flag, 0, sizeof(flag));
        cin >> n;
        cout << "CASE #" << i << ": ";
        if (n==0)
            cout << "INSOMNIA";
        else
        {
            for ( t=n; finish<10; t+=n)
            {
                tmp=t;
                while (tmp)
                {
                    if (!flag[tmp%10])
                    {
                        flag[tmp%10]=true;
                        finish++;
                    }
                    tmp/=10;
                }
            }
            t-=n;
            cout << t;
        }

        cout << endl;
    }
    return 0;
}
