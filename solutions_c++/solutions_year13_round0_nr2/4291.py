#include<iostream>
//#include<conio.h>
using namespace std;

int func(int, int, int ), col, row;
int arr[100][100];
int main()
{
int i,j, result;

int input;
cin>>input;
int input1 = input;
while(input--){
result = 1;
cin>>row>>col;
if(row==0 || col ==0)
return 0;
for(i=0;i<row;i++)
	for(j=0;j<col;j++)
		cin>>arr[i][j];
for(i=0;i<row && result;i++)
	for(j=0;j<col && result;j++)
		{
			result=0;
			result = func(arr[i][j], i, j);
		}
if(result)
	cout<<"Case #"<<input1-input<<": YES\n";
else 
	cout<<"Case #"<<input1-input<<": NO\n";

}
return 0;
}

int func(int ele, int rowval, int colval)
{
	int i,j, rowfalse=0, colfalse=0;
	for(i=0;i<row;i++)
		{
			if(arr[i][colval]>ele)
				{
				colfalse = 1;
					break;
				}
		}
	for(j=0;j<col;j++)
	{
		if(arr[rowval][j]>ele)
			{
				rowfalse = 1;
				break;
			}
	}
	
	if(colfalse && rowfalse)
		return 0;
	else return 1;
	
}
