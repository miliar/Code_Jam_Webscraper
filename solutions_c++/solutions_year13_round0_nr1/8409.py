#include<stdio.h>
#include<iostream.h>
#define maxn 10
using namespace std;
int gox[4]={1,0,1,1},goy[4]={0,1,1,-1};
char map[10][10];
int check(long i,long j,long bw){
	if(map[i][j]==bw||map[i][j]=='T')
		return 1;
	else
		return 0;
	}
void search(long num,long empty){
	long i,j,k,l,bw=0,ww=0;
	for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				for(k=0;k<4;k++)
					if(check(i+gox[k],j+goy[k],map[i][j])&&check(i+2*gox[k],j+2*goy[k],map[i][j])&&check(i+3*gox[k],j+3*goy[k],map[i][j])){
						if(map[i][j]=='X'){
							bw=1;
						}
						if(map[i][j]=='O'){
							ww=1;
						}
					}
	if(bw==0&&ww==0){
		if(empty==1){
		printf("Case #%d: Game has not completed",num);
		return;
		}
		else{
			printf("Case #%d: Draw",num);
			return;
		}	
	}
		
	if(bw==1&&ww==1){
		printf("Case #%d: Draw",num);
		return;
	}	
	if(bw==1){
		printf("Case #%d: X won",num);
		return;
	}
	if(ww==1){			
	printf("Case #%d: O won",num);
	return;
	}	
}	




int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);	
	long t;
	long i,j,k,l,num,empty=0;
	cin>>t;
	for(num=1;num<=t;num++){
		memset(map,-1,sizeof(map));
		empty=0;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++){
				cin>>map[i][j];
				if(map[i][j]=='.')
					empty=1;
				}
				search(num,empty);
			cout<<endl;
		}
	return 0;
	}
