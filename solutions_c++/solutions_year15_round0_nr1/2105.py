#include<stdio.h>
#include<string>
#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
	int t ;
	scanf("%d",&t);getchar();
	int counter = 1;
	while(t--)
	{
		int size;
		scanf("%d",&size);getchar();
		string input ;
		getline(cin,input);
		int current = input[0] - '0';
		int result = 0 ;
		for(int i = 1 ; i <= size ; i++ )
		{
			if(current >= i)
			{
				current += input[i] - '0'; 
			}
			else
			{
				int temp = i - current ;
				current += temp + input[i] - '0';
				result += temp ; 
			}
		}
		printf("Case #%d: %d\n",counter++,result);
	}
}
