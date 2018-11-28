#include <cstdio>
#include <set>
using namespace std;

int main(){
  int T; scanf("%d", &T);
  
  for(int t = 1; t <= T; ++t){
    int A, B, K;
    scanf("%d %d %d", &A, &B, &K);
    
    int cnt = 0;
    set<pair<int,int> > st;
    
    for(int i = 0; i < A; ++i)
      for(int j = 0; j < B; ++j)
	if((i & j) < K)
	  if(!st.count(pair<int,int>(i,j))) {
	    cnt++;
	    st.insert(pair<int,int>(i,j));
	  }
    printf("Case #%d: %d\n",t,cnt);
  }
}