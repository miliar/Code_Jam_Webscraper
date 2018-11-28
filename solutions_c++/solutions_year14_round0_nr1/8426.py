#include<stdio.h>

struct i4{
  int ps[4];
};

i4 getposcard(){
  i4 ps;
  int nr;
  int cv;
  scanf("%d",&nr);nr--;
  for(int r=0;r<4;r++){
    for(int i=0;i<4;i++){
      scanf("%d",&cv);
      if(r==nr)
        ps.ps[i]=cv;
    }
  }
  return ps;
}

int main(int agrc,char*argv[]){
  int T;scanf("%d",&T);
  for(int tc=1;tc<=T;tc++){
    i4 first=getposcard();
    i4 second=getposcard();
    int match=0;
    int mval;
    for(int i=0;i<16;i++)
      if(first.ps[i&3]==second.ps[i>>2]){
        match++;
        mval=first.ps[i&3];
      }
    printf("Case #%d: ",tc);
    switch(match){
      case 0:  printf("Volunteer cheated!");   break;
      case 1:  printf("%d",mval);              break;
      default: printf("Bad magician!");        break;
    }
    printf("\n");
  }
  return 0;
}
