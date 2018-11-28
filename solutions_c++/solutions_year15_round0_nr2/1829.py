#include<stdio.h>
#include<list>
using namespace std;

/*

    list<int>p;
    for(int i=0;i<D;i++){ 
      int hp;scanf("%d",&hp);
      p.push_back(hp);
    }
    p.sort();    //FAIL: 2 2 9 -> 6 instead of 5 (2,2,6,3 -> 2,2,3,3,3)
    int res=p.back();
    list<int>::iterator i
      for(it=p.begin();it!=p.end();it++)
        printf("%4d",*it);
      printf("\n");
    for(int s=1;s<=res;s++){
      list<int>::iterator it=p.begin();
      int r=p.back();
      p.pop_back();
      int is[2]={r/2,r-r/2};
      it=p.begin();
      for(int i=0;i<2;i++){
        while(it!=p.end()&& *it<is[i]) it++;
        it=p.insert(it,is[i]);
      }
      if(p.back()+s<res) res=p.back()+s;
    }
    p.clear();
*/

int p[1000];

int main(int agrc,char*argv[]){
  int T;scanf("%d",&T);
  for(int tc=1;tc<=T;tc++){
    int D;scanf("%d",&D);
    for(int i=0;i<D;i++)
      scanf("%d",&p[i]);
    int res=1000;
    for(int v=1;v<=1000;v++){
      int sm=v;
      for(int i=0;i<D;i++)
        if(p[i]>v)
          sm+=(p[i]-1)/v;
      if(sm<res) res=sm;
    }
    printf("Case #%d: %d\n",tc,res);
  }
  return 0;
}
