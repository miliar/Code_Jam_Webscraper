#include<cstdio>

using namespace std;

bool check(int a, int possible[]){
  for(int i=0;i<4;i++){
    //printf("%d %d\n",possible[i],a);
    if(possible[i]==a)
      return true;
  }
  return false;
}

int main(){
  int cards[4][4];
  int possible[4];
  int tc, row, ans, tot,caseNo=1;
  scanf("%d\n",&tc);
  while(tc--){
    scanf("%d",&row);
    row=row-1;
    for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
	scanf("%d",&cards[i][j]);
    for(int i=0;i<4;i++)
      possible[i]=cards[row][i];
    scanf("%d",&row);
    row=row-1;
    for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
	scanf("%d",&cards[i][j]);
    tot=0;
    for(int i=0;i<4;i++){
      if(check(cards[row][i],possible)){
	tot++;
	ans=cards[row][i];
      }
    }
    if(tot==1)
      printf("Case #%d: %d\n",caseNo,ans);
    else if(tot>1)
      printf("Case #%d: Bad magician!\n",caseNo);
    else
      printf("Case #%d: Volunteer cheated!\n",caseNo);
    caseNo++;
  }
}
