#include<iostream>
#include<string.h>
#include<math.h>
#include<stdio.h>
#include<malloc.h>

using namespace std;


int is_palindrome(char *c)
{
	int len,i;
	if(strlen(c)%2 == 0)
	{
		len = strlen(c);
		for(i=0;i<len/2;i++)
		{
			if(c[i] != c[len-1-i])
				return 0;
		}

	}
	return 1;

}


int is_fair(int a)
{
	char str[500];
	sprintf(str,"%d",a);
	if(is_palindrome(&str[0]))
		return 1;
	return 0;
}

int is_square(int a)
{
	char str[500];
	int d = (int)sqrt(a);
	if(d*d == a)
	{
		sprintf(str, "%d",d);
		if(is_palindrome(str))
			return 1;
	}
	return 0;
}


int is_fair_and_square(int a)
{
	if(is_fair(a) && is_square(a))
		return 1;
	return 0;
}



int main()
{
	int t,i,a,b,ct=0,j;
	cin >> t;

	char *s[500],temp[100];
	char *temp1 = (char*)malloc(100*sizeof(char));
	for(i=0;i<t;i++)
	{
		ct=0;
		cin >> a >> b;
		sprintf(temp,"%d",i+1);
		s[i] = (char*)malloc(100*sizeof(char));
		strcat(s[i],"Case #");
		strcat(s[i],temp);
		strcat(s[i],": ");
		
		for(j=a;j<=b;j++)
		{
			if(is_fair_and_square(j))
			{
				//cout<< j <<"is fair and squae";
				ct++;
			}

		}
		sprintf(temp1,"%d",ct);
		strcat(s[i],temp1);
		
		
		
		
	}
	for(i=0;i<t;i++)
	cout << s[i]<<endl;
}