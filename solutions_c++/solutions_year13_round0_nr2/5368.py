#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<stdlib.h>
int split(char A[],int B[],char ch=' ')
{
for(int i=0;A[i]!='\0';i++);
int n=0,num=0;
for(int j=0;j<i;j++)
	if(A[j]==ch)
		{int o=1;
		B[num]=0;
			for(int p=j-1;p>=n;p--) {
				B[num]=B[num]+((A[p]-48)*o);
				o*=10;


						}
			num++;
		n=j+1;
		 }
	 else if(A[j+1]=='\0')
		{
		int o=1;
		B[num]=0;
			for(int p=j;p>=n;p--){
				B[num]=B[num]+((A[p]-48)*o);
				o*=10;
				}


		num++;
		n=j+1;
		}
return num;
}
int maximum(int A[],int b)
{
int max=A[0];
for(int i=0;i<b;i++)
	if(A[i]>max)
		max=A[i];
return max;
}

void main()
{
char ans;
ifstream infile("A0.txt");
ofstream outfile("gcians.txt");
char A[100];
infile.getline(A,100);
int T=atoi(A);
for(int i=1;i<=T;i++)
	{
	int  B[2];
	infile.getline(A,100);
	split(A,B);
	int l=B[0];
	int b=B[0];
	int lb[100][100];
	for(int j=0;j<l;j++)
		{
		infile.getline(A,10000);
		split(A,lb[j]);
		}
	int except[100]; int len=0;
	for(int p=0;p<l;p++)
		{
		len=0;
		int max=maximum(lb[p],b);
		for(int q=0;q<b;q++)
			{
			if(lb[p][q]!=max)
				{except[len]=q;
				 len++;}
			}

		for(int e=0;e<len;e++)
			 {
			 int temp[100];

			 for (int u=0;u<l;u++)
				{
				int r=except[e];
				temp[u]=lb[u][r];
				 }
			 int max=maximum(temp,l);
				for(int t=0;t<l;t++)
					if(temp[t]!=max)
						ans='n';
			 }
		  }
	outfile<<"Case #"<<i<<": ";
	if(ans=='n')
		outfile<<"NO"<<endl;
	else
		outfile<<"YES"<<endl;



	}


}
