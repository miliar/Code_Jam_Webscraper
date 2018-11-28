#include <iostream>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <cstdlib>
#include <set>
#include <map>
#include <fstream>
#include <bitset>

#define PI 3.14159265359

using namespace std;

int table[5][5] = {{0, 0, 0, 0, 0}, {0, 1, 2, 3, 4}, {0, 2, -1, 4, -3}, {0, 3, -4, -1, 2}, {0, 4, 3, -2, -1}};


int main()
{
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int kras=1; kras<=tc; kras++)
    {
        int x, l;
        scanf("%d %d", &l, &x);
        string one = "";
        cin >> one;

        string s = "";
        for(int i=0; i<x; i++)
        {
            for(int j=0; j<l; j++)
            {
                s += one[j];
            }
        }

        vector<int> prod(s.size(), 0);
        int current = 1;
        for(int i=0; i<s.size(); i++)
        {
            prod[i] = table[abs(current)][s[i]=='1'?1:s[i]-'i'+2];
            if(current<0)
            {
                prod[i] *= (-1);
            }
            current = prod[i];
        }

        /*for(int i=0; i<prod.size(); i++)
        {
            cout << prod[i] << " ";
        }
        cout << endl;*/
        bool possible = false;
        for(int start=0; start<s.size(); start++)
        {
            for(int finish=start+1; finish<s.size()-1; finish++)
            {
                if(prod[start] == 2 && prod[finish] == 4 && prod[s.size()-1] == -1)
                {
                    possible = true;
                    break;
                }
            }
            if(possible)
            {
                break;
            }
        }

        if(possible)
        {
            printf("Case #%d: YES\n", kras);
        }
        else
        {
            printf("Case #%d: NO\n", kras);
        }

    }
    return 0;
}
