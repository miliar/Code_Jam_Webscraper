#include<cmath>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<iostream>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<list>
#include<algorithm>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int t=1; t<=T; t++){
    int N;
    vector<int> m;
    cin >> N;
    m.resize(N);
    for(int i=0; i<N; i++) cin >> m[i];
    //for(int i=0; i<N; i++) cout << m[i] << " ";
    //cout << endl;

    int ans1,ans2;
    ans1 = 0;
    for(int i=1; i<N; i++){
      if(m[i] < m[i-1]) ans1 += m[i-1] - m[i];
    }

    ans2 = 0;
    int smax = 0;
    for(int i=1; i<N; i++){
      smax = max(smax, m[i-1]-m[i]);
    }

    for(int i=1; i<N; i++){
      if(m[i-1] < smax) ans2 += m[i-1];
      else ans2 += smax;
    }

    cout << "Case #" << t << ": " << ans1 << " " << ans2 << endl;
  }
}

