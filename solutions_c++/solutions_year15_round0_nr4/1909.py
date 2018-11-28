#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<iostream>
using namespace std;

#define For(Q,W) for(int Q=0; Q<W; Q++)

string kto[] = {"RICHARD","GABRIEL"};
int ans[][4][4]={
  {{1,1,1,1},
   {1,1,1,1},
   {1,1,1,1},
   {1,1,1,1}    
  },
  {{0,1,0,1},
   {1,1,1,1},
   {0,1,0,1},
   {1,1,1,1}    
  },
  {{0,0,0,0},
   {0,0,1,0},
   {0,1,1,1},
   {0,0,1,0}    
  },
  {{0,0,0,0},
   {0,0,0,0},
   {0,0,0,1},
   {0,0,1,1}    
  }  
};



void solve(int T){
  int X,R,C;
  scanf("%d %d %d ",&X,&R,&C);
  
  printf("Case #%d: ",T+1);
  cout<<kto[ans[X-1][R-1][C-1]]<<endl;
}

int main(){
  int T;
  scanf("%d ",&T);
  For(i,T) solve(i);
  return 0;
}

