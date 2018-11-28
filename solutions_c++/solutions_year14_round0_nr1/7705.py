#include <cstdio>
void read(int & n,int a[4][4]) {
  scanf("%d",&n);
  for(int i=0;i<4;i++){
    for(int j=0;j<4;j++){
      scanf("%d",&a[i][j]);
    }
  }
}
int ck(int n,int a[4][4],int m) {
  for(int i=0;i<4;i++){
    if(a[n-1][i]==m) return 1;
  }
  return 0;
}
int main()
{
  int T,ca=0;
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  scanf("%d",&T);
  while(T--){
    int n1,n2;
    int a[4][4],b[4][4];
    read(n1,a);
    read(n2,b);
    int cnt = 0;
    int ans;
    for(int i = 1; i <= 16; i++){
       if(ck(n1,a,i) && ck(n2,b,i)){
         ans = i;
         cnt++;
       }
    }
    printf("Case #%d: ",++ca);
    if(cnt == 1) {
      printf("%d\n",ans);
    } else if(cnt == 0) {
      puts("Volunteer cheated!");
    } else {
      puts("Bad magician!");
    }
  }
}


