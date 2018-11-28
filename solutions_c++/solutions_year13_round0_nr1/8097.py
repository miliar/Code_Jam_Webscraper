#include<iostream>
#include<vector>
#include<string>
using namespace std;
struct p
{
	char c;
	int max;
};
vector<vector<char> >input()
{
	vector<vector<char> >vec;
	for(int i=0;i<4;i++)
	{
		vector<char>x;
		for(int j=0;j<4;j++)
		{
			char tmp;
			cin>>tmp;
			x.push_back(tmp);
		}
		vec.push_back(x);
	}
	return vec;
}
p diagonals(vector<vector<char> >vec)
{
	int dx=0,dy=0;
	bool dxch=true,dych=true;
	for(int d=0;d<4;d++)
	{
		if(vec[d][d]=='X')dx++;
		if(vec[d][d]=='O')dy++;
		if(vec[d][d]=='T'){dx++;dy++;}
		if(vec[d][d]=='X'&&(d==1||d==2))dych=false;
		if(vec[d][d]=='O'&&(d==1||d==2))dxch=false;
	}
	int rdx=0,rdy=0;
	bool rdxch=true,rdych=true;
	for(int d=0;d<4;d++)
	{
		int k=4-d-1;
		if(vec[d][k]=='X')rdx++;
		if(vec[d][k]=='O')rdy++;
		if(vec[d][k]=='T'){rdx++;rdy++;}
		if(vec[d][k]=='X'&&(d==1||d==2))rdych=false;
		if(vec[d][k]=='O'&&(d==1||d==2))rdxch=false;
	}
	int max=0;
	char maxch=0;
	if(dxch==true&&dx>max){max=dx;maxch='X';};
	if(rdxch==true&&rdx>max){max=rdx;maxch='X';};
	if(dych==true&&dy>max){max=dy;maxch='O';};
	if(rdych==true&&rdy>max){max=rdy;maxch='O';};
	p fin;
	fin.c=maxch;
	fin.max=max;
	return fin;
}
string search(vector<vector<char> >vec)
{
	//Check Diagonals:
	p fin=diagonals(vec);
	int max=fin.max;
	char maxch=fin.c;
	if(max==4)
	{
		string str="";
		str+=maxch;
		str+=" won";
		return str;
	}
	//Check All Matrix:
	int xs=0,os=0,dots=0;
	vector<bool>xch(4,true);
	vector<bool>rxch(4,true);
	vector<bool>och(4,true);
	vector<bool>roch(4,true);
	vector<int> vecx;
	vector<int>vecrx;
	vector<int>veco;
	vector<int>vecro;
	for(int i=0;i<4;i++)
	{
		int x=0,o=0,rx=0,ro=0;
		for(int j=0;j<4;j++)
		{
			if(vec[i][j]=='X'&&(j==1||j==2)){och[i]=false;}
			if(vec[j][i]=='X'&&(j==1||j==2)){roch[i]=false;}
			if(vec[i][j]=='O'&&(j==1||j==2)){xch[i]=false;}
			if(vec[j][i]=='O'&&(j==1||j==2)){rxch[i]=false;}
			if(vec[i][j]=='X'){x++;xs++;}
			if(vec[i][j]=='O'){o++;os++;}
			if(vec[j][i]=='X'){rx++;xs++;}
			if(vec[j][i]=='O'){ro++;os++;}
			if(vec[i][j]=='T'){x++;o++;}
			if(vec[j][i]=='T'){rx++;ro++;}
			if(vec[j][i]=='.'||vec[i][j]=='.'){dots++;}
		}
		vecx.push_back(x);
		vecrx.push_back(rx);
		veco.push_back(o);
		vecro.push_back(ro);
	}
	int max_X=0,max_O=0;
	for(int i=0;i<4;i++)
	{
		if(vecx[i]==4&&xch[i]==true)
		{
			if(vecx[i]>max_X)max_X=vecx[i];
		}
		if(vecrx[i]==4&&rxch[i]==true)
		{
			if(vecrx[i]>max_X)max_X=vecrx[i];
		}
		if(veco[i]==4&&och[i]==true)	
		{
			if(veco[i]>max_O)max_O=veco[i];
		}
		if(vecro[i]==4&&roch[i]==true)	
		{
			if(vecro[i]>max_X)max_O=vecro[i];
		}
	}
	if(max_X>max_O)return "X won";
	else if(max_X<max_O)return "O won";
	else if(max_X==max_O&&dots==0)return "Draw";
	if(dots>=xs&&dots>=os)
		return "Game has not completed";
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int TC;
	cin>>TC;
	for(int T=0;T<TC;T++)
	{
		vector<vector<char> >vec=input();
		cout<<"Case #"<<(T+1)<<": "<<search(vec)<<endl;
	}
}