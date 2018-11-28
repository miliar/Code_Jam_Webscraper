#include <stdio.h>
#include <stdlib.h>
#include <bits/stdc++.h>

/// Type definitions
#define rep(a,b) for(int i=a;i<=b;i++)
#define rev(a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
#define in(n) scanf("%d",&n)

///STL
#define vi vector<int>
#define vvi vector< vector<int> >
#define pb push_back
#define mp make_pair
#define mii map<int,int>
#define pii pair<int,int>
#define f first
#define s second

/// Iterator
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)

/// Constants
#define ll long long
#define mod 1000000007
#define EPS 1e-7
#define sqr(x) ((x)*(x))
#define sqrt(x) sqrt(1.0*(x))
#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 9223372036854775807LL
#define INF 1000000000

/// Files.
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

using namespace std;

int main()
{
    ifstream inpfile;
    ofstream outfile;

    inpfile.open("A-large.in");
    outfile.open("A-large.txt");

    int t, counter = 1;
    inpfile >> t;
    while (t > 0)
    {
        string s, ans = "";
        inpfile >> s;
        int arr[2000] = {0}, n = s.length();

        for (int i = 0; i < n; i++)
            arr[s[i]]++;

        if (arr['Z'] > 0)
        {
            int cnt = arr['Z'];
            arr['Z'] -= cnt;
            arr['E'] -= cnt;
            arr['R'] -= cnt;
            arr['O'] -= cnt;
            for (int i = 0; i < cnt; i++)
                ans.push_back('0');
        }

        if (arr['W'] > 0)
        {
            int cnt = arr['W'];
            arr['T'] -= cnt;
            arr['W'] -= cnt;
            arr['O'] -= cnt;
            for (int i = 0; i < cnt; i++)
                ans.push_back('2');
        }

        if (arr['U'] > 0)
        {
            int cnt = arr['U'];
            arr['F'] -= cnt;
            arr['O'] -= cnt;
            arr['U'] -= cnt;
            arr['R'] -= cnt;
            for (int i = 0; i < cnt; i++)
                ans.push_back('4');
        }

        if (arr['X'] > 0)
        {
            int cnt = arr['X'];
            arr['S'] -= cnt;
            arr['I'] -= cnt;
            arr['X'] -= cnt;
            for (int i = 0; i < cnt; i++)
                ans.push_back('6');
        }

        if (arr['G'] > 0)
        {
            int cnt = arr['G'];
            arr['E'] -= cnt;
            arr['I'] -= cnt;
            arr['G'] -= cnt;
            arr['H'] -= cnt;
            arr['T'] -= cnt;
            for (int i = 0; i < cnt; i++)
                ans.push_back('8');
        }

        if (arr['O'] > 0)
        {
            int cnt = arr['O'];
            arr['O'] -= cnt;
            arr['N'] -= cnt;
            arr['E'] -= cnt;
            for (int i = 0; i < cnt; i++)
                ans.push_back('1');
        }

        if (arr['T'] > 0)
        {
            int cnt = arr['T'];
            arr['T'] -= cnt;
            arr['H'] -= cnt;
            arr['R'] -= cnt;
            arr['E'] -= cnt;
            arr['E'] -= cnt;
            for (int i = 0; i < cnt; i++)
                ans.push_back('3');
        }

        if (arr['F'] > 0)
        {
            int cnt = arr['F'];
            arr['F'] -= cnt;
            arr['I'] -= cnt;
            arr['V'] -= cnt;
            arr['E'] -= cnt;
            for (int i = 0; i < cnt; i++)
                ans.push_back('5');
        }

        if (arr['S'] > 0)
        {
            int cnt = arr['S'];
            arr['S'] -= cnt;
            arr['E'] -= cnt;
            arr['V'] -= cnt;
            arr['E'] -= cnt;
            arr['N'] -= cnt;
            for (int i = 0; i < cnt; i++)
                ans.push_back('7');
        }

        if (arr['E'] > 0)
        {
            int cnt = arr['E'];
            arr['N'] -= cnt;
            arr['I'] -= cnt;
            arr['N'] -= cnt;
            arr['E'] -= cnt;
            for (int i = 0; i < cnt; i++)
                ans.push_back('9');
        }

        sort(ans.begin(), ans.end());

        outfile << "Case #" << counter << ": " << ans << endl;
        counter++;
        t--;
    }

    inpfile.close();
    outfile.close();

    return 0;
}










