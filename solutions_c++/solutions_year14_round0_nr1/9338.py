#include<iostream>
#include<stdio.h>
using namespace std;
int main(int argc, char const *argv[])
{
	int n,cases;
	cin>>cases;
	int lisa[4];
	int lisb[4];
	int a,b;
	for (int i = 0; i < cases; ++i)
	{
		cin>>a;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				if(j!=a-1)cin>>n;
				else cin>>lisa[k];
			}
		}
		cin>>b;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				if(j!=b-1)cin>>n;
				else cin>>lisb[k];
			}
		}
		int ns=0;
		int sol=-1;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				if(lisa[j]==lisb[k]) ns++;	
			}
		}
		if(ns==1){
			for (int j = 0; j < 4; ++j)
			{
				for (int k = 0; k < 4; ++k)
				{
					if(lisa[j]==lisb[k]) sol=lisa[j];
				}
			}
			printf("Case #%d: %d\n",i+1,sol);
		}
		else if(ns>1){
			printf("Case #%d: Bad magician!\n",i+1);
		}
		else if(ns==0){
			printf("Case #%d: Volunteer cheated!\n",i+1);
		}
	}
	return 0;
}