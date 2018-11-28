#include <iostream> 
#include <stdio.h>
using namespace std;
char m;int map[4][4];int heng[4],shu[4],xie[2];int all;
void inti()
{
	
	for(int i=0;i<4;i++)
	{
		heng[i] = 0;
		shu[i] =0;
	}
	xie[0] =0;
	xie[1] =0;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			cin>>m;
			if(m=='X')
			{
				map[i][j]=1;
				all++;
			}
			if(m=='O')
			{
				map[i][j]=-1;
				all++;
			}
			if(m=='T')
			{
				map[i][j]=0;
				all++;
			}
			if(m=='.')
			    map[i][j]=65535;
			//if(j!=3)
			//	cout<<map[i][j]<<" ";
		//	else
			 //   cout<<map[i][j]<<endl;
			
		}
		
	}
}

int find()
{
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			heng[i] += map[i][j];
			shu[i] += map[j][i];
		}
		//cout<<"heng["<<i<<"] = "<<heng[i]<<endl;
		//cout<<"shu["<<i<<"] = "<<shu[i]<<endl;
		if(heng[i] == 4 || heng[i]== 3 || shu[i] == 4 || shu[i]== 3)
			return 1;
		else
		{
			if(heng[i] == -4 || heng[i]== -3 ||shu[i] == -4 || shu[i]== -3)
				return -1;
		}
	}
	for(int i=0;i<4;i++)
	{
		xie[0] += map[i][i];
		xie[1] += map[i][3-i];
	}
	for(int i=0;i<2;i++)
	{
		//cout<<"xie["<<i<<"] = "<<xie[i]<<endl;
		if(xie[i]==3 || xie[i]==4 )
			return 1;
		else
		{
			if(xie[i]==-3 || xie[i]==-4)
				return -1;
		}
	}
	
    return 0;	
			
}



int main()
{
	int num;
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>num;
	for(int n=1;n<=num;n++)
	{
		all=0;
		inti();
		int ans = find();
		//cout<<endl<<ans<<endl;
		//cout<<endl<<all<<endl;
		if(ans == 1)
		{
			cout<<"Case #"<<n<<": X won"<<endl;
			continue;	
		}
		if(ans == -1 )
		{
			cout<<"Case #"<<n<<": O won"<<endl;
			continue;	
		}	
		if(ans == 0)
		{
			if(all==16)
			{
				cout<<"Case #"<<n<<": Draw"<<endl;
			}
			else
				cout<<"Case #"<<n<<": Game has not completed"<<endl;
		}
		
		
	}
	
}
