// ConsoleApplication2.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
#pragma warning(disable: 4996) //Disabling use _s function warning.

#include<iostream>

int _tmain(int argc, _TCHAR* argv[])
{

	using namespace std;
	int count;
	freopen("input.txt", "r", stdin);
	freopen( "C:\\Users\\veharshv\\Desktop\\output.txt", "w", stdout );

	cin>>count;
	
	int row, temp;
	
	bool openCard[16] = {};

	for(int c=1;c<=count;c++)
	{
		bool openCard[16] = {};

		//first matrix set
		cin>>row;
		for(int i=1; i<row;i++)
			cin>>temp>>temp>>temp>>temp;

		for(int i=0; i<4;i++)
		{
			cin>>temp;
			openCard[temp-1]=true;
		}

		for(int i=row+1; i<=4;i++)
			cin>>temp>>temp>>temp>>temp;

		//second matrix set
		cin>>row;
		for(int i=1; i<row;i++)
			cin>>temp>>temp>>temp>>temp;

		int valueOfCard = -1;

		for(int i=0; i<4;i++)
		{
			cin>>temp;
			if(openCard[temp-1])	//isopen
			{
				if(valueOfCard ==- 1)
					valueOfCard = temp;
				else
					valueOfCard = -2;	//Bad magician!
			}
		}

		for(int i=row+1; i<=4;i++)
			cin>>temp>>temp>>temp>>temp;

		cout<<"Case #";
		cout<<c;
		cout<<": ";

		if(valueOfCard==-1)
			cout<<"Volunteer cheated!"<<endl;
		else if(valueOfCard==-2)
			cout<<"Bad magician!"<<endl;
		else
			cout<<valueOfCard<<endl;
			

	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}

