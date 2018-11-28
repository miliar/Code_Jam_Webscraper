#include<stdio.h>
#include<string.h>
int occur1[17];
int occur2[17];
char *bad = "Bad magician!";
char *cheat = "Volunteer cheated!";
int main()
{
  freopen("A-small-attempt0.in","r",stdin);
  freopen("A-small-attempt0.out","w",stdout);
  int T,row1,row2,count,idx;
  int mtx1[5][5],mtx2[5][5];
  scanf("%d",&T);
  for(int t=1;t<=T;t++) {
    count = 0;
    memset(occur1,0,sizeof(occur1));
    memset(occur2,0,sizeof(occur2));
    scanf("%d",&row1);
    for(int i=1;i<=4;i++)
      for(int j=1;j<=4;j++) 
        scanf("%d",&mtx1[i][j]);
    scanf("%d",&row2);
    for(int i=1;i<=4;i++)
      for(int j=1;j<=4;j++) 
        scanf("%d",&mtx2[i][j]);
    for(int i=1;i<=4;i++)
      occur1[mtx1[row1][i]]++;
    for(int i=1;i<=4;i++)
      occur2[mtx2[row2][i]]++;
    for(int i=1;i<=16;i++) {
      if(occur1[i] == 1 && occur2[i] == 1)
        {count++;idx = i;}
    }
    if(count==0) {
      printf("Case #%d: %s\n",t,cheat);
    } else if(count==1) {
      printf("Case #%d: %d\n",t,idx);
    } else {
      printf("Case #%d: %s\n",t,bad);
    }
  }
  return 0;
}