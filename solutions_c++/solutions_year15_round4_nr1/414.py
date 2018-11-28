#include<cstdio>
#include<algorithm>
#include<map>
#include<string>
#include<cstring>
using namespace std;
char mapa[201][201];
pair<int,int> grafo[201][201];
int dir[4][2]= {{0,1},{0,-1},{1,0},{-1,0}};
int calc(char c){
  if (c=='^')
    return 3;
  if (c=='v')
    return 2;
  if (c=='<')
    return 1;
  if (c=='>')
    return 0;
  throw "perdi";
}
int main () {
  int tt;
  scanf("%d",&tt);
  
  for(int rr=1;rr<=tt;rr++) {
    int n=0,m=0;
    scanf("%d %d",&n, &m);
    memset(mapa,0,sizeof(mapa));
    for(int i=1;i<=n;i++)
      for(int j=1;j<=m;j++)
	{
	  scanf(" %c",&mapa[i][j]);
	}
    int ret =0;
    bool fudeu = false;
    for(int i=1;i<=n;i++){
      for(int j=1;j<=m;j++){
	if(mapa[i][j]!='.'){
	  int x=i,y=j;
	  int r = calc(mapa[i][j]);
	  do{
	    x += dir[r][0];
	    y += dir[r][1];
	  }while(mapa[x][y]=='.');

	  if(mapa[x][y]==0){
	    bool ok = false;
	    for(int r=0;r<4;r++)
	      {
		int z=i,w=j;
	    
	    
		do{
		  z += dir[r][0];
		  w += dir[r][1];
		}while(mapa[z][w]=='.');
		
		if(mapa[z][w]!=0){ret++;ok=true;break;}
	      }
	    if(!ok)
	      {
		fudeu = true;
	      }
	  }
	}
	
      }
      
    }
    printf("Case #%d: ",rr);
    if(fudeu)printf("IMPOSSIBLE\n");
    else printf("%d\n",ret);
  }
  return 0;
}
