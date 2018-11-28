#include<cstdio>
#include<map>
#include<algorithm>
#include<cstring>

using namespace std;
char arr[4][4];
char sv[4][4];
int lastchar;

bool dfs(char last,int x,int y,int lvl,int ts)
{
}

int main()
{
	int tc,T;
	scanf(" %d",&T);
	for(tc=1;tc<=T;tc++){
		int i,j;
		for(i=0;i<4;i++) scanf(" %s",arr[i]);
		bool done=false;
		char donebychar='.';
		int dotsrem=0;
		int dx[4]={1,1,1,0};
		int dy[4]={0,1,-1,1};
		int k,p;
		memcpy(sv,arr,sizeof(sv));
		for(i=0;i<4 && !done;i++) {
		for(j=0;j<4 && !done;j++) {
			if(arr[i][j]=='.') dotsrem++;
			for(k=0;k<4  && !done;k++){
			   int nx=i,ny=j;
			   char thischar=arr[nx][ny];
			   map<char,int> M;
			   M[thischar]++;
			   for(p=0;p<4;p++){
				nx+=dx[k];
				ny+=dy[k];
				if(nx<0 || nx>3) continue;
				if(ny<0 || ny>3) continue;
				M[arr[nx][ny]]++;
			   }
			   if(M['X']==3 && M['T']==1) { done=true;donebychar='X'; }
			   if(M['X']==4 ) { done=true; donebychar='X'; }
			   if(M['O']==4 ) { done=true; donebychar='O'; }
			   if((M['O']==3)  && (M['T']==1)) { done=true; donebychar='O'; }
		
			}
		   }
		}
		printf("Case #%d: ",tc);
		if(done ){
			printf("%c won\n",donebychar);
		} else {
			if(dotsrem==0) printf("Draw\n");
			else printf("Game has not completed\n");
		}
		
	}
	return 0;
}
	
