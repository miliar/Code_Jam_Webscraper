#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

int main(){
  const int T = getInt();

  REP(cc, T){
    const int n = getInt();
    const int c = getInt();

    multiset<int> s;

    REP(i,n) s.insert(getInt());

    int ans = 0;
    while(s.size()){
      const int mx = *s.rbegin();
      ans++;

      {
	multiset<int>::iterator it = s.end();
	--it;
	s.erase(it);
      }

      const int mn = c - mx + 1;

      multiset<int>::iterator it = s.lower_bound(mn);
      if(it == s.begin()){
      }else{
	--it;
	if(mx + *it > c) throw 0;
	s.erase(it);
      }
    }

    printf("Case #%d: %d\n", cc + 1, ans);

  }

  return 0;
}
