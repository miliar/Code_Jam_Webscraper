//Problem D. Freeform Factory
//By: phoenixinter@gmail.com
//May 28, 2016

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool gr[25][25], newgr[25][25];
bool valid;
int n;
bool usedMachine[25];

int main()
{
    int t, kase = 0;
    cin >> t;
    while (t--)
    {
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            string str;
            cin >> str;
            for (int j = 0; j < n; j++)
                gr[i][j] = (str[j] == '1');
        }
        int ans = INT_MAX;
        for (int bitmask = 0; bitmask < (1 << (n * n)); bitmask++)
        {
            memset(newgr, false, sizeof(newgr));
            bool valid = true;
            int numAdd = 0;
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    int idx = i * n + j;
                    bool f = false;
                    if (bitmask & (1 << idx)) f = true;
                    newgr[i][j] = f;
                    if (!f && gr[i][j])
                    {
                        valid = false;
                        goto end;
                    }
                    if (f && !gr[i][j]) numAdd++;
                }
            }
        end: if (!valid) continue;
            vector<int> orderPeople, orderMachine;
            for (int i = 0; i < n; i++)
            {
                orderPeople.push_back(i);
                orderMachine.push_back(i);
            }
            bool blocked = false, hasValid = false;
            do
            {
                /*
                cout << "People: ";
                for (int i = 0; i < n; i++)
                    cout << orderPeople[i] << " ";
                cout << endl;
                */
                do
                {
                    /*
                    cout << "Machine: ";
                    for (int i = 0; i < n; i++)
                        cout << orderMachine[i] << " ";
                    cout << endl;
                    */
                    bool used[25], validMachineOrder = true;
                    memset(used, false, sizeof(used));
                    for (int i = 0; i < n; i++)
                    {
                        int peopleIdx = orderPeople[i];
                        int machineIdx = orderMachine[i];
                        int cnt = 0;
                        for (int j = 0; j < n; j++)
                            if (newgr[peopleIdx][j] && !used[j])
                                cnt++;
                        if (cnt == 0)
                            blocked = true;
                        if (!newgr[peopleIdx][machineIdx])
                        {
                            validMachineOrder = false;
                            break;
                        }
                        used[machineIdx] = true;
                        if (validMachineOrder) hasValid = true;
                    }
                    //cout << blocked << " " << hasValid << endl;
                } while (next_permutation(orderMachine.begin(), orderMachine.end()));
            } while (next_permutation(orderPeople.begin(), orderPeople.end()));
            if (!blocked && hasValid)
                ans = min(ans, numAdd);
        }
        cout << "Case #" << ++kase << ": " << ans << endl;
    }
    return 0;
}