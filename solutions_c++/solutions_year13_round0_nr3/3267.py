#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

const int N = 128;

int dat[N][N];

bool isPalind(int x)
{
    ostringstream oss;
    oss << x;
    string str = oss.str();
    for(int i = 0, j = str.size() - 1; i <= j; i++, j--)
        if(str[i] != str[j])
            return false;
    return true;
}

int judge(int x)
{
    int re = 0;
    if(!isPalind(x)) return 0;
    for(int i = 1; i * i <= x; i++)
    {
        if(i * i == x && isPalind(i))
            return 1;
    }
    return re;
}

int main()
{
    freopen("out3.txt", "w", stdout);
    int tcas, cas = 0;
    scanf("%d", &tcas);
    while(tcas --)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        int ans = 0;
        for(int i = a; i <= b; i++)
        {
            ans += judge(i);
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
