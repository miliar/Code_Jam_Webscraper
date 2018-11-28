#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>

#define small 
//#define large

typedef std::vector<bool> vb;
typedef std::vector<int> vi;
typedef long long ll;

int main()
{
#if defined(small)
  freopen("D-small-attempt1.in", "r", stdin);
#elif defined(large)
  freopen("D-large.in", "r", stdin);
#endif
  freopen("out.out", "w", stdout);

  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d:", t);
    fprintf(stderr, "Case #%d:", t);
    
    int K, C, S;
    scanf("%d %d %d", &K, &C, &S);

    //    unsigned long long int KpowC = pow(K, C);
    for (unsigned long long int i = 1; i <= S; i++) {
      printf(" %d", i);
      fprintf(stderr, " %d", i);  
    }
    printf("\n");
    fprintf(stderr, " \n");
  }
  return 0;
}
