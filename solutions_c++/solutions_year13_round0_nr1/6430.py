#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	char arr[4][4];
	ifstream infile("A-large.in");
	ofstream outfile("output.txt");

	string s[4] = {"X won","O won","Draw","Game has not completed"};

	int t;
	infile >> t;

	for(int l=0; l<t; l++)
	{
		string result="";
		for(int i=0; i<4; i++)	//filling array
		{
			for(int j=0; j<4; j++)
			{
				infile >> arr[i][j];
			}
		}

		bool dot, x, o;
		bool globalDot=false;

		for(int i=0; i<4; i++)
		{
			//row checking
			dot=false;	x=true;	o=true;
			for(int j=0; j<4; j++)
			{
				if(arr[i][j]=='.')
				{
					dot=true;
					globalDot=true;
					break;
				}
				else if( arr[i][j]=='X')
					o=false;
				else if( arr[i][j]=='O')
					x=false;
			}

			if(dot!=true && x==true)
			{
				result=s[0];
				break;
			}
			else if(dot!=true && o==true)
			{
				result=s[1];
				break;
			}

			//column checking
			dot=false;	x=true;	o=true;
			for(int j=0; j<4; j++)
			{
				if(arr[j][i]=='.')
				{
					dot=true;
					globalDot=true;
					break;
				}
				else if( arr[j][i]=='X')
					o=false;
				else if( arr[j][i]=='O')
					x=false;
			}

			if(dot!=true && x==true)
			{
				result=s[0];
				break;
			}
			else if(dot!=true && o==true)
			{
				result=s[1];
				break;
			}

			//diagonal checking
			dot=false;	x=true;	o=true;
			for(int j=0; j<4; j++)
			{
				if(arr[j][j]=='.')
				{
					dot=true;
					globalDot=true;
					break;
				}
				else if( arr[j][j]=='X')
					o=false;
				else if( arr[j][j]=='O')
					x=false;
			}
			if(dot!=true && x==true)
			{
				result=s[0];
				break;
			}
			else if(dot!=true && o==true)
			{
				result=s[1];
				break;
			}

			dot=false;	x=true;	o=true;
			for(int j=0; j<4; j++)
			{
				if(arr[j][3-j]=='.')
				{
					dot=true;
					globalDot=true;
					break;
				}
				else if( arr[j][3-j]=='X')
					o=false;
				else if( arr[j][3-j]=='O')
					x=false;
			}
			if(dot!=true && x==true)
			{
				result=s[0];
				break;
			}
			else if(dot!=true && o==true)
			{
				result=s[1];
				break;
			}
		}
		if(result=="")
		{
			if(globalDot)
				result=s[3];
			else
				result=s[2];
		}
		outfile << "Case #" << l+1 << ": " << result << endl;
	}

	infile.close();
	outfile.close();
	return 0;
}