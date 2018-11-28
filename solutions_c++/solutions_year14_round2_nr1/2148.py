#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

static const int NC=100;

int main()
{
  int T, nc;
  unsigned char order[NC];
  int sig[100][NC];

  scanf("%d\n", &T);

  for(int t=1; t<=T; t++) {
    int n, impos = 0;
    
    scanf("%d\n", &n);
    nc = 0;
    for(int i=0; i<n; i++) {
      unsigned char c;
      int nci = 0;

      unsigned char oldc = 0;

      while((c=fgetc(stdin))!='\n') {
	if(feof(stdin))
	  break;
	if(c!=oldc) {
	  if(i==0)
	    order[nc++] = c;
	  else {
	    if(nci==nc || order[nci]!=c)
	      impos = 1;
	  }
	  sig[i][nci] = 0;
	  nci++;
	}
	sig[i][nci-1]++;
	oldc = c;
      }
      if(nci!=nc)
	impos = 1;
    }

    // for(int i=0; i<n; i++) {
    //   for(int j=0; j<nc; j++)
    // 	printf("%d ", sig[i][j]);
    //   printf("\n");
    // }

      
    if(impos)
      printf("Case #%d: Fegla Won\n", t);
    else {
      int nmin = 0;
      for(int j=0; j<nc; j++) {
	double sum = 0;
	for(int i=0; i<n; i++)
	  sum += sig[i][j];
	int mean = round(sum/n);
	for(int i=0; i<n; i++)
	  nmin += abs(mean-sig[i][j]);
      }
      printf("Case #%d: %d\n", t, nmin);
    }
  }
      

  return 0;
}
