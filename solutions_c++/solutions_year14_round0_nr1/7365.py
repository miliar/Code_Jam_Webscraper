#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;
int test;
int arr[200][4][4];
int rows[200];

int calculate(int testcase)
{
	
	int ret = -1;
	int ele = testcase*2;
	for(int i = 0; i < 4; ++i)
	{
		for(int j = 0; j < 4; ++j)
		{
            if(arr[ele][rows[ele]-1][i] == arr[ele+1][rows[ele+1]-1][j])
			{
				if(ret != -1)
				{
					ret = -2; break;
				}
				else
				{
                     ret = arr[ele][rows[ele]-1][i];
				}
			}
		}
	}
   return ret;
}
void main()
{
	ifstream read("C:\\Users\\SwatiSh\\Downloads\\A-small-attempt0.in");

	read >> test;
	for (int i = 0; i < (test*2); ++i)
	{
		read>>rows[i];
		for(int j = 0; j < 4; ++j)
		{
			
				read>>arr[i][j][0]>>arr[i][j][1]>>arr[i][j][2]>>arr[i][j][3];
			
		}
		++i;
		read>>rows[i]; 
		for(int j = 0; j < 4; ++j)
		{
			read>>arr[i][j][0]>>arr[i][j][1]>>arr[i][j][2]>>arr[i][j][3];
		} 
	}
	int result;
	for(int i = 0; i < test; ++i)
	{ 

		result= calculate(i);
		if(result == -2)
		{
			cout<<"Case #"<<(i+1)<<": Bad magician!"<<endl;
		}
		else if(result == -1)
		{
			cout<<"Case #"<<(i+1)<<": Volunteer cheated!"<<endl;
		}
		else 
		{
			cout<<"Case #"<<(i+1)<<": "<<result<<endl;
		}
       
	}

	getch();
}