#include<iostream>

using namespace std;

int main()
{
	int T,i,j;
	
	char a[4][4],winner;
	bool isdot,opdone;
	
	
	cin >> T;
	
	for(int r=1;r<T+1;r++)
	{
		isdot = false;
		opdone=false;
		
		//accept input
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				cin >> a[i][j];
				 if(a[i][j] == '.')
					isdot = true;
					
			}
				
			
	//Winning rowwise
	for(i=0;i<4;i++)
	{
		winner = '\0';
		
		for( j=0;j<4;j++)
			 {
				 if(a[i][j]=='.')
					break;
				 if(a[i][j] == 'T')
					continue;
				 if(winner =='\0')
					winner = a[i][j];
				if(a[i][j] != winner)
					break;
					
			 }
		
		if(j==4)
		{
			cout << "Case #"<<r<<": "<<winner<<" won"<<endl;
			opdone =true;
			break;
		}
	}


//Winning colwise
	for(j=0;j<4 && opdone ==false;j++)
	{
		winner = '\0';
		
		for( i=0;i<4;i++)
			 {
				 if(a[i][j]=='.')
					break;
				 if(a[i][j] == 'T')
					continue;
				 if(winner =='\0')
					winner = a[i][j];
				if(a[i][j] != winner)
					break;
					
			 }
		
		if(i==4)
		{
			cout << "Case #"<<r<<": "<<winner<<" won"<<endl;
			opdone =true;
			break;
		}
	}



//Winning diagonalwise
if(opdone ==false)
{
	winner = '\0';
	for(i=0;i<4 ;i++)
	{
		if(a[i][i] =='.')
			break;
		if(a[i][i] =='T')
			continue;
		if(winner=='\0')
			winner = a[i][i];
		if(a[i][i]!=winner)
			break;
	}

	if(i==4)
	{
			cout << "Case #"<<r<<": "<<winner<<" won"<<endl;
			opdone =true;
		
	}
	else
	{
		winner = '\0';
		for(i=0;i<4 ;i++)
		{
			if(a[i][3-i] =='.')
				break;
			if(a[i][3-i] =='T')
				continue;
			if(winner=='\0')
				winner = a[i][3-i];
			if(a[i][3-i]!=winner)
				break;
		}

		if(i==4)
		{
			cout << "Case #"<<r<<": "<<winner<<" won"<<endl;
			opdone =true;
		
		}
	}
}


if(opdone ==false)
{
if(isdot)
	cout << "Case #"<<r<<": Game has not completed"<<endl;
	else
	cout << "Case #"<<r<<": Draw"<<endl;
}
isdot=false;
opdone=false;

	}

return 0;
}
