#include<iostream>
#include<string>
#include<algorithm>
#include<math.h>
#include<memory.h>
#include<stdio.h>
#include<vector>
using namespace std;
int o,x,d,t;
char z[5][5];
bool f(char a){
    int c=0,i,j;
	for(i=0;i<4;i++,c=0){
		for(j=0;j<4;j++)
			if(z[i][j]==a||z[i][j]=='T')
				c++;
			if(c==4)
				return true;
	}
	for(i=0;i<4;i++,c=0){
		for(j=0;j<4;j++)
			if(z[j][i]==a||z[j][i]=='T')
				c++;
			if(c==4)
				return true;
	}
	c=0;
	for(i=0;i<4;i++)
		if(z[i][i]==a||z[i][i]=='T')
			c++;
	if(c==4)
		return true;
	c=0;
	for(i=0;i<4;i++)
		if(z[i][3-i]==a||z[i][3-i]=='T')
			c++;
	if(c==4)
		return true;
	return false;
}
int main(){
	freopen("src.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for(int i=0;i<t;i++){
		o=x=d=0;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				cin>>z[j][k];
				if(z[j][k]=='.')d++;
				else if(z[j][k]=='O')o++;
				else if(z[j][k]=='X')x++;
			}
		}
		if(f('X')){
			cout<<"Case #"<<i+1<<": X won"<<endl;
			continue;
		}
		else if(f('O')){
			cout<<"Case #"<<i+1<<": O won"<<endl;
			continue;
		}
		else if(!d){
			cout<<"Case #"<<i+1<<": Draw"<<endl;
			continue;
		}
		else cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
	}
	return 0;
}