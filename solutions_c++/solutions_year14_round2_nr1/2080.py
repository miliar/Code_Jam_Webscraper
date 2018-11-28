#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

int N;
char strings[102][102];
int nos[102];
int inds[102];

void work(int indexa) {
  printf("Case #%d: ", indexa);
  scanf("%d", &N);
  int i;
  for(i = 0; i < N; i++) {
    scanf("%s", strings[i]);
  }
  char t;
  int ind;
  int len = strlen(strings[0]);
  int no;
  int templen;
  int flag = 0;
  int sum;
  int avg;
  int cost = 0;
  for(i = 0; i < N; i++) {
    inds[i] = nos[i] = 0;
  }
  for(ind = 0; ind < len;) {
    t = strings[0][ind];
    sum = 0;
    i = 0;
    no = 1;
    while(++ind < len && strings[0][ind] == t) {
      no++;
    }
    nos[0] = no;
    sum += no;
    for(i = 1; i < N; i++) {
      templen = strlen(strings[i]);
      if(inds[i] >= templen || strings[i][inds[i]] != t) {
	flag = 1;
	//printf("i=%d, string=%s, t=%c, inds[i]=%d\n", i, strings[i], t, inds[i]);
	break;
      }
      no = 1;
      while((++inds[i]) < templen && strings[i][inds[i]] == t) {
	no++;
      }
      nos[i] = no;
      sum += no;
    }
    if(flag == 1) break;
    avg = (int) round(((double)sum / N));
    for(i = 0; i < N; i++) {
      cost += abs(nos[i] - avg);
    }
  }
  for(i = 1; i < N; i++) {
    templen = (int)strlen(strings[i]);
    if(inds[i] < templen) {
      //printf("i=%d\n", i);
      flag = 1;
      break;
    }
  }
  if(flag == 1) {
    printf("Fegla won\n");
  }
  else {
    printf("%d\n", cost);
  }
}
      
  

int main() {
  int T;
  scanf("%d", &T);
  int cnt;
  for(cnt = 1; cnt <= T; cnt++) {
    work(cnt);
  }
  return 0;
}
