#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define PB push_back
#define MP make_pair
#define ll long long

inline int toInt(string s){int v;istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x){ostringstream sout;sout<<x;return sout.str();}

bool isVowel(char c){
    if(c == 'a' || c == 'i' || c == 'u' || c == 'e' || c == 'o'){
        return true;
    }else{
        return false;
    }
}

int main(){
    int cases;

    cin >> cases;
    for(int x=1;x<=cases;x++){
        string str;
        int n;
        cin >> str >> n;
        int len = str.size();
        ll dp[len+1];
        int cnt = 0;
        ll ret = 0;

        if(n == 0){
            ret = (1 + len) * len / 2;  
        }else{
            dp[0] = 0;
            for(int i=1;i<=len;i++){
                if(isVowel(str[i-1])){
                    cnt = 0;
                    dp[i] = dp[i-1];
                }else{
                    cnt++;
                    if(cnt >= n){
                        dp[i] = i - n + 1;
                    }else{
                        dp[i] = dp[i-1];
                    }
                }
                ret += dp[i];
            }
        }
        cout << "Case #" << x << ": " << ret << endl;
    }
}
