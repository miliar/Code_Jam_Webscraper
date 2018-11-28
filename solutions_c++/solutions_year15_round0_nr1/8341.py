#include "stdio.h"
#include "string.h"
#include "iostream"
#include <fstream>
using namespace std;
int main(int argc, char const *argv[])
{
	int a=0,help=0,count=0;
	//printf("%d",'0');
	cin >> a;
	// a=1;
	int c[a];
	char b[a][1005];
	ofstream myfile;
  	myfile.open ("Standing Ovation.txt");
	// for (int i = 0; i < a; ++i)
	// {
	// 	cin >> c[1];
	// 	gets(b[1]);
	// 	for (int j = 0; j <= c[1]; ++j)
	// 	{
	// 		count+=b[1][j];
	// 		printf("%d %d %d %d\n",count,help,j,b[1][j]);
	// 		// cout << count << " "<< help<< " "<< j<< "\n";
	// 		if (help+count>=j+32)
	// 		{
	// 			help++;
	// 			//cout << "help" << i+48 <<" "<< help <<" "<< b[1][j];
	// 		}

	// 		//printf("hello %c\n",count);
	// 	}
	// 	myfile << "Case #"<< i+1 <<": "<< help <<"\n";
	// 	cout << "Case #"<< i+1 <<": "<< help <<"\n";
	// 	help=0;
	// 	count=0;
	// }
	for (int i = 0; i < a; ++i)
	{
		cin >> c[1];
		gets(b[1]);
		for (int j = 0; j <= c[1]; ++j)
		{
			count+=b[1][j+1]-48;
			//printf("%d %d %d %d\n",count,help,j,b[1][j+1]-48);
			if (help+count<=j)
			{
				help++;
				//cout << "help" << i+48 <<" "<< help <<" "<< b[1][j];
			}

			//printf("hello %c\n",count);
		}
		myfile << "Case #"<< i+1 <<": "<< help <<"\n";
		//cout << "Case #"<< i+1 <<": "<< help <<"\n";
		help=0;
		count=0;
	}
	myfile.close();
	return 0;
}
