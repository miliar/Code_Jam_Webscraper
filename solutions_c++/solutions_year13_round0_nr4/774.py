#include <cstdio>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <string.h>
#include <math.h>
#include <sstream>
#include <stack>

using namespace std;

typedef struct
{
    int type;
    int num;
    int key[201];
} chest_t;

stack<int> g_chestIndex;
chest_t chest[21];
int g_numOfChest = 0;

bool
func(bool* opened, int* keys, bool& back_flag, int& back_type)
{
    // 全ての箱が空いているかチェックする
    bool allOpened = true;
    for (int i = 1; i < g_numOfChest+1; i++)
    {
        if (opened[i] == false)
        {
            allOpened = false;
        }
    }
    if (allOpened == true) {
        return true;
    }

    for (int j = 1; j < g_numOfChest+1; j++)
    {
        if(opened[j] == false)
        {
            if (keys[chest[j].type] > 0)
            {
                keys[chest[j].type]--;
                opened[j] = true;
                if (chest[j].num > 0)
                {
                    for(int k = 0; k < 201; k++)
                    {
                        keys[k] += chest[j].key[k];
                    }
                }

                bool ret;
                ret = func(opened, keys, back_flag, back_type);
                if (ret == true)
                {
                    g_chestIndex.push(j); // この箱のIDをグローバルに保存して
                    return true;
                }
                else
                {
                    // 元に戻す
                    keys[chest[j].type]++;
                    opened[j] = false;
                    if (chest[j].num > 0)
                    {
                        for(int k = 0; k < 201; k++)
                        {
                            keys[k] -= chest[j].key[k];
                        }
                    }

                    if (back_flag == true)
                    {
                        if (back_type == chest[j].type)
                        {
                            back_flag = false;
                        }
                        else
                        {
                            return false;
                        }
                    }
                }
            }
            else
            {
                // 開いていない箱で開けられるようになるか調べる。
                bool flag_canopen = false;
                for (int i = 1; i < g_numOfChest+1; i++)
                {
                    if(opened[i] == false
                        && i != j)
                    {
                        if (chest[i].key[chest[j].type] > 0)
                        {
                            flag_canopen = true;
                        }
                    }
                }
                if (flag_canopen == false)
                {
                    back_flag = true;
                    back_type = chest[j].type;
                }
            }
        }
    }

    return false;
}

int main(int argc, const char **argv)
{
    if (argc != 2)
    {
        fprintf(stderr, "Error:%d\n", __LINE__);
        return -1;
    }

    ifstream fin(argv[1]);
    ofstream fout("out.txt");

    int T;
    fin >> T;

    for (int tc = 0; tc < T; tc++)
    {
        int K, N;
        fin >> K >> N;
        g_numOfChest = N;
        bool flag = false;

        for (int i = 0; i < N+1; i++)
        {
            for (int j = 0; j < 201; j++)
            {
                chest[i].key[j] = 0;
            }
        }

        chest[0].type = 0;
        chest[0].num = K;
        for (int i = 0; i < K; i++)
        {
            int tmp;
            fin >> tmp;
            chest[0].key[tmp]++;
        }

        for (int i = 1; i < N+1; i++)
        {
            fin >> chest[i].type;
            fin >> chest[i].num;
            for (int j = 0; j < chest[i].num; j++)
            {
                int tmp;
                fin >> tmp;
                chest[i].key[tmp]++;
            }
        }

        for (int i = 0; i < 201; i++)
        {
            int sum_chesttype = 0;
            int sum_keytype = 0;
            int j;
            for (j = 0; j < N+1; j++)
            {
                if (chest[j].type == i
                    && j != 0)
                {
                    sum_chesttype++;
                }
                sum_keytype += chest[j].key[i];
            }
            if (sum_chesttype > sum_keytype)
            {
                flag = true;
            }
        }

        fout << "Case #" << tc+1 << ":";

        if (flag == true)
        {
            fout << " IMPOSSIBLE";
        }
        else
        {
            bool opened[21];
            opened[0] = true;
            for (int i = 1; i < N+1; i++)
            {
                opened[i] = false;
            }

            bool r;
            bool back_flag = false;
            int back_type = 0;
            r = func(opened, chest[0].key, back_flag, back_type);
            if (r == true)
            {
                while (g_chestIndex.empty() == false)
                {
                    fout << " " << g_chestIndex.top();
                    g_chestIndex.pop();
                }
            }
            else
            {
                fout << " IMPOSSIBLE";
            }
        }

        fout << endl;
    }

    return (0);
}
