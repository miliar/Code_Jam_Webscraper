#include<iostream>
#include<string>
#include<map>
using namespace std;
string f[4];
int search(int i,int j,int x,int y,char a)
{
	if(i==4 || j==4 || i<0 || j<0) return 0;
	if(f[i][j]!=a and f[i][j]!='T') return 0;
	return 1+search(i+x,j+y,x,y,a);
}
int main()
{
	int cas;
	cin>>cas;
	map<char,bool>x;
	for(int cass=0;cass<cas;cass++){
	for(int i=0;i<4;i++) cin>>f[i];
	bool af2=true;
	x['O']=false;
	x['X']=false;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(f[i][j]=='T') continue;
			if(f[i][j]=='.') {af2=false;continue;}
			if(search(i,j,1,-1,f[i][j])==4) x[f[i][j]]=true;
			if(search(i,j,-1,0,f[i][j])==4)x[f[i][j]]=true;
			if(search(i,j,-1,1,f[i][j])==4)x[f[i][j]]=true;
			if(search(i,j,-1,-1,f[i][j])==4)x[f[i][j]]=true;
			if(search(i,j,0,1,f[i][j])==4)x[f[i][j]]=true;
			if(search(i,j,0,-1,f[i][j])==4)x[f[i][j]]=true;
			if(search(i,j,1,0,f[i][j])==4)x[f[i][j]]=true;
			if(search(i,j,1,1,f[i][j])==4)x[f[i][j]]=true;
		}
	}
	bool n=x['O'],m=x['X'];
	cout<<"Case #"<<cass+1<<": ";
	if(n) cout<<"O won";
	if(m) cout<<"X won";
	if(!n and !m) {if(af2) cout<<"Draw"; else cout<<"Game has not completed";}
	cout<<endl;}
	return 0;
}
