#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
using namespace std;

const int N = 1010;
char str[N];

vector<char>g;

int main(void)
{
    int T;
    freopen("A-large.in", "r", stdin);
    freopen("ou.txt", "w", stdout);
    cin >> T;
    int cnt = 1;
    while(T--)
    {
        cin >> str;
        g.clear();
        cout << "Case #" << cnt++ << ": "  ;
        int len = strlen(str);
        int c = 0;
        for(int i = 0; i < len; i++)
        {
            if(str[i] < c)
            {
                g.push_back( str[i] );
            }
            else
            {
                g.insert( g.begin(), str[i] );
                c = str[i];
            }
        }
        for(int i = 0; i < g.size(); i++)
            cout << g[i] ;
        cout << endl;
    }
    return 0;
}
