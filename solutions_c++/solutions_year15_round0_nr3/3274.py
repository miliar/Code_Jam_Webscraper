#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#define mx(a,b) ((a>b)? a:b)
#define mn(a,b) ((a<b)? a:b)
#define inf 2000000000
using namespace std;
int cmd[300][300][3];
char str[10100],tmp[10100],tab[10100][10100];
void solve(){
	cmd[1][1][0]=1; cmd[1][1][1]=1;
	cmd['i']['i'][0]=cmd['j']['j'][0]=cmd['k']['k'][0]=1;
	cmd['i']['i'][1]=cmd['j']['j'][1]=cmd['k']['k'][1]=-1;
	cmd['i'][1][0]=cmd[1]['i'][0]=cmd['j']['k'][0]='i';
	cmd['i'][1][1]=cmd[1]['i'][1]=cmd['j']['k'][1]=1;
	cmd['j'][1][0]=cmd[1]['j'][0]=cmd['k']['i'][0]='j';
	cmd['j'][1][1]=cmd[1]['j'][1]=cmd['k']['i'][1]=1;
	cmd['k'][1][0]=cmd[1]['k'][0]=cmd['i']['j'][0]='k';
	cmd['k'][1][1]=cmd[1]['k'][1]=cmd['i']['j'][1]=1;
	cmd['k']['j'][0]='i'; cmd['k']['j'][1]=-1;
	cmd['i']['k'][0]='j'; cmd['i']['k'][1]=-1;
	cmd['j']['i'][0]='k'; cmd['j']['i'][1]=-1;
	int T;
	scanf("%d",&T);
	for(int l=1;l<=T;l++){
		int len,re,x=1,c=1;
		scanf("%d %d %s",&len,&re,str);
		len*=re;
		strcpy(tmp,str);
		while(--re)
			strcat(str,tmp);
		// printf("%d %s\n",len,str);
		for(int i=0;i<len;i++){
			int x=1,c=1;
			for(int j=i;j<len;j++){
				c*=cmd[x][str[j]][1];
				x=cmd[x][str[j]][0];
				if(c==1)
					tab[i][j]=x;
				else
					tab[i][j]=-1;
			}
		}
		for(int i=0;i<len;i++){
			if(tab[0][i]=='i'){
				for(int j=i+1;j<len;j++){
					if(tab[i+1][j]=='j' && tab[j+1][len-1]=='k'){
						printf("Case #%d: Yes\n",l);
						goto AAA;
					}
				}
			}
		}
		printf("Case #%d: NO\n",l);
		AAA:;
	}
}
int main(){
	solve();
	return 0;
}