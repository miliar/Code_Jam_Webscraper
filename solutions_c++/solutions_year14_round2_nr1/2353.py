#include <cmath>
#include <queue>
#include <vector>
#include <queue>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <fstream>
#include <iomanip>   
#include <iostream>  
#include <sstream>  // istringstream buffer(myString);
#include <stack>
#include <set>
#include <algorithm>
#include <cstring>
#include <limits>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int cnt[110][110];

int main() {
  freopen("A-small-attempt2.in","r",stdin);
  //freopen("in","r",stdin);
  freopen("A-small.out","w",stdout);

  int TC, CASE=1;
  scanf("%d", &TC);
  while(TC--) {
    int N;
    scanf("%d\n", &N);
    vector<string> s(N);
    string last;
    bool found = false;
    memset(cnt, 0, sizeof(cnt));
    for(int i=0;i<N;i++) {
      cin >> s[i];

      string cur = "";
      cur += s[i][0];
      int k=0;
      cnt[0][i] = 1;
    
      for(size_t j=1;j<s[i].size();j++) {
        //cout << cur << k << endl;
        //cout << s[i][j] << ":" << cur[cur.size()-1] << endl;
        if(s[i][j] != cur[cur.size()-1]) {
          cur += s[i][j];
          k++;
          cnt[k][i] = 1;
        } else {
          cnt[k][i] = cnt[k][i] + 1;
        }
      }
      if (!last.empty() && cur != last) { found = true;}
      last = cur;
    }

    if(!found) {
      int edits = 0;
      for(int i=0;i<=100;i++) {
        int best = 110;
        for(int k=0;k<=100;k++) {
          int r = 0;
          for(int j=0;j<N;j++) {
            r += abs(cnt[i][j] - k);            
          }
          if (r<best) { best = r;}
        }
        edits += best;
      }
      
      printf("Case #%d: %d\n", CASE++, edits);        
    } else {
      printf("Case #%d: Fegla Won\n", CASE++);
    }
  }
}
