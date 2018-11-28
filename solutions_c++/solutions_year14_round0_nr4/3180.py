#include <algorithm>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <set>

using namespace std;


int main ()
{
    ios_base::sync_with_stdio(false);
    ofstream cout ("D:\\outDLARGE.txt");
    ifstream cin ("D:\\DOWNLOADS\\D-large.in");
    //ifstream cin ("D:\\in.txt");
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int n;
        set <double> naomi, ken;
        cin >> n;
        double temp;
        for (int j = 0; j < n && cin >> temp; ++j)
            naomi.insert(temp);
        for (int j = 0; j < n && cin >> temp; ++j)
            ken.insert(temp);

        int unfair = 0, fair = 0;
        for (auto it1 = naomi.begin(), it2 = ken.begin();
             it1 != naomi.end();)
        {
            if (*it1 > *it2)
            {
                ++unfair;
                ++it2;
            }
            ++it1;
        }

        for (auto it = naomi.begin(); it != naomi.end();)
        {
            auto iter = ken.upper_bound(*it);
            if (iter == ken.end())
            {
                ++fair;
            }
            else
            {
                ken.erase(iter);
            }
            it = naomi.erase(it);
        }

        cout << "Case #" << i + 1 << ": " << unfair << " " << fair << endl;
    }

}
