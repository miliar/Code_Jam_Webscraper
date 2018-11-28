# include <iostream>
# include <string>

using namespace std;

int main()
{
	int i,j,k,l,m,no[100][10],t,c1,c2,c3,c4;
	for(i = 0;i < 100; i++)
	{
		for(j=0;j<10;j++)
		{
			no[i][j] = 0;
		}
	}
	char s[2000];
	cin>>t;
	for(m=0;m<t;m++)
	{
	cin>>s;
	l = strlen(s);
		for(j=0;j<l;j++)
		{
			if(s[j]=='Z')
			{
				no[m][0]++;
				s[j]='y';
				c1 = 0;
				c2 = 0;
				c3 = 0;
				c4 = 0;
				for(k=0;k<l;k++)
				{
					if(s[k]=='E'&&c1==0)
					{
						s[k] = 'y';
						c1++;
					}
					if(s[k]=='R'&&c2==0)
					{
						s[k] = 'y';
						c2++;
					}
					if(s[k]=='O'&&c3==0)
					{
						s[k] = 'y';
						c3++;
					}	

				}

				
				
			}
		}
		for(j=0;j<l;j++){
			if(s[j]=='G')
			{
				no[m][8]++;
				s[j]='y';
				c1 = 0;
				c2 = 0;
				c3 = 0;
				c4 = 0;
				for(k=0;k<l;k++)
				{
					if(s[k]=='E'&&c1==0)
					{
						s[k] = 'y';
						c1++;
					}
					if(s[k]=='I'&&c2==0)
					{
						s[k] = 'y';
						c2++;
					}
					if(s[k]=='H'&&c3==0)
					{
						s[k] = 'y';
						c3++;
					}
					if(s[k]=='T'&&c4==0)
					{
						s[k] = 'y';
						c4++;
					}	

				}
				
				
			}
		}
		for(j=0;j<l;j++){
			if(s[j]=='X')
			{
				no[m][6]++;
				s[j]='y';
				c1 = 0;
				c2 = 0;
				c3 = 0;
				c4 = 0;
				for(k=0;k<l;k++)
				{
					if(s[k]=='S'&&c1==0)
					{
						s[k] = 'y';
						c1++;
					}
					if(s[k]=='I'&&c2==0)
					{
						s[k] = 'y';
						c2++;
					}
					if(s[k]=='0'&&c3==0)
					{
						s[k] = 'y';
						c3++;
					}	

				}
				
				
			}
		}
		for(j=0;j<l;j++){
			if(s[j]=='W')
			{
				no[m][2]++;
				s[j]='y';
				c1 = 0;
				c2 = 0;
				c3 = 0;
				c4 = 0;
				for(k=0;k<l;k++)
				{
					if(s[k]=='T'&&c1==0)
					{
						s[k] = 'y';
						c1++;
					}
					if(s[k]=='O'&&c2==0)
					{
						s[k] = 'y';
						c2++;
					}
					if(s[k]=='o'&&c3==0)
					{
						s[k] = 'y';
						c3++;
					}	

				}
				
				
			}
		}
		for(j=0;j<l;j++){
			if(s[j]=='H')
			{
				no[m][3]++;
				s[j]='y';
				c1 = 0;
				c2 = 0;
				c3 = 0;
				c4 = 0;
				for(k=0;k<l;k++)
				{
					if(s[k]=='T'&&c1==0)
					{
						s[k] = 'y';
						c1++;
					}
					if(s[k]=='R'&&c2==0)
					{
						s[k] = 'y';
						c2++;
					}
					if(s[k]=='E'&&c3==0)
					{
						s[k] = 'y';
						c3++;
					}	
					if(s[k]=='E'&&c4==0)
					{
						s[k] = 'y';
						c4++;
					}	
				}
				
				
			}
		}
		for(j=0;j<l;j++){
			if(s[j]=='R')
			{
				no[m][4]++;
				s[j]='y';
				c1 = 0;
				c2 = 0;
				c3 = 0;
				c4 = 0;
				for(k=0;k<l;k++)
				{
					if(s[k]=='F'&&c1==0)
					{
						s[k] = 'y';
						c1++;
					}
					if(s[k]=='O'&&c2==0)
					{
						s[k] = 'y';
						c2++;
					}
					if(s[k]=='U'&&c3==0)
					{
						s[k] = 'y';
						c3++;
					}	

				}
				
				
			}
		}
		for(j=0;j<l;j++){
			if(s[j]=='F')
			{
				no[m][5]++;
				s[j]='y';
				c1 = 0;
				c2 = 0;
				c3 = 0;
				c4 = 0;
				for(k=0;k<l;k++)
				{
					if(s[k]=='I'&&c1==0)
					{
						s[k] = 'y';
						c1++;
					}
					if(s[k]=='V'&&c2==0)
					{
						s[k] = 'y';
						c2++;
					}
					if(s[k]=='E'&&c3==0)
					{
						s[k] = 'y';
						c3++;
					}	

				}
				
				
			}
		}
		for(j=0;j<l;j++){
			if(s[j]=='O')
			{
				no[m][1]++;
				s[j]='y';
				c1 = 0;
				c2 = 0;
				c3 = 0;
				c4 = 0;
				for(k=0;k<l;k++)
				{
					if(s[k]=='N'&&c1==0)
					{
						s[k] = 'y';
						c1++;
					}
					if(s[k]=='E'&&c2==0)
					{
						s[k] = 'y';
						c2++;
					}
					if(s[k]=='o'&&c3==0)
					{
						s[k] = 'y';
						c3++;
					}	

				}
				
				
			}
		}
		for(j=0;j<l;j++){
			if(s[j]=='S')
			{
				no[m][7]++;
				s[j]='y';
				c1 = 0;
				c2 = 0;
				c3 = 0;
				c4 = 0;
				for(k=0;k<l;k++)
				{
					if(s[k]=='E'&&c1==0)
					{
						s[k] = 'y';
						c1++;
					}
					if(s[k]=='V'&&c2==0)
					{
						s[k] = 'y';
						c2++;
					}
					if(s[k]=='E'&&c3==0)
					{
						s[k] = 'y';
						c3++;
					}
					if(s[k]=='N'&&c4==0)
					{
						s[k] = 'y';
						c4++;
					}		

				}
				
				
			}
		}
		for(j=0;j<l;j++){
			if(s[j]=='N')
			{
				no[m][9]++;
				s[j]='y';
				c1 = 0;
				c2 = 0;
				c3 = 0;
				c4 = 0;
				for(k=0;k<l;k++)
				{
					if(s[k]=='I'&&c1==0)
					{
						s[k] = 'y';
						c1++;
					}
					if(s[k]=='N'&&c2==0)
					{
						s[k] = 'y';
						c2++;
					}
					if(s[k]=='E'&&c3==0)
					{
						s[k] = 'y';
						c3++;
					}
					if(s[k]=='n'&&c4==0)
					{
						s[k] = 'y';
						c4++;
					}		

				}
				
				
			}
		 }
	
	}
	for(m=0;m<t;m++)
	{
		cout<<"Case #"<<m+1<<": ";
		for(i=0;i<=9;i++)
		{
			for(j=0;j<no[m][i];j++)
				cout<<i;
		}
		cout<<endl;
	}
	return 0;

}