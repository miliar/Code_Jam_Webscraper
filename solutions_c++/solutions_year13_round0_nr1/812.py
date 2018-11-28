#include<iostream>
#include<stdio.h>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
int ca,ti,i,j,cnt;
char g[4][4];
bool same(char a,char b){
	return a==b||b=='T';
}
bool win(char ch){
	int i;
	fr(i,0,3)
		if(same(ch,g[i][0])&&same(ch,g[i][1])&&same(ch,g[i][2])&&same(ch,g[i][3]))
			return true;
	fr(i,0,3)
		if(same(ch,g[0][i])&&same(ch,g[1][i])&&same(ch,g[2][i])&&same(ch,g[3][i]))
			return true;
	return same(ch,g[0][0])&&same(ch,g[1][1])&&same(ch,g[2][2])&&same(ch,g[3][3])||same(ch,g[0][3])&&same(ch,g[1][2])&&same(ch,g[2][1])&&same(ch,g[3][0]);
}
int main(){
	freopen("a2.in","r",stdin);
	freopen("a2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		fr(i,0,3)
			scanf("%s",g[i]);
		cout<<"Case #"<<ti<<": ";
		if(win('X'))
			cout<<"X won"<<endl;
		else
			if(win('O'))
				cout<<"O won"<<endl;
			else{
				cnt=0;
				fr(i,0,3)
					fr(j,0,3)
						cnt+=(g[i][j]=='.');
				if(cnt==0)
					cout<<"Draw"<<endl;
				else
					cout<<"Game has not completed"<<endl;
			}
				
	}
}