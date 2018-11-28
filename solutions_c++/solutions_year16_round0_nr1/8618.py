//============================================================================
// Name        : sheep.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
using namespace std;

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.out", "w", stdout);

	int t;

	cin>>t;
	int nt;

	unsigned long input;
	unsigned long temp;

	int mul = 1;
	int arr[10];
	int done = 0;

	for(nt=0; nt<t; nt++)
	{
		mul = 1;
		cin>>input;

		int arr[10] = {0};
		done = 0;


		if (input == 0)
		{
			cout<<"Case #"<<nt+1<<": "<<"INSOMNIA"<<endl;
			continue;
		}

		while(true)
		{
			temp = input * mul;
			mul++;

			while(temp > 0)
			{
				int rem = temp % 10;
				temp /= 10;
				arr[rem] = 1;

			}

			done = 1;
			for(int i=0; i<10; i++)
			{
				if(arr[i] == 0)
				{
					done = 0;
				}
			}

			if(done == 1)
			{
				cout<<"Case #"<<nt+1<<": "<<input*(mul-1)<<endl;
				break;
			}

		}


	}


	return 0;
}
