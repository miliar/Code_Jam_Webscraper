#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>

//#define small 
#define large

typedef std::vector<bool> vb;
typedef std::vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;

int main()
{
#if defined(small)
  freopen("A-small-attempt3.in", "r", stdin);
#elif defined(large)
  freopen("A-large.in", "r", stdin);
#endif
  freopen("out.out", "w", stdout);

  
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d:", t);
    fprintf(stderr, "Case #%d:", t);
    
    int N;
    scanf("%d", &N);

    std::vector<int> senators(27);
    for (int i = 0; i < N; i++) {
      std::cin >> senators[i];;
    }

    int total=1, max=0;
    while (total != 0){
      total = 0;
      max=0;
      for (int i = 0; i < N; i++) {
	total += senators[i];
	max = std::max(max, senators[i]);
      }
      if(total == 0)
	break;
      printf(" ");
      fprintf(stderr, " ");
      int senatorsLeaving;
      if (max == 1 && total == 3)
	senatorsLeaving = 1;
      else
	senatorsLeaving = 2;
      for (int i = 0; i < N; i++) {
	if(senators[i] == max){
	  printf("%c", 'A'+i);
	  fprintf(stderr, "%c", 'A'+i);
	  senators[i]--;
	  senatorsLeaving--;
	  if (senatorsLeaving == 0){
	    break;
	  }
	}
      }

    }
    
    printf("\n");
    fprintf(stderr, " \n");
  }
  return 0;
}
