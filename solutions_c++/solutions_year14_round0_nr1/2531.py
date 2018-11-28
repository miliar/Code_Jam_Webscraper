#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <stdio.h>
#include <string>
#include <queue>
#include <iterator>

using namespace std;

int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);

    int T;

    cin >> T;

    for(int t = 0; t < T; ++t)
    {
        int R1, R2;

        vector< vector<int> > data1(4, vector<int>(4)), data2(4, vector<int>(4));

        cin >> R1;

        for(int i = 0; i < 4; ++i)
        {
            for(int j = 0; j < 4; ++j)
            {
                cin >> data1[i][j];
            }
        }


        cin >> R2;

        for(int i = 0; i < 4; ++i)
        {
            for(int j = 0; j < 4; ++j)
            {
                cin >> data2[i][j];
            }
        }

        vector<int> set1, set2, result(8);
        std::vector<int>::iterator it;

        for(int i = 0; i < 4; ++i)
        {
            set1.push_back(data1[R1 - 1][i]);
            set2.push_back(data2[R2 - 1][i]);
        }

        sort(set1.begin(), set1.end());
        sort(set2.begin(), set2.end());

        it = std::set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(), result.begin());

        result.resize(it - result.begin());

        if(!result.size())
        {
            //cout << "Volunteer cheated!" << endl;
            printf("Case #%d: Volunteer cheated!\n", t + 1);
        }
        else
        {
            if(result.size() == 1)
            {
                //cout << result[0] << endl;
                printf("Case #%d: %d\n",t + 1, result[0]);
            }
            else
            {
                //cout << "Bad magician!" << endl;
                printf("Case #%d: Bad magician!\n", t + 1);
            }
        }
    }

    return 0;
}