#include <cstdio>
#include <cstdlib>

using namespace std;

int cmp(const void* f1, const void* f2)
{
  double d1 = *(double*)f1, d2 = *(double*)f2;
  return d1<d2?-1:1;
}

int main()
{
  int T;

  scanf("%d", &T);

  for(int i=0; i<T; i++) {
    int n;
    double naomi[1000], ken[1000];

    scanf("%d", &n);    
    for(int j=0; j<n; j++)
      scanf("%lf", &naomi[j]);
    for(int j=0; j<n; j++)
      scanf("%lf", &ken[j]);

    qsort(naomi, n, sizeof(double), &cmp);
    qsort(ken, n, sizeof(double), &cmp);

    int pts_d = 0;
    int kjp = n-1, njp = n-1, kjm = 0, njm = 0;
    for(int j=0; j<n; j++)
      if(naomi[njm]>ken[kjm]) {
	njm++;
	kjm++;
	pts_d++;
      }
      else {
	kjp--;
	njm++;
      }
	
    int pts_w = 0;
    kjp = n-1, njp = n-1, kjm = 0, njm = 0;
    for(int j=0; j<n; j++)
      if(naomi[njp]>ken[kjp]) {
	njp--;
	kjm++;
	pts_w++;
      }
      else {
	njp--;
	kjp--;
      }

    printf("Case #%d: %d %d\n", i+1, pts_d, pts_w);
  }  
  return 0;
}
