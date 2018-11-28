#include <cstdio>
#include <cmath>
#include <string>
#include <cstdlib>

using namespace std;

int ctoi(char c){
  return (c-48);
}

int main(){
  FILE * in = fopen("StandingOvation.in", "r");
  FILE * out = fopen("StandingOvation.out", "w");

  int t;
  fscanf(in, "%d",&t);

  for(int i=0;i<t;i++){
    int s;
    char a[12345];
    fscanf(in, "%d %s",&s, a);

    int stand=ctoi(a[0]);
    int need=0;
    for(int j=1;j<=s;j++){
      int c = ctoi(a[j]);
      if(c>0){
        if(j>stand){
          need+=(j-stand);
          stand+=(c+j-stand);
        }else{
          stand+=c; 
        }
      }
    }
    fprintf(out,"Case #%d: %d\n",i+1,need);
  }
}