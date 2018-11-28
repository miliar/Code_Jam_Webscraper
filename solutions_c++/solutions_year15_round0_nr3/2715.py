#include<iostream>
#include<string.h>
#include<stdio.h>
#include<string>
using namespace std;

int M[8][8]={{0,1,2,3,4,5,6,7},{1,0,5,6,7,2,3,4},{2,5,1,4,6,0,7,3},{3,6,7,1,2,4,0,5},{4,7,3,5,1,6,2,0},{5,2,0,7,3,1,4,6},{6,3,4,0,5,7,1,2},{7,4,6,2,0,3,5,1}};

void fromfront(int front[],int len, int x, char S[], int Iindex[],int &Icount)
{
	front[0]=(int)S[0]-103;
	if(front[0]==2)
	{
		Iindex[Icount]=0;
		Icount++;
	}
	for(int i=1;i<len*x;i++)
	{
		front[i]=M[front[i-1]][(int)S[i]-103];
		if(front[i]==2)
		{
			Iindex[Icount]=i;
			Icount++;
		}
	}
}

void fromback(int back[],int len, int x,char S[],int Kindex[], int &Kcount)
{
	back[len*x-1]=(int) S[len*x-1]-103;
	if(back[len*x-1]==4)
	{
		Kindex[Kcount]=len*x-1;
		Kcount++;
	}
	for(int i=len*x-2;i>=0;i--)
	{
		back[i]=M[(int)S[i]-103][back[i+1]];
		if(back[i]==4)
		{
			Kindex[Kcount]=i;
			Kcount++;
		}
	}
}

int main()
{
	int T;
	freopen( "input.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	//fromfront(front,2,6,S);
	//fromback(back,2,6,S);
/*	cout<<front[2*6-1]<<" should be 1\n";
	cout<<front[Kindex[0]-1]<<" should be 4\n";
	cout<<back[Iindex[0]+1]<<" should be 2\n"; */
	cin>>T;
	for(int x=0;x<T;x++)
	{
		int front[10001];
		int back[10001];
		char S[10001]="";
		char L[10001]="";
		int X;
		int len;
		cin>>len>>X;
		cin>>L;
		if(len*X<3)
		{
			cout<<"Case #"<<x+1<<": NO"<<endl;
			continue;
		}
		int Iindex[10000];
		int Icount=0;
		int Kindex[10000];
		int Kcount=0;
		for(int i=0;i<X;i++)
		{
			strcat(S,L);
		}
	
		fromfront(front,len,X,S,Iindex,Icount);
		fromback(back,len,X,S,Kindex,Kcount);
		int flag=0;
		if(front[len*X-1]==1)
		{
			int l=0,r=0;
			for(l;l<Icount;l++)
			{
				for(r;r<Kcount;r++)
				{
				//	cout<<Kindex[r]<<" "<<Iindex[l];
					if(Iindex[l]+1>Kindex[r])
					{
						break;
					}
					else if((front[Kindex[r]-1]==4)&&(back[Iindex[l]+1]==2))
					{
						flag=1;
						break;
					}
				}
			}
		}
		else
		{
			cout<<"Case #"<<x+1<<": NO"<<endl;
			continue;
		}
		if(flag)
		{
			cout<<"Case #"<<x+1<<": YES"<<endl;
		}
		else

		{
			cout<<"Case #"<<x+1<<": NO"<<endl;
		}
	} 
}