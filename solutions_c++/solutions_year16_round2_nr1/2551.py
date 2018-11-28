#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vI;
typedef vector<double> vD;
typedef vector<pair<int, int> > vpI;
typedef vector<string> vS;
typedef pair<int, int> pI;
typedef pair<double, double> pD;
typedef map<int, int> mI;
typedef map<string, int> mSI;
typedef map<int, pair<int, int> > mIP;
typedef map<pair<int, int>, int> mPI;
typedef set<int> sI;
typedef set<pI> sPI;
typedef set<string> sS;
typedef priority_queue<int> Qmax;
typedef priority_queue<int, vector<int>, greater<int> >Qmin;

#define TWO(k)  (1<<(k))
#define LTWO(k) (((LL)(1)<<(k)))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define For(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define Ford(i,a,b) for(int (i)=(a);(i)>=(b);(i)--)
#define F0(n) for(int (i)=0;(i)<(n);(i)++)
#define F1(n) for(int (i)=1;(i)<=(n);(i)++)
#define Zero(i) memset((i),0,sizeof((i)))
#define Fu1(i) memset((i),0xff,sizeof((i)))
#define Bit(s,i) (( (s) &(1<<(i)))>0)
#define NP next_permutation

//const double PI = acos(-1.0);
//const double EPS = 1e-9;
//const int ioo = (~0)-(1<<31);
//const LL loo = (~(LL)0)-((LL)1<<63);
//const int MOD = 1000000007;
//const LL MODL = 1000000007LL;
//const LL LL1 = (LL)1;

string s;
string d[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
const int dd[10] = {0,6,8,4,2,1,3,7,5,9};
const char ss[11] = "ZXGUWOTSFI";
int cnt[26];
int ans[10];
void sol(){
    Zero(cnt);
    Zero(ans);
    int l = s.length();
    F0(l) cnt[s[i]-'A']++;
    ans[0] = cnt['Z'-'A'];
    for(int i = 0; i < 10; i++){
        ans[dd[i]] = cnt[ss[i]-'A'];
        for(int j = 0; j < d[dd[i]].length(); j++){
            cnt[d[dd[i]][j]-'A'] -= ans[dd[i]];
        }
    }
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < ans[i]; j++) cout<<i;
    }
    cout<<endl;
}
int main()
{
     freopen("out.txt","w",stdout);
     freopen("A-large.in","r",stdin);
    //freopen("in.txt","r",stdin);
    int TTT, test = 0;
    cin>>TTT;
    while(TTT--){
        cout<<"Case #"<<++test<<": ";
        cin>>s;
        sol();

    }
    return(0);
}
