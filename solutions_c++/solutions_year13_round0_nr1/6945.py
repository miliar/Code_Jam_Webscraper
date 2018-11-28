#include <iostream>;

using namespace std;

int main()
{
	int cases;
	cin>>cases;
	int true_case=cases;
	int val ;
	int counter=cases;
	

	while(cases!=0)
	{
		val =true_case-counter+1;
		char arr[4][4];


		//Taking the input
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
			cin>>arr[i][j];
			}
		}
	
		
		

		for(int i=0;i<4;i++)
		{
			int counter_x=0,counter_y=0;

			for(int j=0;j<4;j++)
			{
				if((arr[i][j]=='x')||(arr[i][j]=='X'))
				{
					counter_x++;
				}
				else if((arr[i][j]=='o')||(arr[i][j]=='O'))
				{
					counter_y++;
				}
				else if((arr[i][j]=='T')||(arr[i][j]=='t'))
				{
					counter_x++;
					counter_y++;
				}
				if(counter_x==4)
				{
					cout<<"Case #"<<val<<": ";
					cout<<"X won"<<endl;
					//flag=1;
					goto found;
					
				}
				if(counter_y==4)
				{
					cout<<"Case #"<<val<<": ";
					cout<<"O won"<<endl;
					//flag=1;
					goto found;
					
				}
			
			}
		}
		
		

		

		

		for(int j=0;j<4;j++)
		{
			int counter_x=0,counter_y=0;

			for(int i=0;i<4;i++)
			{
				if((arr[i][j]=='x')||(arr[i][j]=='X'))
				{
					counter_x++;
				}
				else if((arr[i][j]=='o')||(arr[i][j]=='O'))
				{
					counter_y++;
				}
				else if((arr[i][j]=='T')||(arr[i][j]=='t'))
				{
					counter_x++;
					counter_y++;
				}
				if(counter_x==4)
				{
					cout<<"Case #"<<val<<": ";
					cout<<"X won"<<endl;
					//second_flag=1;
					goto found;
					
				}
				if(counter_y==4)
				{
					cout<<"Case #"<<val<<": ";
					cout<<"O won"<<endl;
					//second_flag=1;
					goto found;
					
				}
			
			}
		}


		int counter_x=0;
		int counter_y=0;

		for(int i=0;i<4;i++)
		{
			
			if((arr[i][i]=='x')||(arr[i][i]=='X'))
			{
				counter_x++;
			}
			else if((arr[i][i]=='o')||(arr[i][i]=='O'))
			{
				counter_y++;
			}
			else if((arr[i][i]=='T')||(arr[i][i]=='t'))
			{
				counter_x++;
				counter_y++;
			}

			if(counter_x==4)
			{	cout<<"Case #"<<val<<": ";
				cout<<"X won"<<endl;
				goto found;
			}
			else if(counter_y==4)
			{	cout<<"Case #"<<val<<": ";
				cout<<"O won"<<endl;
				goto found;
			}
		}

		counter_x=0;
		counter_y=0;

		for(int i=0;i<4;i++)
		{
			

			int j=3-i;
			

			if((arr[i][j]=='x')||(arr[i][j]=='X'))
				{
					counter_x++;

				}
				else if((arr[i][j]=='o')||(arr[i][j]=='O'))
				{
					counter_y++;
				}
				else if((arr[i][j]=='T')||(arr[i][j]=='t'))
				{
					counter_x++;
					counter_y++;
				}
				if(counter_x==4)
				{
					cout<<"Case #"<<val<<": ";
					cout<<"X won"<<endl;
					//second_flag=1;
					goto found;
					
				}
				if(counter_y==4)
				{
					cout<<"Case #"<<val<<": ";
					cout<<"O won"<<endl;
					//second_flag=1;
					goto found;
					
				}
			
		}

			

			int new_flag=0;
			for(int i=0;i<4;i++)
			{
				for(int j=0;j<4;j++)
				{
					if(arr[i][j]=='.')
					{
						
						new_flag =1;
						break;
						
					}
				}
			}

			if(new_flag!=1)
			{	cout<<"Case #"<<val<<": ";
				cout<<"Draw"<<endl;
			}
			else
			{	cout<<"Case #"<<val<<": ";
				cout<<"Game has not completed"<<endl;
			}
		

		
		found:
		cases--;
		counter--;
	}
	
return 0;
}