#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<iostream>
using namespace std;

int panCakeStack[100];

int calculate2(int noOfPanCakes)	{
	int noOfFlips=0, temp;
	temp=panCakeStack[0];
	for(int i=1; i<noOfPanCakes; i++)	{
		if(temp!=panCakeStack[i])	{
			noOfFlips++;
			temp = panCakeStack[i];
		}
	}
	noOfFlips++;
	if(panCakeStack[noOfPanCakes-1]==1)
		noOfFlips--;
	return noOfFlips;
}

int main()	{
	int t, noOfPanCakes, garb, answer;
	char s;
	cin>>t;
	garb = getchar();
	for(int i=1; i<=t; i++)	{
		for(int k=0; k<100; k++)
			panCakeStack[k]=0;
		noOfPanCakes=0;
		do  {
			s=getchar();
			if(s=='+')
				panCakeStack[noOfPanCakes]=1;
			noOfPanCakes++;
		} while (s!='\n');
		noOfPanCakes--;
		answer = calculate2(noOfPanCakes);
		cout<<"Case #"<<i<<": "<<answer<<endl;	
	}
	return 0;
}