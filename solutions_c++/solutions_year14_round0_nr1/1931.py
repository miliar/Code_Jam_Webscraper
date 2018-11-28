#include<cstdio>
#include<cstdlib>
#include<cstring>
#define LEN 20
#define ROW 5

int T;
int inrow;
int num[ROW][ROW];
int row1[LEN];
int row2[LEN];
int ans[LEN];

int main(void)
{
  int tc=1;
  scanf("%d",&T);
  while(T--){
    memset(row1,0,sizeof(row1));
    memset(row2,0,sizeof(row2));
    scanf("%d",&inrow);
    for(int i=1;i<=4;++i){
      for(int j=1;j<=4;++j){
        scanf("%d",&num[i][j]);
      }
    }
    for(int j=1;j<=4;++j){
      row1[num[inrow][j]]=1;
    }
    scanf("%d",&inrow);
    for(int i=1;i<=4;++i){
      for(int j=1;j<=4;++j){
        scanf("%d",&num[i][j]);
      }
    }
    for(int j=1;j<=4;++j){
      row2[num[inrow][j]]=1;
    }
    int ansnum=0,anscount=0;
    for(int i=1;i<=16;++i){
      ans[i]=row1[i]&row2[i];
      if(ans[i]){
        ansnum=i;
        ++anscount;
      }
    }
    if(1==anscount){
      printf("Case #%d: %d\n",tc,ansnum);
    }else if(0==anscount){
      printf("Case #%d: Volunteer cheated!\n",tc);
    }else if(anscount>1){
      printf("Case #%d: Bad magician!\n",tc);
    }
    tc++;
  }
  return 0;
}

