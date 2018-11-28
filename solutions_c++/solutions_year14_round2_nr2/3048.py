#include<stdio.h>
#include<stdlib.h>
#include<string.h>
//#include <stdio.h>
#include <conio.h>
#include <iostream>
#include <vector>
using namespace std;


int main()
{
	unsigned short int testcases;
	cin >> testcases;
	int A, B, K;
	for(int t=0 ; t<testcases; t++)
	{
		cin >> A >> B >> K;
		int count = 0;
	
		for(int i=0; i < A; i++)
		{
			for(int j=0; j < B; j++)
			{
				if((i&j) < K)
					count++;
			}
		}
		cout << "Case #"<<t+1<<": "<<count<<"\n";
	}
   
}