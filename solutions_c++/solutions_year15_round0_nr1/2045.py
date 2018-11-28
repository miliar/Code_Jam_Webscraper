//Aleksander Łukasiewicz
#include<cstdio>
using namespace std;

const int MAXN = 1000;

int t;
char tab[MAXN + 3];

int main(){
  scanf("%d", &t);
  for(int cs=1; cs<=t; cs++){
    int n;
    scanf("%d", &n);
    scanf("%s", tab);
    int actual = 0, res = 0;
    for(int i=0; i<=n; i++){
      int val = tab[i] - '0';
      if(actual < i){
	res += i-actual;
	actual = i;
      }
      actual += val;
    }
    
    printf("Case #%d: %d\n", cs, res);
  }

return 0;
}