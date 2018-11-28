//Aleksander Łukasiewicz
#include<cstdio>
#include<algorithm>
using namespace std;

const int MAXN = 1000;

int t;
int tab[MAXN + 3];

int main(){
  scanf("%d", &t);
  for(int cs=1; cs<=t; cs++){
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++)
      scanf("%d", &tab[i]);
    int res = 1000;
    for(int time=1; time<=1000; time++){
      int actual = 0;
      for(int i=0; i<n; i++)
	actual += (tab[i]-1)/time;
      actual+=time;
      res = min(res, actual);
    }
    
    printf("Case #%d: %d\n", cs, res);
  }
  
  
  return 0;
}