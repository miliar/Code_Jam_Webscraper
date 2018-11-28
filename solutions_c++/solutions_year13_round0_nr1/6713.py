#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;
int main(){
	int tc;
	scanf("%d",&tc);
	int l=1;
	while(tc--){
		vector<int>v[10];
		int i;
		int j;
		char c;
		int a=-1;
		int fl=1;
		for(i=0;i<10;i++){
			for(j=0;j<4;j++){
				v[i].push_back(0);
			}
		}
		char st[4];
		for(i=0;i<4;i++){
			scanf("%s",st);
			for(j=0;j<4;j++){
				if(i==j){
					if(st[j]=='X'){
						v[8][0]++;
					}
					else if(st[j]=='O'){
						v[8][1]++;
					}
					else if(st[j]=='.'){
						v[8][2]++;
					}
					else if(st[j]=='T'){
						v[8][3]++;
					}
				}
				if((i+j)==3){
					if(st[j]=='X'){
						v[9][0]++;
					}
					else if(st[j]=='O'){
						v[9][1]++;
					}
					else if(st[j]=='.'){
						v[9][2]++;
					}
					else if(st[j]=='T'){
						v[9][3]++;
					}
				}


				if(st[j]=='X'){
					v[i][0]++;
					v[j+4][0]++;
				}
				else if(st[j]=='O'){
					v[i][1]++;
					v[j+4][1]++;
				}
				else if(st[j]=='.'){
					v[i][2]++;
					v[j+4][2]++;
				}
				else if(st[j]=='T'){
					v[i][3]++;
					v[j+4][3]++;
				}
			}
		}
		int em=0;
		a=-1;
		for(i=0;i<10;i++){
			if(v[i][2]!=0){
				em=1;
			}
			if(v[i][0]==4 || (v[i][0]==3 && v[i][1]==0 && v[i][2]==0 && v[i][3]==1)){
				a=0;
			}
			if(v[i][1]==4 || (v[i][0]==0 && v[i][1]==3 && v[i][2]==0 && v[i][3]==1)){
				a=1;
			}
		}

		if(a==0){
			printf("Case #%d: X won\n",l);
		}
		if(a==1){

			printf("Case #%d: O won\n",l);
		}
		if(a==-1){
			if(em==1){
				printf("Case #%d: Game has not completed\n",l);
			}
			else{
				printf("Case #%d: Draw\n",l);
			}
		}
		l++;
	}
	return 0;
}
