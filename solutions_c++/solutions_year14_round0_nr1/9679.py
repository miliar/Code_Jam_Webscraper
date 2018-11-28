#include<iostream>
#include<fstream>
using namespace std;
void main ()
{/*ifstream inn;  ifstream fin("B-large.in");
ofstream onn;*/
ifstream inn("A-small-attempt2.in");
ofstream onn("e.txt");
int con;
inn>>con;
int arr1[5][5],x;
int num1,num2;
int f=0;
	for(int k=1;k<=con;k++)
{	inn>>num1;    
for(int i=1;i<=4;i++)
		 for(int j=1;j<=4;j++)
			 inn>>arr1[i][j];
	 
	 int arr2[4][4];
     inn>>num2;
	 for(int s=1;s<5;s++)
		 for(int a=1;a<5;a++)
			 inn>>arr2[s][a];
	
	for(int q=1;q<=4;q++)
		for(int w=1;w<=4;w++)
			if(arr1[num1][w]==arr2[num2][q])
				{f++;
	x=arr1[num1][w];}
	switch(f)
		{case (0):onn<<"Case #"<<k<<": Volunteer cheated!"<<endl;
	             break;
		case (1):onn<<"Case #"<<k<<": "<<x<<endl;
			break;
		default:onn<<"Case #"<<k<<": Bad magician!"<<endl;
	}
	f=0;}
					system("pause");
}