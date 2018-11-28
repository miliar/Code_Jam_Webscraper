#include <cstdio>
#include <deque>
#include <fstream>
#include <iostream>
#include <set>

using namespace std;

ifstream fin("d.in");
ofstream fout("d.out");

int T, Num;
set<double> K, N, Ken, Naomi;

int main()
{
    fin >> T;

    for(int t = 1; t <= T; t++)
    {
        fin >> Num;
        Naomi.clear();
        Ken.clear();

        for(int i = 0; i < Num; i++)
        {
            double x;
            fin >> x;
            Naomi.insert(x);
        }
        for(int i = 0; i < Num; i++)
        {
            double x;
            fin >> x;
            Ken.insert(x);
        }

        int ptsA = 0, ptsB = 0;

        for(auto it = Naomi.begin(); it != Naomi.end(); it++)
            N.insert(*it);
        for(auto it = Ken.begin(); it != Ken.end(); it++)
            K.insert(*it);

        while(!N.empty())
        {
            double x = *N.begin();
            N.erase(N.begin());
            auto it = K.upper_bound(x);
            if(it == K.end())
            {
                ptsA++;
                K.erase(K.begin());
            }
            else
                K.erase(it);
        }

        for(auto it = Naomi.begin(); it != Naomi.end(); it++)
            K.insert(*it);
        for(auto it = Ken.begin(); it != Ken.end(); it++)
            N.insert(*it);

        while(!N.empty())
        {
            double x = *N.begin();
            N.erase(N.begin());
            auto it = K.upper_bound(x);
            if(it == K.end())
                K.erase(K.begin());
            else
            {
                K.erase(it);
                ptsB++;
            }
        }

        fout << "Case #" << t << ": " << ptsB << " " << ptsA << "\n";
    }
}
