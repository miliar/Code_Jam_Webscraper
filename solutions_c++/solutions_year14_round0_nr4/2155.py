#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
    ifstream fin("D.in");
    ofstream fout("D.out");
    int T, N;
    fin >> T;
    for (int testnum = 1; testnum <= T; testnum++)
    {
        fin >> N;
        vector<double> Nao, Ken;
        double d;
        for (int i = 0; i < N; i++)
        {
            fin >> d;
            Nao.push_back(d);
        }
        for (int i = 0; i < N; i++)
        {
            fin >> d;
            Ken.push_back(d);
        }
        sort(Nao.begin(), Nao.end());
        sort(Ken.begin(), Ken.end());
        int deceit = 0, war = N;
        int currnao, currken = 0;
        for (currnao = 0; currnao < N; currnao++)
        {
            if (Ken[currken] < Nao[currnao])
            {
                deceit++;
                currken++;
            }

        }
        currnao = 0;
        currken = 0;
        while ((currnao < N) && (currken < N))
        {
            if (Ken[currken] > Nao[currnao])
            {
                war--;
                currnao++;
            }
            currken++;
        }
        fout << "Case #" << testnum << ": " << deceit << ' ' << war << endl;
    }
}