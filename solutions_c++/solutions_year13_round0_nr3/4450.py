#include<iostream>
#include<cmath>
#include<stdio.h>
#include<string.h>
using namespace std;

bool isPalindrome(char *s)
{
	int len = strlen(s);
	for(int i = 0; i < len/2; i++)
	{
		if(s[i]!=s[len-i-1])
		{
			return false;
		}
	}
	return true;
}

int main()
{
	FILE *input, *output;
	if((input = fopen("test","r"))==NULL)
	{
		printf("File input error\n");
		exit(0);
	}
	output = fopen("output","w");
	int caseNum = 1;
	int T;
	char A[100],B[100];
	fscanf(input,"%d",&T);
	while(T--)
	{
		fscanf(input,"%s %s",&A,&B);
		int a = atoi(A);
		int b = atoi(B);
		int count = 0;
		for(int i = a;i<=b;i++)
		{
			int si = sqrt((double)i);
			char stri[101];
			char strsi[101];
			itoa(i,stri,10);
			itoa(si,strsi,10);
			if(i == si*si && isPalindrome(stri) && isPalindrome(strsi))
			{
				count++;
			}
		}
		//output
		fprintf(output,"Case #%d: %d\n",caseNum++,count);
	}
	fclose(output);
	system("pause");
	return 0;
}