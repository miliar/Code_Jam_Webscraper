#include <vector>
#include <cstdio>
#include <queue>
#include <string>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;
 
#define LENDICT 26  
#define CANTIDAD 10
#define LEN 20
int root;
int Sce_k=0;
 
struct node {
   char flag;
   int p[LENDICT];
   void clear(){
        memset( p, -1, sizeof p );
        flag = 0;
    }
};
 
node dict[CANTIDAD*LEN];
 
int new_node() {
   dict[Sce_k].clear();
   return Sce_k++;
}

void addword(char buff[LEN+1])
{   
  int t=root;
       
      for( char *c = buff; *c; ++c ){
         if( dict[t].p[*c-'A'] == -1 )
            dict[t].p[*c-'A'] = new_node();
            t= dict[t].p[*c-'A'];
      }
      dict[t].flag = 1;
}

char arr[30][LEN+1];
int n,m;
int  adall(vector <int> S) {
   Sce_k=0;
   root = new_node();
  
  for(int i=0;i<S.size();i++) {
    addword(arr[S[i]]);
  }
  return Sce_k;
}
int main(){
  int runs;
  scanf("%d",&runs);
  for(int t=1;t<=runs;t++){
    scanf("%d %d",&m,&n);
    for(int i=0;i<m;i++) scanf("%s",arr[i]);
    if(n == 1){
      vector <int> idx;
      for(int i=0;i<m;i++)idx.push_back(i);
	  printf("Case #%d: ",t);
      cout<<adall(idx)<<" "<<1<<endl;
      continue;
    }
    int best = 0, num = 0;
    int BK = 2*m;
    int sz = (1<<BK);
    for(int i=1;i<sz;i++){
      int mask = i;
      bool cagao = false;
      vector < vector <int> > dict(n);
      for(int j = 0; j< m; j++){
        int R = mask%4;
        if(R >= n) cagao = true;
        if(cagao)break;
       dict[R].push_back(j);
        mask /= 4;
      }
      if(cagao) continue;
      int m1 = 0 ;
      for(int j=0;j<dict.size();j++){
          if(dict[j].size() == 0) cagao = true;
          m1 += adall(dict[j]);
        }
      if(cagao)continue; 
      if(m1>best){
          best = m1;
          num = 1;
        }
        else if(m1 == best)
          num++; 
    }
	printf("Case #%d: ",t);
    cout<<best<<" "<<num<<endl;
  }
  return 0;
}
