#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
using namespace std;
ifstream fin("in.txt");
ofstream fout("out.txt");

//#define fin cin
//#define fout cout

int main()
{
    int t;
    fin >> t;
    for(int cas = 1; cas <= t; cas++)
    {

        fout << "Case #" << cas << ": ";
        long long n;
        fin >> n;
        if(n == 0)
        {
            fout << "INSOMNIA" <<endl;
            continue;
        }
        int mark[20] = {0};
        for(long long i = 1;i<=1000;i++)
        {
            long long ans = i * n;
            while(ans)
            {
                mark[ans % 10] = 1;
                ans /= 10;
            }
            int flag = 1;
            for(int j = 0; j <= 9; j++)if(!mark[j])
            {
                flag = 0;
                break;
            }
            if(flag)
            {
                fout << i * n << endl;
                break;
            }
        }
    }
    return 0;
}
