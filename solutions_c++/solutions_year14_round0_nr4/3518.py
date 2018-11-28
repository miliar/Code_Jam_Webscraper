#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int T;
    vector<long double> Naomi, Ken;
    int howMany, war, dwar;

    cin >> T;
    for(int cs = 1; cs <= T; cs++)
    {
        Naomi.clear();
        Ken.clear();
        war = dwar = 0;
        
        cin >> howMany;
        for(int n = 0; n < 2; n++)
        {
            for(int i = 0; i < howMany; i++)
            {
                long double temp;
                cin >> temp;
                if(n == 0)
                {
                    Naomi.push_back(temp);
                }
                else
                {
                    Ken.push_back(temp);
                }
            }
        }

        sort(Naomi.begin(), Naomi.end());
        sort(Ken.begin(), Ken.end());

        // Normal War
        int kenWarWin = 0;
        for(int i = 0, naomiCt = 0; i < Ken.size() && naomiCt < Naomi.size(); i++)
        {
            if(Naomi[naomiCt] < Ken[i])
            {
                kenWarWin++;
                naomiCt++;
            }
        }

        war = Ken.size() - kenWarWin;

        // Deceitful war
        while(Naomi.size() != 0)
        {
            if(Naomi[0] < Ken[0])
            {
                Naomi.erase(Naomi.begin());
                Ken.erase(Ken.end() - 1);
            }
            else
            {
                Naomi.erase(Naomi.begin());
                Ken.erase(Ken.begin());
                dwar++;
            }
        }

        cout << "Case #" << cs << ": " << dwar << " " << war << endl;
    }
    return 0;
}