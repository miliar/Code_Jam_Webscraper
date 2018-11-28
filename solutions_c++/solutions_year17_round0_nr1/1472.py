/*  ^^ ====== ^^
ID: meixiuxiu
PROG: test
LANG: C++11
*/
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cctype>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int ,int> pii;
#define MEM(a,b) memset(a,b,sizeof a)
#define CLR(a) memset(a,0,sizeof a);
#define pi acos(-1.0)
#define maxn 40000
#define maxv 100005
const int inf = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
bool tmp[1005];
int main(){
    freopen("C:\\Users\\meixinyu\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\meixinyu\\Desktop\\out.txt","w",stdout);
    int t;cin >> t;
    int kase = 1;
    while(t--){
        printf("Case #%d: ",kase++);
        string s;cin >> s;
        int k;cin >> k;
       // cout << s << k << endl;
        for(int i=0;i<s.size();i++){
            if(s[i]=='+')tmp[i] = 1;
            else tmp[i] = 0;
           // cout <<tmp[i];
        }
        int pos = 0;
        int cnt = 0;
        int yes = 1;
        while(pos < s.size()){
            if(tmp[pos]){
                pos++;
              //  cout << pos << endl;
                continue;
            }
            if(pos+k-1 < s.size()){
                for(int i=0;i<k;i++){
                    tmp[i+pos] = 1-tmp[i+pos];
                    //cout << i + pos << endl;
                } 
                cnt++;
            }
            else{
                yes = 0;
            }
            pos++;
        }
        if(yes){
            cout << cnt << '\n';
        }
        else cout << "IMPOSSIBLE\n";
    }
}