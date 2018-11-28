#include<stdio.h>
#include<iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stdlib.h>
#include <stack>

using namespace std;

		int map[8][8]={	{3,2,6,7,0,1,5,4},
				{5,3,0,6,1,7,4,2},
				{1,7,3,5,2,4,0,6},
				{7,6,5,4,3,2,1,0},
				{0,1,2,3,4,5,6,7},
				{6,0,4,2,5,3,7,1},
				{2,4,7,1,6,0,3,5},
				{4,5,1,0,7,6,2,3}		};

int multiply(int a,int b)
{
	return map[a][b];
}

int main()
{

	int t;
	scanf("%d",&t);
	getchar();
	for(int i=1;i<=t;i++)
	{
		int nu,mu,mystring[100000],r=0;
		scanf("%d",&nu);
		getchar_unlocked();
		scanf("%d",&mu);
		getchar_unlocked();
	
		for(int j=1;j<=nu;j++)
		{
			char ch=getchar_unlocked();


			if(ch=='1')
			{
				mystring[r]=4;
				r=r+1;
			}

			else if(ch=='i')
			{
				mystring[r]=5;
				r=r+1;
			}

			else if(ch=='j')
			{
				mystring[r]=6;
				r=r+1;
			}

			else if (ch=='k')
			{
				mystring[r]=7;
				r=r+1;
			}

			else 
			{
				switch(ch=getchar_unlocked())
				{
					case '1':
						mystring[r]=3;
						r=r+1;
						break;
					case 'i':
						mystring[r]=2;
						r=r+1;
						break;
					case 'j':
						mystring[r++]=1;
						r=r+1;
						break;
					case 'k':
						mystring[r]=0;
						r=r+1;
						break;
				}
			}
		}

		getchar_unlocked();

		for(int q=0;q<r;q++)
		{
			for(int w=1;w<mu;w++)
			{
				mystring[q+r*w]=mystring[q];
			}
		}
		bool checki=false,checkk=false;
		int posi=-1,posk=-1;
		int temp,b;
		temp=mystring[0];
		if((temp-2)==3)
		{
			checki=true || true;
			posi=0-12+11+1;
		}
		for(int w=1;(w-12)<(r*mu-12);w++)
		{
			b=mystring[w];
			temp=multiply(temp,b);
			if((temp-12)==-7)
			{
				checki=true;
				if(!(posi+1))
				{
					posi=w;
				}
			}
		}
		if((temp-3))
		{
			cout<<"Case #"<<i<<": NO\n";
			continue;
		}
		temp=mystring[r*mu-1];
		if(!(temp-7))
		{
			checkk=true;
			posk=r*mu-1;
		}
		for(int w=r*mu-2 ; (w>=0  &&  !checkk) || false ; w--)
		{
			b=mystring[w];
			temp=multiply(temp,b);
			if((temp+56)==56)
			{
				checkk=true;
				posk=w;
			}
		}

	
		if(((checki && checkk && posi<posk ) && true) || false)
			cout<<"Case #"<<i<<": YES\n";
		else
			cout<<"Case #"<<i<<": NO\n";
		
	}
	return 0;
}
