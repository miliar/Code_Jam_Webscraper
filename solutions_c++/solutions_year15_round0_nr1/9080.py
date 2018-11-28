#pragma comment(linker, "/STACK:640000000")
#include<iostream>
#include<fstream>
#include<cstdio>
#include<cassert>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<string>
#include<sstream>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<vector>
#include<bitset>
#include<algorithm>

#define pb push_back
#define ppb pop_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define ll long long
#define bit __builtin_popcountll
#define sqr(x) (x) * (x)
#define forit(it,S) for(__typeof((S).begin()) it = (S).begin(); it != (S).end(); it++)

using namespace std;

typedef pair<int, int> pii;

const double eps = 1e-9;
const double pi = acos(-1.0);
int TEST = 0;

void solve(int p){
     ifstream cin("A-large.in");
     int t;
     cin >> t;
     ofstream cout("output.txt");
     while(t--){
     int n;
     string s;
     cin >> n >> s;
     int sum = s[0] - '0',ans = 0;
     for(int i = 1; i < s.length(); i++){
             if(s[i] == '0')continue;
             if(i > sum){
                  int t = i - sum; 
                  ans += t;
                  sum += t;
                  sum += s[i] - '0';
             }
             else {
                  sum += s[i] - '0';    
             }
     }
     cout << "Case #" << ++TEST << ": "<< ans << endl;
     }
}
int main() {
    int n;
  
    solve(0);

    return 0;
}
