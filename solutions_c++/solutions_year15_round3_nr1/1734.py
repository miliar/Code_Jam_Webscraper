#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<cstring>

typedef long long ll;

using namespace std;

int T,R,C,W;

int main()
{
  FILE *ifp,*ofp;
  int ret;
  ofp=fopen("A-small-attempt1-result.in","w");
  if((ifp=fopen("A-small-attempt1.in","r"))!=NULL){
    fscanf(ifp,"%d",&T);
    for(int i=0;i<T;i++){
      fscanf(ifp,"%d",&R);
      fscanf(ifp,"%d",&C);
      fscanf(ifp,"%d",&W);
      int tmp=C%W==0?C/W:C/W+1;
      ret=tmp*R+(W-1);
    
      fprintf(ofp,"Case #%d: %d\n",i+1,ret);
      printf("Case #%d: %d\n",i+1,ret);
    }
  }
  fclose(ifp);
  fclose(ofp);
}
