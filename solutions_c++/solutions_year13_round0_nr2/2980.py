#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>

using namespace std;


int check (vector< vector <int> > &lawn, set<int> &height)
{
    if (lawn.size() == 1)
        return 1;
    bool allo = true;
    for (int i = 0; i < lawn.size(); i++)
        if(lawn[i].size() != 1)
            allo = false;
    if(allo)
        return 1;

    bool foue = false;
    int iter = 0;
    while(height.size() != 0)
    {
        int sm = *height.begin();
        for(int i = 0; i < lawn.size(); i++)
        {
            if (lawn[i][0] == sm && lawn[i][lawn[i].size()-1] == sm)
            {
                foue = true;
                bool l = true;
                for (int j = 0; j < lawn[i].size(); j++)
                {
                    if (lawn[i][j] != sm)
                    {
                        l = false;
                        break;
                    }
                }
                if(l)
                {
                    lawn.erase(lawn.begin()+i);
                    i --;
                }
            }
        }

        if (lawn.size() == 0)
            return 1;

        for (int i = 0; i < lawn[0].size(); i++)
        {
            if (lawn[0][i] == sm && lawn[lawn.size() -1][i] == sm)
            {
                foue = true;
                bool r = true;
                for (int j = 0; j < lawn.size(); j++)
                {
                    if (lawn[j][i] !=sm)
                    {
                        r = false;
                        break;
                    }
                }
                if (r)
                {
                    for (int k = 0; k < lawn.size(); k++)
                    {
                        lawn[k].erase(lawn[k].begin()+i);
                    }
                    i --;
                }
            }
        }

        if (!foue && iter == 0)
            return 0;
        height.erase(height.begin());
        iter ++;
    }

    if (lawn.size() > 0)
        return 0;
    return 1;
}




int main()
{
    ifstream f1 ("input");
    ofstream f2("output");

    int cases;
    f1 >> cases;

    for (int i = 0; i < cases; i++)
    {
        int x, y;
        f1 >> x >> y;
        set <int> height;
        vector < vector <int> > lawn;
        for (int j = 0; j < x; j++)
        {
            vector <int > row;
            for (int k = 0; k < y; k++)
            {
                int temp;
                f1 >> temp;
                height.insert(temp);
                row.push_back(temp);
            }
            lawn.push_back(row);
        }
        int s = check (lawn, height);
        f2 <<"Case #" << i + 1 << ": ";
        if ( s == 0)
            f2 <<"NO"<<endl;
        else
            f2 <<"YES"<<endl;

    }
    return 0;
}




