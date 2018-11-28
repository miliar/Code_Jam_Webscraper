#include <stdio.h>

#include <vector>
#include <algorithm>

using namespace std;

bool less (float i,float j) { return (i<j); }

bool gtr (float i,float j) { return (i>j); }

main() {

    int T;
  scanf("%d",&T);
  
  for (int t = 1; t <= T; t++) {

    int N;
    scanf("%d",&N);

    
    vector<float> a,b;
    float w;

    for (int i = 0; i < N; i++) {
      scanf("%f",&w);
      a.push_back(w);
    }
    for (int i = 0; i < N; i++) {
      scanf("%f",&w);
      b.push_back(w);
    }
    
    sort(a.begin(),a.end(),less);
    sort(b.begin(),b.end(),less);

    int wp = 0;
    int k = 0;
    for (int i = 0; i < N; i++) {
      while ((i+k < N) && (a[i] > b[i+k])) { 
	k++;
      }
    }
    wp = k;
    
    int dwp = 0;
    int s = 0;
    int l = 0;
    int r = 0;
    int m = 0;
    for (int i = 0; i < N; i++) {

      if (a[s] > b[r]) {
	dwp++;
	//	printf("play %f %f\n",a[s],b[r]);
	
	s++;
	r++;
      }
      else {
	  
	//	  printf("play %f %f\n",a[s],b[N-m-1]);
	  s++;
	  m++;
	}
      
    }
    
    printf("Case #%d: %d %d\n",t,dwp,wp);
    
  }
  


}
