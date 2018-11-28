#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int minkeres(vector<int>& V)
{
    int e=*max_element(V.begin(),V.end());
    if (1==e){return 1;}
    if (2==e){return 2;}

    int mint=1000000;
    for (int i=2; i<=e/2; i++)
    {
        vector<int> Temp(0);
        for (int j=0; j<V.size(); j++){Temp.push_back(V[j]);}
        Temp.erase(max_element(Temp.begin(),Temp.end()));
        Temp.push_back(i);
        Temp.push_back(e-i);
        int uj=minkeres(Temp)+1;
        if (uj<mint){mint=uj;}
    }
    return (min(mint,e));
}

int main()
{
    ifstream fbe("B-small-attempt2.in");
    //ifstream fbe("Teszt.txt");
    ofstream fki("ki.txt");
    int t;
    fbe>>t;
    for (int i=1; i<=t; i++)
    {
        int D;
        fbe>>D;
        vector<int> Palacs(D);
        for (int j=0; j<D; j++)
        {
            fbe>>Palacs[j];
        }
        fki<<"Case #"<<i<<": "<<minkeres(Palacs)<<endl;
    }


    return 0;
}
