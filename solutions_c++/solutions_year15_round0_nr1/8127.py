#ifdef _HOME_
#include <bits/stdc++.h>
#else
#include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include <stack>
#include <cstdio>
#include <cmath>
#endif
 
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;
typedef vector <int> vi;
typedef vector <ll> vll;
typedef pair <int, int> pii;
typedef vector <pii> vii;
typedef vector <double> vd;
 
#define SQR(x) ((x) * (x))
#define CUBE(x) ((x) * (x) * (x))
#define MP(a, b) make_pair((a), (b))
 
#define TASK "quotient"
#define MOD 1e9
#define X first
#define Y second
#define EPS 1e-7
 
void solution();
 
stack <clock_t> times;
 
void start_t()
{
    times.push(clock());
}
 
void stop_t(string out)
{
    clock_t now = clock();
    clock_t past = times.top();
    times.pop();
    double delta = now - past;
    //cout << out << ": " << fixed << delta / (double)CLOCKS_PER_SEC << endl;
}
 
int main()
{
    ios::sync_with_stdio(false);
#ifdef _HOME_
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    start_t();
#else
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif // _HOME_
    int t;
    cin >> t;
    for(int i = 0;i < t;i++)
    {
        cout << "Case #" << i + 1 << ": ";
        solution();
    }
#ifdef _HOME_
    stop_t("Total time");
#endif // _HOME_
    return 0;
}
 
void solution()
{
    int k;
    cin >> k;
    string s;
    cin >> s;
    int res = 0, need = 0;
    for(int i = 0;i <= k;i++)
    {
        if(need < i)
        {
            res+= i - need;
            need = i;
        }
        need+= s[i] - '0';
    }
    cout << res << endl;
}