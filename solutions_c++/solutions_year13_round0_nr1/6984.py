# include<iostream>
# include<conio.h>
# include<stdio.h>
using namespace std;
void main()
{
		int t,c=1,i,j ;
	char in[17], temp[4][5], w ;
	cin>>t;
	
	while(t--)
	{
		for(i=0;i<4;i++)
		{
			cin>>temp[i];
			
		}
		strcpy(in,temp[0]) ;
		for(i=1;i<4;i++)
		{
			strcat(in,temp[i]) ;
		}
		
		if((in[0] != '.' && in[5] != '.' && in[10] != '.' && in[15] != '.') &&
		   ((in[0] == 'T' && (in[5] == in[10]) && (in[10] == in[15])) ||
		   (in[5] == 'T' && (in[0] == in[10]) && (in[10] == in[15])) ||
		   (in[10] == 'T' && (in[0] == in[5]) && (in[5] == in[15])) ||
		   (in[15] == 'T' && (in[0] == in[5]) && (in[5] == in[10])) ||
		   ((in[0] == in[5]) && (in[5] == in[10]) && (in[10] == in[15]))))
		{
			if(in[0] != 'T')
							
			cout<<"Case #"<<c++<<": "<<in[0]<<" won"<<endl;	
			else if(in[5] != 'T')
				
			 cout<<"Case #"<<c++<<": "<<in[5]<<" won"<<endl;
				
			else if(in[10] != 'T')
				
			
			cout<<"Case #"<<c++<<": "<<in[10]<<" won"<<endl;
			else if(in[15] != 'T')
				cout<<"Case #"<<c++<<": "<<in[15]<<" won"<<endl;
				
			continue;
		}
		
		if((in[3] != '.' && in[6] != '.' && in[9] != '.' && in[12] != '.') &&
		   ((in[3] == 'T' && (in[6] == in[9]) && (in[9] == in[12])) ||
		   (in[6] == 'T' && (in[3] == in[9]) && (in[9] == in[12])) ||
		   (in[9] == 'T' && (in[3] == in[6]) && (in[6] == in[12])) ||
		   (in[12] == 'T' && (in[3] == in[6]) && (in[6] == in[9])) ||
		   ((in[3] == in[6]) && (in[6] == in[9]) && (in[9] == in[12]))))
		{
			if(in[3] != 'T')
				cout<<"Case #"<<c++<<": "<<in[3]<<" won"<<endl;
				
			else if(in[6] != 'T')
				
			cout<<"Case #"<<c++<<": "<<in[6]<<" won"<<endl;
			else if(in[9] != 'T')
				
			cout<<"Case #"<<c++<<": "<<in[9]<<" won"<<endl;
			else if(in[12] != 'T')
				
			cout<<"Case #"<<c++<<": "<<in[12]<<" won"<<endl;
			continue;
		}
		
		for(i=0;i<4;i++)
		{
			if((in[4*i] != '.' && in[4*i+1] != '.' && in[4*i+2] != '.' && in[4*i+3] != '.') &&
			   ((in[4*i] == 'T' && (in[4*i+1] == in[4*i+2]) && (in[4*i+2] == in[4*i+3])) ||
			   (in[4*i+1] == 'T' && (in[4*i] == in[4*i+2]) && (in[4*i+2] == in[4*i+3])) ||
			   (in[4*i+2] == 'T' && (in[4*i] == in[4*i+1]) && (in[4*i+1] == in[4*i+3])) ||
			   (in[4*i+3] == 'T' && (in[4*i] == in[4*i+1]) && (in[4*i+1] == in[4*i+2])) ||
			   ((in[4*i] == in[4*i+1]) && (in[4*i+1] == in[4*i+2]) && (in[4*i+2] == in[4*i+3]))))
			{
				if(in[4*i] != 'T')
					
				cout<<"Case #"<<c++<<": "<<in[4*i]<<" won"<<endl;
				else if(in[4*i+1] != 'T')
					cout<<"Case #"<<c++<<": "<<in[4*i+1]<<" won"<<endl;
					
				else if(in[4*i+2] != 'T')
					cout<<"Case #"<<c++<<": "<<in[4*i+2]<<" won"<<endl;
					
				else if(in[4*i+3] != 'T')
					cout<<"Case #"<<c++<<": "<<in[4*i+3]<<" won"<<endl;
					
				break ;
			}
			
			if((in[i] != '.' && in[i+4] != '.' && in[i+8] != '.' && in[i+12] != '.') && 
			   ((in[i] == 'T' && (in[4+i] == in[8+i]) && (in[i+8] == in[i+12])) ||
			   (in[i+4] == 'T' && (in[i] == in[i+8]) && (in[i+8] == in[i+12])) ||
			   (in[i+8] == 'T' && (in[i] == in[i+4]) && (in[i+4] == in[i+12])) ||
			   (in[i+12] == 'T' && (in[i] == in[i+4]) && (in[i+4] == in[i+8])) ||
			   ((in[i] == in[i+4] ) && (in[i+4] == in[i+8]) && in[i+8] == in[i+12])))
			{
				if(in[i] != 'T')
					cout<<"Case #"<<c++<<": "<<in[i]<<" won"<<endl;
					
				else if(in[i+4] != 'T')
					cout<<"Case #"<<c++<<": "<<in[i+4]<<" won"<<endl;
					
				else if(in[i+8] != 'T')
					cout<<"Case #"<<c++<<": "<<in[i+8]<<" won"<<endl;
					
				else if(in[i+12] != 'T')
					cout<<"Case #"<<c++<<": "<<in[i+12]<<" won"<<endl;
					
				break ;
			}
		}
		
		for(j=0;j<16;j++)
		{
			if(in[j] == '.')
				break ;
		}
		if(j==16 && i==4)
		{
			cout<<"Case #"<<c++<<": Draw"<<endl;
			
			continue ;
		}
		
		if(i==4)
		{
			cout<<"Case #"<<c++<<": Game has not completed"<<endl;
			continue;
		}
	}
	
}