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

ifstream fin("D.txt");
ofstream fout("D.out");

bool Lose[5][5][5];
int H, W, N, T;

int main()
{
    fin >> T;
    Lose[1][1][2] = Lose[1][1][3] = Lose[1][1][4] = true;
    Lose[1][2][3] = Lose[1][2][4] = true;
    Lose[1][3][2] = Lose[1][3][3] = Lose[1][3][4] = true;
    Lose[1][4][3] = Lose[1][4][4] = true;
    Lose[2][2][3] = Lose[2][2][4] = true;
    Lose[2][3][4] = true;
    Lose[2][4][3] = Lose[2][4][4] = true;
    Lose[3][3][2] = Lose[3][3][4] = true;
    Lose[4][4][3] = true;

    f(t,1,T)
    {
        fin >> N >> H >> W;
        if(H>W) swap(H,W);
        if(Lose[H][W][N]) fout << "Case #" << t << ": RICHARD\n";
        else fout << "Case #" << t << ": GABRIEL\n";
    }
}
