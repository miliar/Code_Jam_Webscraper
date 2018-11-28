#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;
int ca[10][10],cb[10][10];
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tcas,cas;
	while(~scanf("%d",&tcas)){
		for(cas=0;cas<tcas;cas++){
			int rowa,rowb,res=0,cot=0;
			scanf("%d",&rowa);
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					scanf("%d",&ca[i][j]);
				}
			}
			scanf("%d",&rowb);
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					scanf("%d",&cb[i][j]);
				}
			}
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					if(ca[rowa-1][i]==cb[rowb-1][j]){
					res=ca[rowa-1][i];
					cot++;}
				}
			}
			if(cot==0)printf("Case #%d: Volunteer cheated!\n",cas+1);
			else if(cot>1)printf("Case #%d: Bad magician!\n",cas+1);
			else printf("Case #%d: %d\n",cas+1,res);			
		}
	}
	
	return 0;
} 
/*
Input 
3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Output 
Case #1: 7
Case #2: Bad magician!
Case #3: Volunteer cheated!
*/