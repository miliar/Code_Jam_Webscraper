#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <bits/stdc++.h>
#define rep(s , n) for(int i = s ; i < n ; i++)
#define all(x) x.begin() , x.end()
#define CLR( x ) memset(x , 0 , sizeof x)
#define pb push_back
#define ii pair
#define mp make_pair
#define f first
#define s second
#define ii pair<int , int>
#define vi vector< int >
#define vl vector < long long >
#define vs vector < string >
#define vb vector < bool >
#define oo 10e12
typedef long long ll ;
typedef unsigned long long ull ;
using namespace std;
int cc = 1, tc ;
void solve()
{
    string s;
    cin >> s;
    int i = 0, cnt = 0;
    while (i < (int) s.length() - 1)
    {
        if (s[i] != s[i + 1])
            cnt++;
        i++;
    }
    if (s[s.length() - 1] == '-')
        cnt++;
    cout << "Case #" << cc++ << ": " << cnt << endl;
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> tc;
    while (tc--)
    {
        solve() ;
    }
    return 0 ;
}
