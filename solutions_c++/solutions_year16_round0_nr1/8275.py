#include<cstring>
#include<cstdio>
#include<iostream>
using namespace std;

bool flag[10];

int check(int x)
{
    while(x)
    {
        flag[ x%10 ] = 1;
        x /= 10;
    }
    for(int i = 0; i < 10; i++)
        if(!flag[i]) return 0;
    return 1;
}

int main(void)
{
    int T;
    freopen("A-large.in", "r", stdin);
    freopen("ou.txt", "w", stdout);
    cin >> T;
    int cnt = 1;
    while(T--)
    {
        int n;
        memset(flag, 0, sizeof(flag));
        cin >> n;
        if(!n)  {cout << "Case #" << cnt++ << ": INSOMNIA" << endl;continue;}
        int i;
        for(i = 1; ; i++)
        {
            if(check(i*n)) break;
        }
         cout << "Case #" << cnt++ << ": " << i*n << endl;
    }
    return 0;
}
