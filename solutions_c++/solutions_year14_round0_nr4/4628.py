#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORI(i,b) FOR(i,0,b)

int ffbt(double d,vector<double>* vec)
{
    FORI(i,vec->size())
    {
        if(vec->at(i)>d) return i;
    }
    return -1;
}

int main()
{
    ifstream input("input.in",ifstream::in);
    ofstream output("output.out",ofstream::out);

    int t;
    input >> t;
    FORI(i,t)
    {
        int N;
        input >> N;
        vector<double> Naomi;
        vector<double> Ken;
        double tmp;
        FORI(j,N){input>>tmp;Naomi.push_back(tmp);}
        FORI(j,N){input>>tmp;Ken.push_back(tmp);}

        std::sort(Naomi.begin(),Naomi.end());
        std::sort(Ken.begin(),Ken.end());

        vector<double> WarNaomi = Naomi;
        vector<double> WarKen = Ken;

        int iN = 0;
        int iK = 0;
        bool b;
        if(Naomi.back() < Ken.back()) b = true;
        else b = false;
        while(b)
        {
            Naomi.erase(Naomi.begin());
            Ken.pop_back();
            iK++;
            if(iK >= N || Naomi.back() > Ken.back()) b=false;
        }

        if(iK < N)
        {
            int ind = ffbt(Ken.at(0),&Naomi);
            while(ind>=0)
            {
                Naomi.erase(Naomi.begin()+ind);
                Ken.erase(Ken.begin());
                iN++;
                if(Naomi.size()<=0)ind=-1;
                else ind = ffbt(Ken.at(0),&Naomi);
            }

        }
        int x = iN;
        iN = 0;
        iK = 0;
        FORI(j,N)
        {
            int index = ffbt(WarNaomi.at(j),&WarKen);
            if(index >= 0)
            {
                WarKen.erase(WarKen.begin()+index);
                iK++;
            }
            else iN++;
        }
        int y = iN;
        output << "Case #" << i+1 << ": " << x << " " << y << endl;

    }
    return 0;
}
