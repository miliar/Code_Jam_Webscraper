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
const ll INFLL = 100000000000000000ll;
const ll MOD = 1000000007;

// ----------------------------------------------------------------------------------------------------------

ifstream fin("A.in");
ofstream fout("A_out.txt");

int T, A[256], B[15];
string S;

int main()
{
    fin >> T;

    f(tt,1,T)
    {
        cout << tt << "\n";
        fin >> S;
        f(i,0,255) A[i] = 0;
        f(i,0,9) B[i] = 0;
        for(char c : S) A[c]++;
        while(A['Z'])
        {
            B[0]++;
            A['Z']--, A['E']--, A['R']--, A['O']--;
        }
        while(A['W'])
        {
            B[2]++;
            A['T']--, A['W']--, A['O']--;
        }
        while(A['U'])
        {
            B[4]++;
            A['F']--, A['O']--, A['U']--, A['R']--;
        }
        while(A['X'])
        {
            B[6]++;
            A['S']--, A['I']--, A['X']--;
        }
        while(A['O'])
        {
            B[1]++;
            A['O']--, A['N']--, A['E']--;
        }
        while(A['F'])
        {
            B[5]++;
            A['F']--, A['I']--, A['V']--, A['E']--;
        }
        while(A['V'])
        {
            B[7]++;
            A['S']--, A['E']--, A['V']--, A['E']--, A['N']--;
        }
        while(A['N'])
        {
            B[9]++;
            A['N']--, A['I']--, A['N']--, A['E']--;
        }
        while(A['I'])
        {
            B[8]++;
            A['E']--, A['I']--, A['G']--, A['H']--, A['T']--;
        }
        while(A['H'])
        {
            B[3]++;
            A['T']--, A['H']--, A['R']--, A['E']--, A['E']--;
        }

        fout << "Case #" << tt << ": ";
        f(dig,0,9) f(am,1,B[dig]) fout << dig;
        fout << "\n";
    }
}
