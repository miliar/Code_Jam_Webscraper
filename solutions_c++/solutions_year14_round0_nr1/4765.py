#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORI(i,b) FOR(i,0,b)


int main()
{
    ifstream input("input.in",ifstream::in);
    ofstream output("output.out",ofstream::out);

    int t;
    input >> t;
    FORI(i,t)
    {
        int l1, l2;
        int set1[4][4];
        int set2[4][4];
        input >> l1;
        FORI(j,4)
        {
            FORI(k,4)
            {
                input >> set1[j][k];
            }
        }
        input >> l2;
        FORI(j,4)
        {
            FORI(k,4)
            {
                input >> set2[j][k];
            }
        }

        vector<int> res;
        FORI(j,4)
        {
            FORI(k,4)
            {
                if(set1[l1-1][j]==set2[l2-1][k]) res.push_back(set1[l1-1][j]);
            }
        }
        output << "Case #" << i+1 << ": " ;
        switch (res.size())
        {
        case 0:
            output << "Volunteer cheated!" << endl;
            break;
        case 1:
            output << res.at(0) << endl;
            break;
        default:
            output << "Bad magician!" << endl;
        }
    }
    return 0;
}
