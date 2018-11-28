#include <iostream>
#include <string>
using namespace std;

int R,C;
int d[100][100];//d[R][C]
int parse(char c)
{
	if(c=='^')return 1;
	if(c=='>')return 2;
	if(c=='v')return 3;
	if(c=='<')return 4;
	return 0;
}

bool det(int x,int y,int c)
{
	int dx=0,dy=0;
	if(c==1)dx=-1;
	if(c==3)dx=1;
	if(c==2)dy=1;
	if(c==4)dy=-1;
	do{
		x+=dx;y+=dy;
		if(x<0 || x>=R || y<0 ||y>=C)return false;
	}
	while(d[x][y]==0);
	return true;
}

string calc()
{
	char l[256];
	
	cin>>R>>C;cin.getline(l,1);
	for(int i=0;i<R;i++)
	{
		cin.getline(l,256);
		for(int j=0;j<C;j++)
		{
			d[i][j]=parse(l[j]);
		}
	}

	
	int cnt=0;
	for(int i=0;i<R;i++)
	for(int j=0;j<C;j++)
	if(d[i][j]>0)
	{
		int x=i;int y=j;
		bool flag=det(x,y,d[i][j]);
		if(!flag)
		{
			if(det(x,y,1)||det(x,y,2)||det(x,y,3)||det(x,y,4))cnt++;
			else return "IMPOSSIBLE";
		}
	}
	//cerr<<"cnt:"<<cnt<<endl;
	sprintf(l,"%d",cnt);
	return string(l);
}

int main()
{
	//cout<<calc();return 0;
	int N;cin>>N;
	for(int i=0;i<N;i++)
		cout<<"Case #"<<(i+1)<<": "<<calc()<<endl;
	return 0;
}