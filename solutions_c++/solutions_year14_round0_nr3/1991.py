#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#define mp(a,b) make_pair((a),(b))
#define ff first
#define ss second

using namespace std;

int dfs(int i, int j, vector<vector<int> > &test, vector<vector<int> > &mam){
  //printf("DFS: spracovavam bod %d %d\n",i,j);
  if((i==0) || (i==((int)test.size()-1)) || (j==0) || (j==((int)test[0].size()-1))){
    //printf("DFS: %d %d\n",i,j);
    //printf("DFS: som mimo planu: %d %d\n",((int)test.size()-1),((int)test[0].size()-1));
    return 0;
  }
  //printf("DFS: tento bod mam: %d\n",mam[i][j]);
  if(mam[i][j]==0){
    //printf("DFS: zistujem, ci hladam dalej\n");
    mam[i][j]=1;
    if(test[i][j]==0){
      //printf("DFS: hladam dalej\n");
      dfs(i-1,j-1,test,mam);
      dfs(i-1,j,test,mam);
      dfs(i-1,j+1,test,mam);
      dfs(i,j-1,test,mam);
      dfs(i,j+1,test,mam);
      dfs(i+1,j-1,test,mam);
      dfs(i+1,j,test,mam);
      dfs(i+1,j+1,test,mam);
    }
  }
  return 0;
}

int main(){
  int i,j,k,l,m,r,s,t,u,v;
  int ok;
  vector<vector<int> > pole,test,mam;
  vector<int> mines;
  
  scanf("%d",&t);
  
  for(l=1;l<=t;l++){
    scanf("%d",&r);
    scanf("%d",&s);
    scanf("%d",&m);
    
    if(r*s==m){
      printf("Case #%d:\nImpossible\n",l);
      continue;
    }
    
    pole.clear();
    pole.resize(r+2);
    test.resize(r+2);
    
    mines.clear();
    mines.resize(r*s,0);
    
    for(i=r*s-m;i<r*s;i++){
      mines[i]=1;
    }
    
    for(i=0;i<r+2;i++){
      pole[i].resize(s+2,0);
      test[i].resize(s+2,0);
    }
    
    do{
      
      /*printf("Mines:\n");
      for(i=0;i<r*s;i++){
	printf("%d ",mines[i]);
      }putchar('\n');*/
      
      for(i=1;i<r+1;i++){
	for(j=1;j<s+1;j++){
	  pole[i][j]=-mines[(i-1)*s+j-1];
	}
      }
      
      /*printf("Iba miny:\n");
      for(i=1;i<r+1;i++){
	for(j=1;j<s+1;j++){
	  printf("%d ",pole[i][j]);
	}putchar('\n');
      }*/
      
      for(i=1;i<r+1;i++){
	for(j=1;j<s+1;j++){
	  test[i][j]=-(pole[i-1][j-1]+pole[i-1][j]+pole[i-1][j+1]+pole[i][j-1]+pole[i][j+1]+pole[i+1][j-1]+pole[i+1][j]+pole[i+1][j+1]);
	}
      }
      
      /*printf("Hracie pole:\n");
      for(i=1;i<r+1;i++){
	for(j=1;j<s+1;j++){
	  printf("%d ",test[i][j]);
	}putchar('\n');
      }*/
      
      ok=0;
      for(i=1;i<r+1;i++){
	for(j=1;j<s+1;j++){
	  if(pole[i][j]==-1){
	    continue;
	  }
	  mam.clear();
	  mam.resize(r+2);
	  for(k=0;k<r+2;k++){
	    mam[k].resize(s+2,0);
	  }
	  
	  dfs(i,j,test,mam);
	  
	  /*printf("DFS z bodu %d %d naslo:\n",i,j);
	  for(u=1;u<r+1;u++){
	    for(v=1;v<s+1;v++){
	      printf("%d ",mam[u][v]);
	    }putchar('\n');
	  }*/
	  
	  ok=1;
	  for(u=1;u<r+1;u++){
	    for(v=1;v<s+1;v++){
	      if(mam[u][v]!=1 && pole[u][v]!=-1){
		ok=0;
		break;
	      }
	    }
	    if(!ok){
	      break;
	    }
	  }
	  if(ok){
	    printf("Case #%d:\n",l);
	    
	    for(u=1;u<r+1;u++){
	      for(v=1;v<s+1;v++){
		if(u==i && v==j){
		  putchar('c');
		}else{
		  if(pole[u][v]==-1){
		    putchar('*');
		  }else{
		    putchar('.');
		  }
		}
	      }putchar('\n');
	    }
	    break;
	    
	  }
	  
	}
	if(ok){break;}
      }
      if(ok){break;}
    }while(next_permutation(mines.begin(),mines.end()));
    if(!ok){
      printf("Case #%d:\nImpossible\n",l);
    }
  }
  
  return 0;
}
