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

int t  , cc = 1 ;
bool taken[10];
void solve()
{
    ll n , temp , result;
    cin >> n;
    cout << "Case #" << cc++ << ": ";
    if (n == 0)
    {
        cout << "INSOMNIA" << endl;
        return;
    }
    int cunt = 0, i = 1;
    while (cunt < 10)
    {
        result = temp = n * i;
        while (temp > 0)
        {
            if (!taken[temp % 10])
                cunt++, taken[temp % 10] = 1;
            temp /= 10;
        }
        i++;
    }
    cout << result << endl;
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    while(t--)
    {
        memset(taken, 0, sizeof taken);
        solve() ;
    }
}
