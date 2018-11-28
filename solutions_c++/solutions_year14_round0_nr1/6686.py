#include <iostream>
#include <cstdio>

int main(){
  int T,t=0, m, n;
  scanf("%d", &T);  
  while(t++<T){
    scanf("%d", &m);
    int a[4][4];
    for(int i=0; i<4; i++)
      for(int j=0; j<4; j++)
	scanf("%d", &(a[i][j]));
    scanf("%d", &n);
    int b[4][4];
    for(int i=0; i<4; i++)
      for(int j=0; j<4; j++)
	scanf("%d", &(b[i][j]));
    int c=0, k=0, ans=0;
    while(k<4){
      for(int i=0;i<4;i++){
	if(a[m-1][k]==b[n-1][i]){ans = a[m-1][k]; c++;}
      }
      k++;
    }
    printf("Case #%d: ",t);
    if(c==0) printf("Volunteer cheated!\n");
    else if(c>1) printf("Bad magician!\n");
    else printf("%d\n", ans);
  }
}