#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{	
	int n;
	int nx=0;
	int no=0;
	int np=0;
	int nt=0;
	int f=0;
	int t=0;
	int t2=0;	
	int cont=1;
	char mat[16];
	cin>>n;

	for(int z=0; z<n; z++)
	{
		for(int i=0; i<16; i++)
		{		
			cin>>mat[i];				
		}

		for(int i=0; i<10; i++)
		{
			if(i==5)
				t2=1;
			else if(i==6)
				t2=2;
			else if(i==7)
				t2=3;
			else if(i==8)
				t2=0;
			else if(i==9)
				t2=3;

			for(int j=0; j<4; j++)
			{
				if(i>=0 && i<4)
				{
					if(mat[t]=='X')
						nx++;
					else if(mat[t]=='O')
						no++;
					else if(mat[t]=='T')
						nt++;
					else 
						np++;
					t++;
				}
				else if(i>=4 && i<8)
				{
					if(mat[t2]=='X')
						nx++;
					else if(mat[t2]=='O')
						no++;
					else if(mat[t2]=='T')
						nt++;
					else
						np++;
					t2+=4;
				}
				else if(i==8)
				{
					if(mat[t2]=='X')
						nx++;
					else if(mat[t2]=='O')
						no++;
					else if(mat[t2]=='T')
						nt++;
					else
						np++;
					t2+=5;
				}		
				else if(i==9)
				{
					if(mat[t2]=='X')
						nx++;
					else if(mat[t2]=='O')
						no++;
					else if(mat[t2]=='T')
						nt++;
					else
						np++;
					t2+=3;
				}
			}
			
			if(nx==4 || (nx==3&&nt==1))
			{
				f=1;
				break;
			}
			else if(no==4 || (no==3&&nt==1))
			{
				f=2;
				break;
			}
			else
			{					
				nx=0;
				no=0;	
				nt=0;
			}
		}
		
		if(f==1)		
			cout<<"Case #"<<cont<<": "<<"X won"<<endl;
		else if(f==2)
			cout<<"Case #"<<cont<<": "<<"O won"<<endl;
		else
		{
			if(np>0)
				cout<<"Case #"<<cont<<": "<<"Game has not completed"<<endl;
			else
				cout<<"Case #"<<cont<<": "<<"Draw"<<endl;
		}
		f=0;
		nx=0;
		no=0;
		np=0;
		nt=0;
		t=0;
		t2=0;
		cont++;
	}
	
	return 0;
}

