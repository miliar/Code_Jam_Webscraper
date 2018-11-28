#include <cstdio>
#include <queue>

using namespace std;

int main(){

  FILE * in = fopen("Omino.in", "r");
  FILE * out = fopen("Omino.out", "w");
  
  int t;

  fscanf(in,"%d",&t);

  for(int i=0;i<t;i++){  
    int x,r,c;
    fscanf(in,"%d %d %d",&x,&r,&c);
    bool richard=false;
    if(x<=r*c){
      if(r>c){
        if(x-c>c){
          richard = true;
        }else{
          if(x-c==r){
            richard = true;
          }
        }
      }else{
        if(x-r>r){
          richard = true;
        }else{
          if(x-c==r){
            richard = true;
          }
        }
      }
      if((r*c) % x > 0){
        richard = true;
      }
      if(x==4 & c*r==8){
        richard = true;
      }
    }else{
      richard=true;
    }

    if(richard){
      fprintf(out,"Case #%d: RICHARD\n",i+1);
    }else{
      fprintf(out,"Case #%d: GABRIEL\n",i+1);
    }
  }

  return 0;
}