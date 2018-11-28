#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<fstream>
using namespace std;

	
int main()
{
	int mat1[4][4],mat2[4][4],m1[4],m2[4];
	int i,j,cur=0,x;
	int T,Ans1,Ans2;
	//cin>>Ans;
	
	ifstream fin("A-small-attempt2.in",ios::in);
    ofstream fout("A-small.out",ios::out);
    
    
	fin>>T;
	
	int c[T],fnd[T];
	for(i=0;i<T;i++)
	c[i]=0;
	
	while(cur<T)
	{
	fin>>Ans1;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			fin>>mat1[i][j];
		}
	}
	fin>>Ans2;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			fin>>mat2[i][j];
		}
	}
	
	for(j=0;j<4;j++)
	m1[j]=mat1[Ans1-1][j];	
	
	for(j=0;j<4;j++)
	m2[j]=mat2[Ans2-1][j];	
	
	for(i=0;i<4;i++)
	{
	x=m1[i];
	for(j=0;j<4;j++)
	{
	if(x==m2[j])
	{
	fnd[cur]=x;
	c[cur]++;
	break;
	}
	}
	}
	cur++;
	}
	for(i=0;i<T;i++)
	{
		//	cout<<"\n"<<c[i];
		fout<<"\nCase #"<<i+1<<":";
		if(c[i]==1)
		fout<<" "<<fnd[i];
		else if(c[i]>1)
		fout<<" Bad Magician!";
		else
		fout<<" Volunteer Cheated!";
	}
	
		
getch();
return 0;
}
