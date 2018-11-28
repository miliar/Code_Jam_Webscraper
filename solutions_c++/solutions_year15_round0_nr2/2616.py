#include <iostream>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int main()
{
    freopen("D:\\GoogleCodeJam\\in.txt","r",stdin);
    freopen("D:\\GoogleCodeJam\\out.txt","w",stdout);

    int TestNum = 0;
    cin >> TestNum;
    for (int testCase = 0;testCase < TestNum;testCase++)
	{
        int D = 0;
        cin >> D;
        vector<int> start;

        int totalP = 0;
        for (int i=0;i<D;i++)
        {
            int tem;
            cin >> tem;
            start.push_back(tem);
            totalP += tem;
        }

        sort(start.begin(),start.end(),greater<int>());

        vector<vector<int>> cur;
        vector<vector<int>> nex;
        cur.push_back(start);
        int result = 0;
        if (start[0] == 2)
            result = 2;
        else if (start[0] == 1)
            result = 1;
        else
        for (int r = 1;;r++)
        {
            bool canEnd = false;
            vector<int> temp0;
            vector<int> temp;
            for (int i=0;i<cur.size();i++)
            {
                // eat one day

                for (int j=0;j<cur[i].size();j++)
                {
                    if (cur[i][j] > 0)
                        temp0.push_back(cur[i][j]-1);
                }
                sort(temp0.begin(),temp0.end(),greater<int>());
                nex.push_back(temp0);
                temp0.clear();
                // split max
                for (int k=1;k <= cur[i][0]/2;k++)
                {

                    temp.push_back(k);
                    temp.push_back(cur[i][0]-k);
                    for (int j=1;j<cur[i].size();j++)
                    {
                        temp.push_back(cur[i][j]);
                    }
                    sort(temp.begin(),temp.end(),greater<int>());
                    nex.push_back(temp);
                    temp.clear();
                }
            }
            cur.clear();
            for (int i=0;i<nex.size();i++)
            {
                if (nex[i][0] == 2)
                {
                    canEnd = true;
                    result = r + 2;

                    break;
                }
                else if (nex[i][0] == 1)
                {
                    canEnd = true;
                    result = r + 1;

                    break;
                }

                cur.push_back(nex[i]);
            }
            nex.clear();
            if (canEnd)
            {
                break;
            }
        }
        nex.clear();
        start.clear();
        cur.clear();
        if (testCase != 0) cout << endl;
        cout << "Case #" << (testCase + 1) << ": " << result;
	}
    return 0;
}
