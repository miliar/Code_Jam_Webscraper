#include<iostream>
using namespace std;

int main()
{	int x=1;
	char tt[4][4];
	int t,i,k=-1;
	char ch;
	cin>>t;
	while(t>0)
	{	
		for(int iA=0;iA<4;iA++)
		{	for(int j=0;j<4;j++)
			{	cin>>tt[iA][j];
			}
		}
		cout<<"Case #"<<x++<<": ";	
		if(tt[0][0]=='O')	
		{	k=-1;
			i=1;
			while((tt[i][i]== 'O') || (tt[i][i]=='T') && i<4)
				{	
					k=i;
					i++;
				}
			if(k==3) 
					{	cout<<"O won\n";
						goto l1;
					}	
		}
			
		else if(tt[0][0]=='X')	
		{	k=-1;
			i=1;
			while((tt[i][i]== 'X') || (tt[i][i]=='T') && i<4)
				{	
					k=i;
					i++;
				}
			if(k==3) 
					{	cout<<"X won\n";
						goto l1;
					}	
		}
		
		else if(tt[0][0]=='T')
		{	ch=tt[1][1];
			i=2;
			k=-1;
			while((tt[i][i]== ch) && i<4)
				{	
					k=i;
					i++;
				}
			
			if(k==3 && ch!='.') 
					{	cout<<ch<<" won\n";
						goto l1;
					}	
		}
		if(tt[0][3]=='O')	
		{	k=-1;
			i=1;
			while(((tt[i][3-i]== 'O') || (tt[i][3-i]=='T')) && i<4)
				{	
					k=i;
					i++;
				}
			if(k==3) 
					{	cout<<"O won\n";
						goto l1;
					}	
		}
			
		else if(tt[0][3]=='X')	
		{	k=-1;
			i=1;
			while((tt[i][3-i]== 'X') || (tt[i][3-i]=='T') && i<4)
				{	
					k=i;
					i++;
				}
			if(k==3) 
					{	cout<<"X won\n";
						goto l1;
					}	
		}
		
		else if(tt[0][3]=='T')
		{	k=-1;
			ch=tt[1][2];
			i=2;
			while((tt[i][3-i]== ch) && i<4)
				{	
					k=i;
					i++;
				}
			
			if(k==3) 
					{	cout<<ch<<" won\n";
						goto l1;
					}	
		}
		
		for(int j=0;j<4;j++)
			{	if(tt[j][0]=='O')
				{	i=1;
					k=-1;
					while(((tt[j][i]== 'O') || (tt[j][i]=='T')) && i<4)
						{	
							k=i;
						i++;
						}
					if(k==3) 
					{	cout<<"O won\n";
						goto l1;
					}	
		
				}
			}
			for(int j=0;j<4;j++)
			{	
				if(tt[j][0]=='X')
				{	i=1;
					k=-1;
					while(((tt[j][i]== 'X') || (tt[j][i]=='T')) && i<4)
						{	
							k=i;
						i++;
						}
					if(k==3) 
					{	cout<<"X won\n";
						goto l1;
					}	
				}	
			}
			for(int j=0;j<4;j++)
			{	
				if(tt[j][0]=='T')
				{	i=2;
					k=-1;
					ch=tt[j][1];
					while((tt[j][i]== ch) && i<4)
						{	
							k=i;
						i++;
						}
					if(k==3) 
					{	cout<<ch<<" won\n";
						goto l1;
					}	
				}	
			}
		for(int j=0;j<4;j++)
			{	if(tt[0][j]=='O')
				{	i=1;
					k=-1;
					while((tt[i][j]== 'O') || (tt[i][j]=='T') && i<4)
						{	
							k=i;
						i++;
						}
					if(k==3) 
					{	cout<<"O won\n";
						goto l1;
					}	
		
				}
			}
			for(int j=0;j<4;j++)
			{	if(tt[0][j]=='X')
				{	i=1;
					k=-1;
					while((tt[i][j]== 'X') || (tt[i][j]=='T') && i<4)
						{	
							k=i;
						i++;
						}
					if(k==3) 
					{	cout<<"X won\n";
						goto l1;
					}	
		
				}
			}	
			for(int j=0;j<4;j++)
			{	if(tt[0][j]=='T')
				{	i=2;
					ch=tt[1][j];
					k=-1;
					while((tt[i][j]== ch) && i<4)
						{	
							k=i;
						i++;
						}
					if(k==3 && ch!='.') 
					{	cout<<ch<<" won\n";
						goto l1;
					}	
		
				}
			}
			
			for(int ia=0;ia<4;ia++)
			{	for(int j=0;j<4;j++)
				{	if (tt[ia][j]=='.')
					{	cout<<"Game has not completed\n";
						goto l1;
					}		
				}
			}	
			cout<<"Draw\n";
		l1:t--;
		
	}	
		 
		
return 0;
}
