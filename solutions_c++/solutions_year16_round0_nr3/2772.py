#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <climits>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i=0;i<n;i++)
#define INF INT_MAX/3
#define LINF LLONG_MAX/3
#define MP make_pair
#define PB push_back
#define ALL(v) (v).begin(),(v).end()

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

int T;
int N,J;

ull b[11][20];          //b[i][j] : i^j

void init(){
    for(int i=2;i<11;i++){
        b[i][0] = 1;    //i^0 = 1
        for(int j=1;j<20;j++){
            b[i][j] = b[i][j-1] * i;
        }
    }
}

string gen(ull n){
    string ss = "";
    for(int i=0;i<N;i++){
        if(n%2==1) ss = "1" + ss;
        else ss = "0" + ss;
        n /= 2;
    }
    return "1"+ss+"1";
}


bool ok(string s){
    //16桁の01文字列が与えられる
    reverse(s.begin(),s.end());     //文字列は逆順になっているので反転するとnビット目がs[n]となる
    bool f = true;
    vector<int> ans(11);
    for(int i=2;i<=10;i++){
        ull t = 0;
        for(int j=0;j<s.size();j++){
            t += (s[j]-'0') * b[i][j];
        }
        bool f = false;
        for(ull j=2;j<=10000;j++){
            if(t%j==0){
                ans[i] = j;
                f = true;
                break;
            }
        }
        if(!f) return false;
    }
    reverse(s.begin(),s.end());     //文字列は逆順になっているので反転するとnビット目がs[n]となる

    cout << s << " ";
    for(int i=2;i<10;i++) cout << ans[i] << " ";
    cout << ans[10] << endl;
}

int main(){
    init();
    cin >> T;
    cin >> N >> J;
    N = 16;
    N -= 2;
    int cnt=0;
    ll U = 1L << N;

    cout << "Case #1:" << endl;

    for(ull i=0;i<U;i++){
        string s = gen(i);
        if(ok(s)) cnt++;
        if(cnt==J) break;
    }
}
