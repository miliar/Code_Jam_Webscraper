#include <stdio.h>
#include <vector>

int main() {

  int T;
  scanf("%d", &T);
  int I = 0;
  while (T-- > 0) {
    int N = 0, M = 0;
    scanf("%d %d", &N, &M);

    std::vector<int> maxx;
    maxx.resize(M);
    for (int i = 0 ; i < M; ++i)
      maxx[i] = -1;

    std::vector<int> maxy;
    maxy.resize(N);
    for (int i = 0 ; i < N; ++i)
      maxy[i] = -1;


    std::vector< std::vector<int> > vec;
    vec.resize(N);
    for (int i = 0; i < N; i++) {
      vec[i].resize(M);
      for (int j = 0; j < M; j++) {
	int val = 0;
	scanf("%d", &val);
	//printf("wczytuje %d %d = %d\n", i, j, val);
	vec[i][j] = val;
	if (maxx[j] < val) maxx[j] = val;
	if (maxy[i] < val) maxy[i] = val;
      }
    }

    bool ok = true;
   for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
	if (vec[i][j]<maxx[j] && vec[i][j]<maxy[i]) {
	  ok =false;
	  goto l;
	}
      }
    }

  l:
   /*
    for (int i = 0 ; i < N; ++i) {
       printf("maxy[%d] = %d \n", i, maxy[i]);
    }
  

  for (int i = 0 ; i < M; ++i) {
       printf("maxx[%d] = %d \n", i, maxx[i]);
    }
   */

    printf("Case #%d: ", I+1);

   if (!ok) printf ("NO\n"); else printf("YES\n");


    I++;
  }

}
