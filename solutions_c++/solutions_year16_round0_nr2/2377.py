#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <climits>
using namespace std;

typedef long long ll;
int testCase;
string str;
int s, e;
bool isPlus(int direct)
{
    if(direct == 1)
    {
        if(str[s] == '+') return true;
        else return false;
    }
    else
    {
        if(str[e] == '-') return true;
        else return false;
    }
}

void movePos(int direct)
{
    if(direct == 1) s++;
    else e--;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("codeGem#B.out", "w+", stdout);
    scanf("%d", &testCase);
    for(int tc = 1; tc <= testCase; tc++)
    {
        cin >> str;
        s = 0;
        e = str.size()-1;
        while(str[e] == '+') e--;
        
        int pos = s, direct = 1, res = 0;
        while(s <= e)
        {
            if(isPlus(direct))
            {
                while(isPlus(direct))
                    movePos(direct);
                res++;
            }
            if(!isPlus(direct))
            {
                while(!isPlus(direct))
                    movePos(direct);
                res++;
            }
        }
        printf("Case #%d: %lld\n", tc, res);
    }
}