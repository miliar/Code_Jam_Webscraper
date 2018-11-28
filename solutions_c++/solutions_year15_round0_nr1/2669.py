#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main()
{
    int test;

    fin>>test;

    for(int j=1;j<=test;j++)
    {
        int n;

        fin>>n;

        char str[2000];
        fin>>str;

        int cur_standing=(int)str[0]-(int)('0');
        int extra=0;

        for(int i=1;i<=n;i++)
        {
            int val=(int)str[i]-(int)('0');

            if(cur_standing>=i)
                cur_standing=cur_standing+val;
            else
            {
                extra=extra+(i-cur_standing);
                cur_standing=cur_standing+val+(i-cur_standing);
            }
        }

        fout<<"Case #"<<j<<": "<<extra<<endl;


    }
    return 0;
}
