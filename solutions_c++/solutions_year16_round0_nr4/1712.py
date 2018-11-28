#include<stdio.h>
#include<vector>

using namespace std;

int main(){
  int T;
  scanf("%d", &T);
  int K, C, S;
  vector <int> queries;
  for (int t = 0; t < T; t++){
    scanf("%d %d %d", &K, &C, &S);
    printf("Case #%d:", t+1);
    queries.clear();
    if (K < 3 && C > 1){
      queries.push_back(K);
      //printf("Case #%d: %d\n", t+1, K);
      //continue;
    }
    else {
      if (C == 1){
	for (int i = 0; i < K; i++){
	  queries.push_back(i+1);
	  /*if (i == 0) printf("Case #%d: %d", t+1, i+1);
	  else printf(" %d", i+1);*/
	}
      }
      else{
	for (int i = 1; i <=K; i++){
	  if ((i-1) * K + i + 1 <= K * K) queries.push_back((i-1) * K + i + 1);
	  //printf("%d ", (i-1) * K + i + 1);
	}
      }
    }
    if (queries.size() <=S){
      for (int i = 0; i < queries.size(); i++) printf(" %d", queries[i]);
    }
    else printf(" IMPOSSIBLE");
    printf("\n");
  }
  return 0;
}