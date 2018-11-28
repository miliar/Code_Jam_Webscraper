#include <vector>
#include <map>
#include <set>
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
#include <ctime>
#include <fstream>  
#include <sstream>  

using namespace std;

vector<pair<int,int> > li;
int N , D;
const int maxn = 10010;
int dp[maxn];

void input() {
     int d, l ;
     cin >> N;
     li.clear();
     for(int i = 0 ; i < N ; i ++) {
             cin >> d >> l;
             li.push_back(make_pair(d,l));
     }
     cin >>D;
}

string solve_small() {
    int pos = 0;
    int L;
    memset(dp,0,sizeof(dp));
    dp[0] = li[pos].first*2;
    queue<pair<int,int> > q;
    q.push(make_pair(0, dp[0]));
    while(!q.empty()) {
        pair<int,int> now = q.front();
        q.pop();
        L = now.second;
        pos = now.first;
        if(L>=D) {
           return "YES";
        }
        if(L < dp[pos]) continue;
        for(int i = pos + 1; i < N ;i++) {
            if(L >= li[i].first) {
              int dis = min(li[i].first - li[pos].first, li[i].second) + li[i].first;
              if(dis > dp[i]) {
                 dp[i] = dis;
                 q.push(make_pair(i,dis));
              }
            } else {
              break;       
            }
        }
        
    }
    return "NO";
}

int main() {
    freopen("C:/Users/wangkun/Downloads/A-large-practice.in", "r" , stdin);
    freopen( "D:/result.out",  "w",stdout); 
    int T , cas = 0;
    cin >> T;
    while(T--) {
         cas ++;
         input();
         cout << "Case #"<<cas <<": " << solve_small()<< endl;
    }
    return 0;
}
