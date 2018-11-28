#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

int K, N;

vector<vector<int > > chests;
vector<int> requiredKeys; 
vector<int> keys;  

const int NOT_OPENED = 0;
const int OPENED = 1;
vector<int> chestOpened;
int chestOpenedCount;
int openSteps[256];

map<vector<int>, int> memo;

int treasure(const int step, const int chest)
{
    openSteps[step] = chest;
    chestOpened[chest] = 1;
    ++chestOpenedCount;
    if (chestOpenedCount == N)
        return 1;

    if (memo.count(chestOpened) != 0)
    {
        chestOpened[chest] = 0;
        --chestOpenedCount;
        return memo[chestOpened];
    }

    for (int i = 0; i < (int)chests[chest].size(); ++i)
        keys.push_back(chests[chest][i]);

    for (int i = 1; i <= N; ++i)
    {
        if (chestOpened[i] == 1) continue;

        vector<int>::iterator iter(find(keys.begin(), keys.end(), requiredKeys[i]));
        if (iter != keys.end())
        {
            iter = keys.erase(iter);
            int result = treasure(step + 1, i);
            if (result == 1)
                return 1;

            keys.push_back(requiredKeys[i]);
        }
    }
    chestOpened[chest] = 0;
    --chestOpenedCount;
    for (int i = 0; i < (int)chests[chest].size(); ++i)
        keys.erase(find(keys.begin(), keys.end(), chests[chest][i]));
    
    return memo[chestOpened] = 0;
}

int main ()
{
    int T;
    int caseCount = 0;
    cin >> T;
    while ( T-- )
    {
        caseCount++;
        requiredKeys.resize(1);
        keys.clear(); 

        cin >> K >> N;

        chests.resize(N + 1);
        for (int i = 0; i <= N; ++i)
            chests[i].clear();

        for (int i = 1; i <= K; ++i)
        {
            int key;
            cin >> key;
            keys.push_back(key);
        }
        for (int i = 1; i <= N; ++i)
        {
            int requiredKey;
            cin >> requiredKey;
            requiredKeys.push_back(requiredKey);

            int Ki;
            cin >> Ki;
            for (int j = 0; j < Ki; ++j)
            {
                int containedKey;
                cin >> containedKey;
                chests[i].push_back(containedKey);
            }
        }

        /*REMOVE
        cout << "K = " << K << " N = " << N << endl;
        cout << "keys:";
        for (int i = 0; i < keys.size(); ++i)
            cout << " " << keys[i];
        cout << endl;
        for (int i = 1; i <= N; ++i)
        {
            cout << "chest " << i << "(" << requiredKeys[i] << "):";
            for (int j = 0; j < chests[i].size(); ++j)
                cout << " " << chests[i][j];
            cout << endl;
        }
        //*/

        chestOpened.resize(N + 1);
        chestOpened.assign(N + 1, 0);
        chestOpenedCount = 0;
        
        memo.clear();
        int result = 0;
        for (int i = 1; i <= N; ++i)
        {
            vector<int>::iterator iter(find(keys.begin(), keys.end(), requiredKeys[i]));
            if (iter != keys.end())
            {
                iter = keys.erase(iter);
                result = treasure(0, i);
                if (result == 1)
                    break;
                keys.insert(iter, requiredKeys[i]);
            }
        }

        cout << "Case #"
             << caseCount
             << ": ";
        
        if (result == 0)
            cout << "IMPOSSIBLE";
        else
        {
            cout << openSteps[0];
            for (int i = 1; i < N; ++i)
                cout << " " << openSteps[i];
        }
        cout << endl;
    }
    return 0;
}