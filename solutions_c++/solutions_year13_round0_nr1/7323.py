#include<cstdio>

bool ans[2];
int caso,C;
char s[10][10];
void doit(){
	ans[0]=false,ans[1]=false;
	for(int i=0;i<4;++i)scanf("%s",s[i]);
	for(int i=0;i<4;++i)
		for(int k=0;k<2;++k){
			char c= (k==0? 'X':'O');
			bool valid=true;
			for(int j=0;j<4;++j)if(s[i][j]!=c && s[i][j]!='T')valid=false;
			if(valid)ans[k]=true;
			}
	for(int i=0;i<4;++i)
		for(int k=0;k<2;++k){
			char c= (k==0? 'X':'O');
			bool valid=true;
			for(int j=0;j<4;++j)if(s[j][i]!=c && s[j][i]!='T')valid=false;
			if(valid)ans[k]=true;
			}
	for(int k=0;k<2;++k){
		char c= (k==0? 'X':'O');
		bool valid=true;
		for(int i=0;i<4;++i)if(s[i][i]!=c && s[i][i]!='T')valid=false;
		if(valid)ans[k]=true;
		valid=true;
		for(int i=0;i<4;++i)if(s[i][3-i]!=c && s[i][3-i]!='T')valid=false;
		if(valid)ans[k]=true;
		}
	
	bool end =true;
	for(int i=0;i<4;++i)
		for(int j=0;j<4;++j)if(s[i][j]=='.')end=false;
	if(!ans[0] && !ans[1]){
		if(end)printf("Case #%d: Draw\n",++caso);
		else printf("Case #%d: Game has not completed\n",++caso);
		}
	else if(ans[0])printf("Case #%d: X won\n",++caso);
	else if(ans[1])printf("Case #%d: O won\n",++caso);
	}
int main(){
	scanf("%d",&C);
	caso=0;
	for(int i=0;i<C;++i)doit();
	}
