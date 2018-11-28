#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<iostream>
using namespace std;
int list[10], u;

int check(int temp)	{
	int temp1=1;
	while(temp)	{
		list[temp%10]=1;
		temp = temp/10;
	}
	for(int i=0; i<10; i++)	{
		if(!list[i])	{
			temp1 = 0;
			break;
		}
	}
	return temp1;
}

int calculate(int n)	{
	int temp, flag = 0, i=1;
	while(!flag)	{
		temp = i*n;
		flag = check(temp);
		i++;
	}
	return temp;
}

int main()	{
	int t, n, answer, count, flag;
	cin>>t;
	for(int i=1; i<=t; i++)	{
		cin>>n;
		count=0;
		flag=0;
		for(int j=0; j<10; j++)
			list[j]=0;
		if(!n)
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		else	{
			while(!(n%10))	{
				count++;
				n = n/10;
				flag = 1;
			}
			if(flag){
				if(!(n&1) || n%10==5)	{	
				}
				else	{
					n = n*10;
					count--;
				}
			}
			if(count)
				answer = calculate(n)*pow(10, count);
			else
				answer = calculate(n);
			cout<<"Case #"<<i<<": "<<answer<<endl;	
		}

	}
	return 0;
}