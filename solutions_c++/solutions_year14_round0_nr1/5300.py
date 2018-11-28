#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    ifstream in( "a-small-attempt0.in" );
    ofstream out( "a-out.txt" );
    int T;
    in >> T;
    for (int i=1; i<=T; i++)
    {
        vector<int> poss(22);
        for (int j=0; j<2; j++)
        {
            int row;
            in >> row;
            for (int r=1; r<=4; r++) {
                int x1, x2, x3, x4;
                in >> x1 >> x2 >> x3 >> x4;
                if (r == row) {
                    poss[x1]++;
                    poss[x2]++;
                    poss[x3]++;
                    poss[x4]++;
                }
            }
        }
        int num = 0;
        int ans = 0;
        for (int j=1; j<=16; j++)
        {
            if (poss[j]==2)
            {
                num++;
                ans = j;
            }
        }
        if (num == 0)
            out << "Case #" << i << ": Volunteer cheated!"  << endl;
        else if (num > 1)
            out << "Case #" << i << ": Bad magician!"  << endl;
        else
            out << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}
