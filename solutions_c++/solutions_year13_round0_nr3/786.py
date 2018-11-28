#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <bitset>
#include <numeric>
#include <utility>
#include <iomanip>
#include <algorithm>
#include <functional>
using namespace std;

typedef long long ll;
typedef vector<int> vint;
typedef vector<ll> vll;
typedef pair<int,int> pint;

#define DE 1
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
#define ALL(s) (s).begin(),(s).end()
#define REP(i,n) for (int i = 0; i < (int)(n); ++i)
#define EACH(i,s) for (typeof((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define COUT(x) cout<<#x<<" = "<<(x)<<" (L"<<__LINE__<<")"<<endl

template<class T1, class T2> ostream& operator<<(ostream &s, pair<T1,T2> P){return s<<'<'<<P.first<<", "<<P.second<<'>';}
template<class T> ostream& operator<<(ostream &s, vector<T> P) {s<<"{ ";for(int i=0;i<P.size();++i){if(i>0)s<<", ";s<<P[i];}return s<<" }"<<endl;}
template<class T1, class T2> ostream& operator<<(ostream &s, map<T1,T2> P) {s<<"{ ";for(typeof(P.begin()) it=P.begin();it!=P.end();++it){if(it!=P.begin())s<<", ";s<<'<'<<it->first<<"->"<<it->second<<'>';}return s<<" }"<<endl;}



ll A, B;
vector<string> strpal;
vll res;

void dfs(string str, int num, int now, int keta) {
    if (now == (keta-1)/2) {
        if (keta & 1) {
            string str2 = str;
            str += (char)(num+'0');
            reverse(ALL(str2));
            str += str2;
        }
        else {
            str += (char)(num+'0');
            string str2 = str;
            reverse(ALL(str2));
            str += str2;
        }
        strpal.PB(str);
        return;
    }
    
    str += (char)(num+'0');
    for (int i = 0; i < 10; ++i) {
        dfs(str, i, now+1, keta);
    }
}

bool ispal(ll num) {
    stringstream ss;
    ss << num;
    string str1 = ss.str();
    string str2 = str1;
    reverse(ALL(str2));
    if (str1 == str2) return true;
    else return false;
}


int main() {
    freopen( "/Users/macuser/Documents/Programming/Contest/C-large-1.in", "r", stdin );
    freopen( "/Users/macuser/Documents/Programming/Contest/CL1.txt", "w", stdout );
    
    for (int keta = 1; keta <= 7; ++keta) {
        for (int i = 1; i < 10; ++i) {
            dfs("", i, 0, keta);
        }
    }
    //COUT(strpal);
    //COUT(strpal.size());
    ll num;
    for (int i = 0; i < strpal.size(); ++i) {
        istringstream sin(strpal[i]);
        sin >> num;
        num = num*num;
        if (ispal(num)) res.PB(num);
    }
    
    //COUT(res);
    
    int T;
    scanf("%d", &T);
    for (int id = 1; id <= T; ++id) {
        cin >> A >> B;
        int con = 0;
        for (int i = 0; i < res.size(); ++i) {
            if (A <= res[i] && res[i] <= B) ++con;
        }
        
        printf("Case #%d: ", id);
        printf("%d", con);
        printf("\n");
    }
    
    return 0;
}




