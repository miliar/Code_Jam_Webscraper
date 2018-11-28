#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
using namespace std;

int f(int arr[],int N,int cnt);
int J;

FILE *fin,*fout;

int main()
{

	// ifstream fin;
	// ofstream fout;
	// fin.open("C-small-attempt1.in");
	// fout.open("C-small-attempt1.out");

	fin=fopen("C-small-attempt1.in","r");
	fout=fopen("C-small-attempt1.out","w");

    int t;
    // scanf("%d",&t);
    fscanf(fin,"%d",&t);
    for(int i=1;i<=t;i++)
    {
    	int N;
    	// scanf("%d%d",&N,&J);
    	fscanf(fin,"%d%d",&N,&J);
    	int arr[N];
    	for(int i=0;i<N;i++)
    	{
    		if(i==0||i==N-1) arr[i]=1;
    		else arr[i]=0;
    	}
    	fprintf(fout,"Case #%d:\n",i);
    	f(arr,N,1);
    }
}

int f(int arr[],int N,int cnt)
{
	if(J==0) return 0;
	bool chk=false;
	if(cnt==N-1)
	{
		vector<int> v;
		for(long long i=2;i<=10;i++)
		{
			long long sum=0;
			for(int j=N-1;j>=0;j--)
			{
				if(arr[j]==1)
				{
					long long mul=1;
					for(int k=j;k<N-1;k++) mul*=i;
					sum+=mul;
				}
			}

			bool b=false;
			for(int j=2;j<sqrt(sum);j++)
			{
				if((sum%j)==0)
				{
					v.push_back(j);
					b=true;
					break;
				}
			}
			
			if(!b)
			{
				chk=true;
				break;
			}
		}
		if(!chk)
		{
			// for(int i=0;i<N;i++) printf("%d",arr[i]);
			// printf(" ");
			// for(int i=0;i<v.size();i++) printf("%d ",v[i]);
			// printf("\n");
			for(int i=0;i<N;i++) fprintf(fout,"%d",arr[i]);
			fprintf(fout," ");
			for(int i=0;i<v.size();i++) fprintf(fout,"%d ",v[i]);
			fprintf(fout,"\n");
			J--;
		}
		return 0;
	}

	int A[N],B[N];
	for(int i=0;i<N;i++)
	{
		A[i]=arr[i];
		B[i]=arr[i];
	}

	f(A,N,cnt+1);
	B[cnt]=1;
	f(B,N,cnt+1);
}

