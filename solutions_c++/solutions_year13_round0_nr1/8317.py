#include<iostream>
using namespace std;
int main() {

char arr[4][4];
int j=0;
int i;
int testcases,T;
cin>>T;
testcases=T;
do{
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
		cin>>arr[i][j];
		}
	}
	T--;


	//check for X horizontaly
	
	//access input
/*for(i=0;i<4;i++)
	{
	for(j=0;j<4;j++)
	{
	cout<<arr[i][j];
	}
	cout<<endl;
	}*/
	
//cases for winning of X
//first case for horizontal

for(i=0;i<4;i++)
{
if((arr[i][0]=='X'||arr[i][0]=='T') && (arr[i][1]=='X'||arr[i][1]=='T') && (arr[i][2]=='X'||arr[i][2]=='T') && (arr[i][3]=='X'||arr[i][3]=='T'))
{
cout<<"Case #"<<(-T+testcases)<<": "<<"X won"<<endl;
goto END;
}
}

//second case for vertical
for(i=0;i<4;i++)
{
if((arr[0][i]=='X'||arr[0][i]=='T') && (arr[1][i]=='X'||arr[1][i]=='T') && (arr[2][i]=='X'||arr[2][i]=='T') && (arr[3][i]=='X'||arr[3][i]=='T'))
{
cout<<"Case #"<<(-T+testcases)<<": "<<"X won"<<endl;
goto END;
}
}

//third case for diagonal
if((arr[0][0]=='X'||arr[0][0]=='T') && (arr[1][1]=='X'||arr[1][1]=='T') && (arr[2][2]=='X'||arr[2][2]=='T') && (arr[3][3]=='X'||arr[3][3]=='T'))
{
cout<<"Case #"<<(-T+testcases)<<": "<<"X won"<<endl;
goto END;
}
else if((arr[0][3]=='X'||arr[0][3]=='T') && (arr[1][2]=='X'||arr[1][2]=='T') && (arr[2][1]=='X'||arr[2][1]=='T') && (arr[3][0]=='X'||arr[3][0]=='T'))
{
cout<<"Case #"<<(-T+testcases)<<": "<<"X won"<<endl;
goto END;
}

//cases for winning of O
//first case for horizontal
for(i=0;i<4;i++)
{
if((arr[i][0]=='O'||arr[i][0]=='T') && (arr[i][1]=='O'||arr[i][1]=='T') && (arr[i][2]=='O'||arr[i][2]=='T') && (arr[i][3]=='O'||arr[i][3]=='T'))
{
cout<<"Case #"<<(-T+testcases)<<": "<<"O won"<<endl;
goto END;
}
}


//second case for vertical
for(i=0;i<4;i++)
{
if((arr[0][i]=='O'||arr[0][i]=='T') && (arr[1][i]=='O'||arr[1][i]=='T') && (arr[2][i]=='O'||arr[2][i]=='T') && (arr[3][i]=='O'||arr[3][i]=='T'))
{
cout<<"Case #"<<(-T+testcases)<<": "<<"O won"<<endl;
goto END;
}
}


//third case for diagonal
if((arr[0][0]=='O'||arr[0][0]=='T') && (arr[1][1]=='O'||arr[1][1]=='T') && (arr[2][2]=='O'||arr[2][2]=='T') && (arr[3][3]=='O'||arr[3][3]=='T'))
{
cout<<"Case #"<<(-T+testcases)<<": "<<"O won"<<endl;
goto END;
}
else if((arr[0][3]=='O'||arr[0][3]=='T') && (arr[1][2]=='O'||arr[1][2]=='T') && (arr[2][1]=='O'||arr[2][1]=='T') && (arr[3][0]=='O'||arr[3][0]=='T'))
{
cout<<"Case #"<<(-T+testcases)<<": "<<"O won"<<endl;
goto END;
}

//still if game is not over
for(i=0;i<4;i++)
{
	for(j=0;j<4;j++)
	{
	if(arr[i][j]=='.')
	{
	cout<<"Case #"<<(-T+testcases)<<": "<<"Game has not completed"<<endl;
	goto END;
	}
	}
}

cout<<"Case #"<<(-T+testcases)<<": "<<"Draw"<<endl;

END:;


//cout<<"Case #"<<(T-testcases)<<": "<<"X won";		
}while(T!=0);


return 0;
}
