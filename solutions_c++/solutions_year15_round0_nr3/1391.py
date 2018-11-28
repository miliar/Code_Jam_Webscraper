#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

#define all(x) x.begin(), x.end()
#define f(i,a,b) for(int i = (a); i <= (b); i++)
#define fd(i,a,b) for(int i = (a); i >= (b); i--)
#define mp make_pair
#define faster_io() ios_base::sync_with_stdio(false)
#define pb push_back
#define pii pair<int,int>
#define SZ(x) ((int)x.size())
#define vii vector<pair<int,int>>

const int INF = 1000000005;
const ll INFLL = 100000000000000000ll;
const ll MOD = 1000000007;

ifstream fin("C.txt");
ofstream fout("C.out");

int A[10005], L, Left[10005], Right[10005], X, T;
string S;
vector<vector<int>> Mult = {{0,1,2,3,4,5,6,7},
                            {1,4,3,6,5,0,7,2},
                            {2,7,4,1,6,3,0,5},
                            {3,2,5,4,7,6,1,0},
                            {4,5,6,7,0,1,2,3},
                            {5,0,7,2,1,4,3,6},
                            {6,3,0,5,2,7,4,1},
                            {7,6,1,0,3,2,5,4}};

string solve()
{
    Left[0] = 0;
    f(i,1,L) Left[i] = Mult[Left[i-1]][A[i]];
    Right[L+1] = 0;
    fd(i,L,1) Right[i] = Mult[A[i]][Right[i+1]];
    f(l,1,L) if(Left[l] == 1) f(r,1,L) if(Right[r] == 3)
    {
        int v = 0;
        f(i,l+1,r-1) v = Mult[v][A[i]];
        if(v == 2) return "YES";
    }
    return "NO";
}

int main()
{
    fin >> T;

    f(t,1,T)
    {
        string s;
        fin >> L >> X >> s;
        S = "";
        f(x,1,X) S += s;
        L *= X;
        f(i,1,L)
        {
            if(S[i-1] == '1') A[i] = 0;
            if(S[i-1] == 'i') A[i] = 1;
            if(S[i-1] == 'j') A[i] = 2;
            if(S[i-1] == 'k') A[i] = 3;
        }
        fout << "Case #" << t << ": " << solve() << "\n";
        cout << "Ended " << t << "\n";
    }
}
