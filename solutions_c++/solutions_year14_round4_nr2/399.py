#include <map>
#include <algorithm>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>

inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

template<typename T>
int indexOf(const vector<T> &v, T val){
  return find(v.begin(), v.end(), val) - v.begin();
}

int main(){
  const int T = getInt();

  REP(cc, T){
    const int n = getInt();
    vector<int> v(n);

    REP(i,n) v[i] = getInt();
    const int mxIdx = max_element(v.begin(), v.end()) - v.begin();

    int ans = 0;
    REP(t,n){
      int cnt = 0;
      int cnt2 = 0;

      {
	const int start = min(t, mxIdx);
	const int end = max(t, mxIdx);
	for(int i = start; i <= end; i++){
	  if(v[i] < v[t]) cnt++;
	}
      }

      {
	const int start = t < mxIdx ? 0 : t + 1;
	const int end = t < mxIdx ? t - 1 : n - 1;
	for(int i = start; i <= end; i++){
	  if(v[i] > v[t]) cnt2--;
	}
      }

      {
	const int start = t < mxIdx ? t + 1 : 0;
	const int end = t < mxIdx ? n - 1 : t - 1;
	for(int i = start; i <= end; i++){
	  if(v[i] > v[t]) cnt2++;
	}
      }

      ans += min(cnt, cnt + cnt2);
    }

    printf("Case #%d: %d\n", cc + 1, ans);
  }

  return 0;
}
