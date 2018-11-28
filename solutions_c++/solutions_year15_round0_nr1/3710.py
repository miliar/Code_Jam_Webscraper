#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <set>
#include <memory.h>
#include <string.h>
#include <sstream>
#include <queue>
#include <bitset>

using namespace std;

//Loops
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define MEM(a,b) memset((a),(b),sizeof(a))

//Constants
#define inf 1000000000
#define pi 2*acos(0.0)
#define eps 1e-9
#define N 1010

//Functions
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define sz(x) int((x).size())

//Pairs
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

//Input-Output
#define FREOPEN(a,b) freopen(a,"r",stdin); freopen(b,"w",stdout);

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;

const int mod = int(1e9) + 7;

int Solve(){
    int Smax, ans = 0, cur = 0;
    string s;
    cin >> Smax >> s;
    for(int i = 0; i <= Smax; i++)
        if(s[i] > '0'){
            if(cur >= i){
                cur += s[i] - '0';
            }
            else{
                ans += i - cur;
                cur = i + s[i] - '0';
            }
        }
    return ans;
}
int main()
{
    FREOPEN("input.txt", "output.txt");
    int test;
    scanf("%d",&test);
    for(int t = 0; t < test; t++){
        int ans = Solve();
        printf("Case #%d: %d\n",t + 1, ans);
    }
    return 0;
}
