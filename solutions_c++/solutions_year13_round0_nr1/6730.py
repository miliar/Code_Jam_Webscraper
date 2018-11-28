#include<iostream>
#include<math.h>
#include<fstream>
#include<conio.h>
using namespace std;
int main()
{
	ifstream fin("A-large.in");
	ofstream fout("f1.txt");
	int no;
	fin>>no;
	char arr[4][4];
	for(int s=1;s<=no;s++)
	{		
		
		for(int j=0;j<4;j++)	
		{
			for(int k=0;k<4;k++)
			{
				fin>>arr[j][k];
		//	cout<<arr[j][k]<<" ";
			}
	//	cout<<endl<<endl;;
		}
		bool x=false,o=false,d=false,i=false;
		for(int l=0;l<4;l++)
		{//left to right
		if((arr[l][0]=='X'||arr[l][0]=='T')&&(arr[l][1]=='X'||arr[l][1]=='T')&&(arr[l][2]=='X'||arr[l][2]=='T')&&(arr[l][3]=='X'||arr[l][3]=='T'))		
					x=true;
		}
	//	cout<<x;
	//	getch();
		
		for(int l=0;l<4;l++)
		{//up to down
		if((arr[0][l]=='X'||arr[0][l]=='T')&&(arr[1][l]=='X'||arr[1][l]=='T')&&(arr[2][l]=='X'||arr[2][l]=='T')&&(arr[3][l]=='X'||arr[3][l]=='T'))	
			x=true;
		}	
		if((arr[0][0]=='X'||arr[0][0]=='T')&&(arr[1][1]=='X'||arr[1][1]=='T')&&(arr[2][2]=='X'||arr[2][2]=='T')&&(arr[3][3]=='X'||arr[3][3]=='T'))	
		x=true;	
		if((arr[0][3]=='X'||arr[0][3]=='T')&&(arr[1][2]=='X'||arr[1][2]=='T')&&(arr[2][1]=='X'||arr[2][1]=='T')&&(arr[3][0]=='X'||arr[3][0]=='T'))	
		x=true;
		
		for(int l=0;l<4;l++)
		{//left to right
		if((arr[l][0]=='O'||arr[l][0]=='T')&&(arr[l][1]=='O'||arr[l][1]=='T')&&(arr[l][2]=='O'||arr[l][2]=='T')&&(arr[l][3]=='O'||arr[l][3]=='T'))		
		o=true;
		}
		for(int l=0;l<4;l++)
		{//up to down
		if((arr[0][l]=='O'||arr[0][l]=='T')&&(arr[1][l]=='O'||arr[1][l]=='T')&&(arr[2][l]=='O'||arr[2][l]=='T')&&(arr[3][l]=='O'||arr[3][l]=='T'))
			o=true;
		}	
		if((arr[0][0]=='O'||arr[0][0]=='T')&&(arr[1][1]=='O'||arr[1][1]=='T')&&(arr[2][2]=='O'||arr[2][2]=='T')&&(arr[3][3]=='O'||arr[3][3]=='T'))
		o=true;	
		if((arr[0][3]=='O'||arr[0][3]=='T')&&(arr[1][2]=='O'||arr[1][2]=='T')&&(arr[2][1]=='O'||arr[2][1]=='T')&&(arr[3][0]=='O'||arr[3][0]=='T'))
		o=true;
		for(int j=0;j<4;j++)	
			for(int k=0;k<4;k++)
			{
			if(arr[j][k]=='.')
			i=true;	
			}
	if((!i)&&(!x)&&(!o))
	d=true;
	
	
	if(x)
	fout<<"Case #"<<s<<": "<<"X won"<<endl;
	else if(o)
	fout<<"Case #"<<s<<": "<<"O won"<<endl;
	else if(d)
	fout<<"Case #"<<s<<": "<<"Draw"<<endl;
	else
	fout<<"Case #"<<s<<": "<<"Game has not completed"<<endl;
	
	}



}
