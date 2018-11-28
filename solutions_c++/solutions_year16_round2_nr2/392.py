#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

typedef long long ll;
using namespace std;
using namespace __gnu_pbds;

template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag,tree_order_statistics_node_update>;

#define all(x) x.begin(), x.end()
#define f(i,a,b) for(int i = (a); i <= (b); i++)
#define fd(i,a,b) for(int i = (a); i >= (b); i--)
#define mp make_pair
#define faster_io() ios_base::sync_with_stdio(false)
#define pb push_back
#define pii pair<int,int>
#define SZ(x) ((int)x.size())
#define vii vector<pair<int,int>>

const int INF = 1000000002;
const ll INFLL = 1000000000000000005ll;
const ll MOD = 1000000007;

// ----------------------------------------------------------------------------------------------------------

ifstream fin("B.in");
ofstream fout("B_out.txt");

int N, Tests;
ll DP[20][15][15][3], A[20][15][15][3], B[20][15][15][3];
string S, T;

string tostr(ll x)
{
    string ret = "";
    while(x)
    {
        ret += (char) (x%10 + '0');
        x /= 10;
    }
    return ret;
}

int main()
{
    fin >> Tests;

    f(tt,1,Tests)
    {
        cout << tt << "\n";
        fin >> S >> T;
        /*S = T = "";
        f(i,0,17)
        {
            int x = rand() % 2;
            if(x) S += '?';
            else S += (char) (rand() % 10 + '0');
        }
        f(i,0,17)
        {
            int x = rand() % 2;
            if(x) T += '?';
            else T += (char) (rand() % 10 + '0');
        }*/
        N = SZ(S);
        f(i,0,18) f(a,0,9) f(b,0,9) f(st,0,2) DP[i][a][b][st] = INFLL;
        f(a,0,9) f(b,0,9) DP[0][a][b][0] = 0;
        f(i,0,SZ(S)-1) f(ds,0,9) f(dt,0,9) f(st,0,2)
        {
            //cout << "Best " << i << " " << ds << " " << dt << " " << st << " = " << A[i][ds][dt][st] << " and " << B[i][ds][dt][st] << "\n";
            //if(tt == 32 && i == 2 && ds == 1 && dt == 0) cout << DP[i][ds][dt][st] << " with " << A[i][ds][dt][st] << "," << B[i][ds][dt][st] << "\n";
            if(DP[i][ds][dt][st] >= INFLL) continue;
            //if(tt == 1) cout << "I can reach " << i << " " << ds << " " << dt << " " << st << " with " << A[i][ds][dt][st] << " and " << B[i][ds][dt][st] << "\n";
            f(ns,0,9) f(nt,0,9)
            {
                bool first = false, second = false;
                if(ns == S[i] - '0' || S[i] == '?') first = true;
                if(nt == T[i] - '0' || T[i] == '?') second = true;
                if(first && second)
                {
                    ll next_a = A[i][ds][dt][st]*10 + ns;
                    ll next_b = B[i][ds][dt][st]*10 + nt;
                    int next_st = st;
                    if(st == 0 && next_a > next_b) next_st = 1;
                    if(st == 0 && next_a < next_b) next_st = 2;
                    if(i == 2 && tt == 59 && ns == 3 && nt == 8 && next_st == 2)
                    {
                        //cout << "Next_a would be " << next_a << " and Next_b would be " << next_b << " and current DP is " << DP[i+1][ns][nt][next_st] << "\n";
                        //getchar();
                    }
                    if(abs(next_a - next_b) < DP[i+1][ns][nt][next_st])
                    {
                        if(i == 2 && tt == 59 && ns == 3 && nt == 8 && next_st == 2) cout << "I choose first\n";
                        DP[i+1][ns][nt][next_st] = abs(next_a - next_b);
                        A[i+1][ns][nt][next_st] = next_a;
                        B[i+1][ns][nt][next_st] = next_b;
                    }
                    if(abs(next_a - next_b) == DP[i+1][ns][nt][next_st] && next_a < A[i+1][ns][nt][next_st])
                    {
                        if(i == 2 && tt == 59 && ns == 3 && nt == 8 && next_st == 2) cout << "I choose second\n";
                        DP[i+1][ns][nt][next_st] = abs(next_a - next_b);
                        A[i+1][ns][nt][next_st] = next_a;
                        B[i+1][ns][nt][next_st] = next_b;
                    }
                }
            }
        }
        //getchar();
        ll best = INFLL, best_a = 0, best_b = 0;
        f(st,0,2) f(a,0,9) f(b,0,9) if(DP[N][a][b][st] < best || (DP[N][a][b][st] == best && A[N][a][b][st] < best_a))
        {
            //cout << "I have best at " << st << " " << a << " " << b << " for " << DP[N][a][b][st] << " with " << A[N][a][b][st] << " and " << B[N][a][b][st] << "\n";
            //getchar();
            best = DP[N][a][b][st];
            best_a = A[N][a][b][st];
            best_b = B[N][a][b][st];
        }
        string sx = tostr(best_a), sy = tostr(best_b);
        while(SZ(sx) < SZ(S)) sx += '0';
        while(SZ(sy) < SZ(T)) sy += '0';
        reverse(all(sx)), reverse(all(sy));
        fout << "Case #" << tt << ": " << sx << " " << sy << "\n";
    }
}
