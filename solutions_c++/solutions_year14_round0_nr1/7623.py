#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <cmath>
#include <ctime>
using namespace std;
 
#define FORZ(i,n) for(typeof(n)i=0;i<n;i++)
#define all(x) (x).begin(),(x).end()
#define PB push_back
#define sz size()
#define FF first
#define SS second
typedef vector<int> VI;
typedef pair<int,int> pII;
typedef vector<string> VS;
typedef long long LL;

int main() {
  int T;
  cin >> T;
  
  for(int t = 1; t <= T; t ++) {
    int ans1;
    cin >> ans1;
    
    int g1[4][4];
    FORZ(i, 4)
      FORZ(j, 4)
        cin >> g1[i][j];
    
    int ans2;
    cin >> ans2;
    
    int g2[4][4];
    FORZ(i, 4)
      FORZ(j, 4)
        cin >> g2[i][j];
        
    VI poss1(4);
    FORZ(j, 4)
      poss1[j] = g1[ans1 - 1][j];
    
    VI poss2(4);
    FORZ(j, 4)
      poss2[j] = g2[ans2 - 1][j];
      
    map<int, int> mp;
    
    FORZ(i, 4) {
      mp[poss1[i]] ++;
      mp[poss2[i]] ++;
    }
    
    int cnt = 0, ret = -1;
    
    for(map<int, int>::iterator it = mp.begin(); it != mp.end(); it ++) {
      if(it->second > 1) {
        cnt ++;
        ret = it->first;
      }
    }
    
    cout << "Case #" << t << ": ";
    if(cnt == 0)
      cout << "Volunteer cheated!" << endl;
    else if(cnt > 1)
      cout << "Bad magician!" << endl;
    else
      cout << ret << endl;
  }
  
  return 0;
}