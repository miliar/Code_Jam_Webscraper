#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;
#define MAX 6
int adj[2][MAX][MAX];
int ans[2],re;
int ssort(){
	int i2=ans[1];
	int j1=1,j;
	bool fl=false;
	int i = ans[0];
		for(j=1;j<=4;j++){
			for(j1=1;j1<=4;j1++){
				if(adj[0][i][j]==adj[1][i2][j1]){
					if(!fl){
						re = adj[0][i][j];
						fl = true;
					}
					else{
						return 0;
					}
				}		
			}	

		}
	if(fl)
	return 1;
	else
	return 2;

}
int main(){
	int T,i,j,k;
	FILE *o = fopen("ans.txt","w");	
	scanf("%d",&T);
	int c=0;
while(T--){
	int ss=2;
	c++;
	k=0;
	while(ss--){

	scanf("%d",&ans[k]);

	for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
		scanf("%d",&adj[k][i][j]);
		
	k++;
	}
			
	int f = ssort();
	if(f==1)
	fprintf(o,"Case #%d: %d\n",c,re);
	else if(f==2)
	fprintf(o,"Case #%d: Volunteer cheated!\n",c);
	else
	fprintf(o,"Case #%d: Bad magician!\n",c);
	

}
	fclose(o);	

return 0;
}
