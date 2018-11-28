#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

int warScore(set<double> naomi, set<double> ken)
{
    int score(0);
    set<double>::iterator iterChosenNaomi, iterChosenKen;
    while (!naomi.empty()) {
        iterChosenNaomi = naomi.begin();
        
        iterChosenKen = ken.lower_bound(*iterChosenNaomi);
        if (iterChosenKen == ken.end()) iterChosenKen = ken.begin();
        //cout << *iterChosenNaomi << " " << *iterChosenKen << endl;
        if (*iterChosenNaomi > *iterChosenKen) ++score;

        naomi.erase(iterChosenNaomi);
        ken.erase(iterChosenKen);
    
    }
    return score;
}

int deceitfulWarScore(set<double> naomi, set<double> ken)
{
    int score(0);
    set<double>::iterator iterChosenNaomi, iterChosenKen, iterSmallerKen;
    while (!naomi.empty())
    {
        iterChosenNaomi = naomi.end();
        for (set<double>::iterator iterNaomi(naomi.begin()); iterNaomi != naomi.end(); ++iterNaomi) { 
            iterSmallerKen = ken.lower_bound(*iterNaomi);
            if (iterSmallerKen != ken.begin()) {
                iterChosenNaomi = iterNaomi; break;
            }
        }
        double toldNaomi;
        if (iterChosenNaomi == naomi.end()) {
            iterChosenNaomi = naomi.begin();
            toldNaomi = *iterChosenNaomi;
        } else toldNaomi = *(--iterSmallerKen) - 1e-7;

        //cout << *iterChosenNaomi << endl;
        //cout << toldNaomi << endl;
        
        iterChosenKen = ken.lower_bound(toldNaomi);
        if (iterChosenKen == ken.end()) iterChosenKen = ken.begin();
        //cout << *iterChosenNaomi << " " << *iterChosenKen << endl;
        if (*iterChosenNaomi > *iterChosenKen) ++score;

        naomi.erase(iterChosenNaomi);
        ken.erase(iterChosenKen);
    
    }
    return score;
}

int main(int argc, char** argv)
{
    ifstream is(argv[1]);
    size_t nbCases;
    is >> nbCases;

    for (size_t ca(1); ca != nbCases+1; ++ca)
    {
        int nb;
        is >> nb;

        double weight;
        set<double> naomi,ken;
        for (size_t i(0); i != nb; ++i) {
            is >> weight;
            naomi.insert(weight);
        }
        for (size_t i(0); i != nb; ++i) {
            is >> weight;
            ken.insert(weight);
        }

        cout << "Case #" << ca << ": " << deceitfulWarScore(naomi,ken) << " " << warScore(naomi,ken) << endl;
    }
}

