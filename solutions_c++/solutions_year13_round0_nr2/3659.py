#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream out("B-large.out");
    string line;
    int T;
    fin>>T;
    for(int i=0; i<T; i++)
    {
        string result = "YES";
        bool solved = false;
        bool re1, re2;
        re1 = re2 = true;
        int M, N;
        fin>>M>>N;
        int lawn[M][N];
        for(int j=0; j<M; j++)
        {
            for(int k=0; k<N; k++)
            {
                fin>>lawn[j][k];
            }
        }
        for(int j=0; !solved&&j<M; j++)
        {
            for(int k=0; !solved&&k<N; k++)
            {
                //lawn[j][k];
                re1 = re2 = true;
                for(int lie=0; lie<N; lie++)
                {
                    if(lawn[j][k]<lawn[j][lie])
                    {
                        re1 = false;
                        break;
                    }

                }
                for(int hang=0; hang<M; hang++)
                {
                    if(lawn[j][k]<lawn[hang][k])
                    {
                        re2 = false;
                        break;
                    }
                }
                if(re1==false && !re2)
                {
                    result = "NO";
                    solved = true;
                }
            }
        }
        out<<"Case #"<<i+1<<": "<<result<<endl;

    }
    fin.close();
    out.close();
    return 0;
}
