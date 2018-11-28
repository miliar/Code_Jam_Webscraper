#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int T,total,ret,temp;
int map[10][10],used[10][10];

int answer(){
	for(int j=1;j<=4;j++){
		ret=1;
		temp=map[j][1];
		if(temp=3) temp=map[j][2];
		for(int i=1;i<=4;i++){
			if(map[j][i]==3) continue; 
			if(map[j][i]!=temp||temp==0) {
			    ret=0;break;
			}
		}
		if(ret) return temp;
	}
	for(int j=1;j<=4;j++){
		ret=1;
		temp=map[1][j];
		if(temp=3) temp=map[2][j];
		for(int i=1;i<=4;i++){
			if(map[i][j]==3) continue;
			if(map[i][j]!=temp||temp==0) {
			    ret=0;break;
			}
		}
		if(ret) return temp;
	}

	ret=1;
	temp=map[1][1];
	if(temp=3) temp=map[2][2];
	for(int i=1;i<=4;i++){
	    if(map[i][i]==3) continue;
		if(map[i][i]!=temp||temp==0) {
		    ret=0;break;
		}
	}
	if(ret) return temp;
	
	ret=1;
	temp=map[1][4];
	if(temp=3) temp=map[2][3];
	for(int i=1;i<=4;i++){
		if(map[i][5-i]==3) continue;
		if(map[i][5-i]!=temp||temp==0) {
		    ret=0;break;
		}
	}
	if(ret) return temp;
	
	return 0;
}

int main(){
	freopen("A-small-attempt3.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	int TT=T;
	while(T--){
		memset(map,0,sizeof(map));
		total=0;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				char temp_in;
				cin>>temp_in;
				if(temp_in=='X') {
				map[i][j]=1;total++;}
				if(temp_in=='O') {
				map[i][j]=2;total++;}
				if(temp_in=='T') {
				map[i][j]=3;total++;}
			}
	    }
	    int temp_ans;
	    temp_ans=answer();
	    if(temp_ans==1) cout<<"Case #"<<TT-T<<": X won"<<endl;
		if(temp_ans==2) cout<<"Case #"<<TT-T<<": O won"<<endl;
		if(temp_ans==0&&total==16) cout<<"Case #"<<TT-T<<": Draw"<<endl;
		if(temp_ans==0&&total<16) cout<<"Case #"<<TT-T<<": Game has not completed"<<endl;
	}
	return 0;
}
