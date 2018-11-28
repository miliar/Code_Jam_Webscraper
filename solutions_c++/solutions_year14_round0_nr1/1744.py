#include <cstdio>


int main () {
  int tt=0;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++) {
    int tem[55]={0};
    int r1,r2;
    scanf("%d",&r1);
    for(int i=1;i<=4;i++)
      for(int j=1;j<=4;j++) {
	int a;
	scanf("%d",&a);
	if(i==r1)tem[a]++;
      }

    scanf("%d",&r2);
    for(int i=1;i<=4;i++)
      for(int j=1;j<=4;j++) {
	int a;
	scanf("%d",&a);
	if(i==r2)tem[a]++;
      }
    int ret=-1;
    for(int i=1;i<=16;i++){
      if(tem[i]==2) {
	if (ret!=-1)ret = 99;
	else ret=i;
      }
    }
    printf("Case #%d: ", pp);
    if(ret==99)printf("Bad magician!\n");
    else if(ret==-1)printf("Volunteer cheated!\n");
    else printf("%d\n",ret);
  }
  return 0;
}
