#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  int T; scanf("%d", &T);
  
  for(int t = 1; t <= T; ++t){
    int N; scanf("%d",&N);
    vector<double> as(N,0),bs(N,0);
    
    for(int i = 0; i< N; ++i)
      scanf("%lf",&as[i]);
    for(int i = 0; i< N; ++i)
      scanf("%lf",&bs[i]);
    
    sort(as.begin(), as.end());
    sort(bs.begin(), bs.end());
    
    int cnt1 = 0, cnt2 = 0;
/*    
    for(int i = 0; i< N; ++i)
      cnt1 += (as[i] > bs[i]);
    */
    
    vector<bool> bu(N,false);
    
    for(int i = 0; i< N; ++i){
      for(int j = 0; j < N; ++j)
	if(bs[j] > as[i] && !bu[j]){
	  cnt2++;
	  bu[j] = true;
	  break;
	}
    }
    
    vector<bool> au(N,false);
    
    for(int i = 0; i< N; ++i){
      for(int j = 0; j < N; ++j)
	if(as[j] > bs[i] && !au[j]){
	  cnt1++;
	  au[j] = true;
	  break;
	}
    }
    
    printf("Case #%d: %d %d\n",t,cnt1,N - cnt2);
  }
}