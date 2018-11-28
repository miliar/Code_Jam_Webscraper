#include <iostream>
#include <list>
#include <algorithm>

using namespace std;

int deceitful(list<double> naomi, list<double> ken)
{
    int naomipts = 0;
    while(!naomi.empty())
    {
        double minnaomi = *naomi.begin();
        naomi.erase(naomi.begin());
        if(minnaomi < *ken.begin())
        {
            ken.erase(--ken.end());
        }
        else
        {
            list<double>::iterator best = ken.begin();
            for(list<double>::iterator it = ken.begin(); it != ken.end(); ++it)
            {
                if(*it > minnaomi)
                    break;
                else
                    best = it;
            }
            ken.erase(best);
            naomipts++;
        }
    }
    return naomipts;
}

int straight(list<double> naomi, list<double> ken)
{
    int naomipts = 0;
    while(!naomi.empty())
    {
        double naomival = *naomi.begin();
        naomi.erase(naomi.begin());

        list<double>::iterator kenbest = ken.begin();
        for(; kenbest != ken.end(); ++kenbest)
            if(*kenbest > naomival)
                break;

        if(kenbest == ken.end())
        {
            naomipts++;
            ken.erase(ken.begin());
        }
        else
            ken.erase(kenbest);
    }
    return naomipts;
}

void testCase()
{
    int N;
    cin >> N;
    list<double> naomi;
    for(int i=0; i<N; i++)
    {
        float m;
        cin >> m;
        naomi.push_back(m);
    }
    list<double> ken;
    for(int i=0; i<N; i++)
    {
        float m;
        cin >> m;
        ken.push_back(m);
    }
    naomi.sort();
    ken.sort();
    cout << deceitful(naomi, ken) << " " << straight(naomi, ken) << endl;
}

int main()
{
    int t;
    cin >> t;
    for(int i=0; i<t; i++)
    {
        cout << "Case #" << i+1 << ": ";
        testCase();
    }
}


