#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


int multTable[5][5] =
{
    {0,0,0,0,0},
    {0,1,2,3,4},
    {0,2,-1,4,-3},
    {0,3,-4,-1,2},
    {0,4,3,-2,-1}
};

using namespace std;

int main()
{
    freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);
    int nbT;
    cin >> nbT;
    for (int t = 1; t <= nbT; t++)
    {
        cout << "Case #" << t << ": ";

        int len, nbTimes;
        string s;
        cin >> len >> nbTimes >> s;
        vector<int> idsStr;
        idsStr.reserve(len*nbTimes);
        int corr[256];
        corr['i'] = 2;
        corr['j'] = 3;
        corr['k'] = 4;

        for (int i = 0; i < nbTimes; i++)
        {
            for (int j = 0; j < len; j++)
                idsStr.push_back(corr[s[j]]);

        }

        char corrBis[5] = {'a', '1', 'i', 'j', 'k'};

        int lenTotal = len*nbTimes;
        int cur1 = 1;
        bool found = false;
        for (int p1 = 0; p1 < lenTotal-2; p1++)
        {
            int signCur = 1;
            if (cur1 < 0)
            {
                cur1 = -cur1;
                signCur = -1;
            }
            int signP1 = 1;

            int nbP1 = idsStr[p1];
            if (nbP1 < 0)
            {
                nbP1 = -nbP1;
                signP1 = -1;
            }
            cur1 = signCur*signP1*multTable[cur1][nbP1];
            /*if (signCur == -1)
                cout << '-';
            cout << corrBis[cur1] << "==>" <<cur1 << endl;*/

            if (cur1 == 2)
            {
                int cur2 = 1;
                for (int p2 = p1+1; p2 < lenTotal-1; p2++)
                {
                    int signCur2 = 1;
                    if (cur2 < 0)
                    {
                        cur2 = -cur2;
                        signCur2 = -1;
                    }

                    int signP2 = 1;
                    int nbP2 = idsStr[p2];
                    if (nbP2 < 0)
                    {
                        nbP2 = -nbP2;
                        signP2 = -1;
                    }
                    cur2 = signCur2*signP2*multTable[cur2][nbP2];
                    /*if (signCur == -1)
                        cout << '-';
                    cout << corrBis[cur2] << " LII ==>" << cur2 << endl;*/

                    if (cur2 == 3)
                    {
                        int cur3 = 1;
                        for (int p3 = p2+1; p3 < lenTotal; p3++)
                        {
                            int signCur3 = 1;
                            if (cur3 < 0)
                            {
                                cur3 = -cur3;
                                signCur3 = -1;
                            }
                            int signP3 = 1;
                            int nbP3 = idsStr[p3];
                            if (nbP3 < 0)
                            {
                                nbP3 = -nbP3;
                                signP3 = -1;
                            }
                            cur3 = signCur3*signP3*multTable[cur3][nbP3];
                        }
                        if (cur3 == 4)
                        {
                            found = true;
                            p2 = lenTotal;
                            p1 = lenTotal;
                        }

                    }
                }
            }


        }

        cout << (found?"YES\n":"NO\n");


    }


    return 0;
}
