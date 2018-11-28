#include<iostream.h>
#include<conio.h>
#include<fstream.h>
void main()
{
clrscr();
ifstream ipf;
ofstream opf;

ipf.open("input.in");
opf.open("output.out");

int n=0;
int a1[100],a2[100];
int arr1[100][4][4];
int arr2[100][4][4];

int tmp1[100][4];
int tmp2[100][4];

int ans[100];

int flg[100];
int cnt[100];

int count_tmp1=1,count_tmp2=1;

ipf>>n;

for(int i=1;i<=n;i++)
{
	count_tmp1=1;
	count_tmp2=1;
	
	ipf>>a1[i];
	
	for(int j=1;j<=4;j++)
	{
		for(int k=1;k<=4;k++)	
		{
			ipf>>arr1[i][j][k];
			if(j==a1[i])
			{
				tmp1[i][count_tmp1]=arr1[i][j][k];
				count_tmp1++;
			}

			
		}
		
	}
	
	ipf>>a2[i];

	for(j=1;j<=4;j++)
	{
		for(int k=1;k<=4;k++)	
		{
			ipf>>arr2[i][j][k];
			if(j==a2[i])
			{
				tmp2[i][count_tmp2]=arr2[i][j][k];
				count_tmp2++;
			}
			
		}
		
	}


}

for(i=1;i<=n;i++)
{
	cnt[i]=0;
	flg[i]=0;
	for(int j=1;j<=4;j++)
	{
		for(int k=1;k<=4;k++)
		{
			if(tmp1[i][j]==tmp2[i][k])
			{
				cnt[i]=cnt[i]+1;
				if(cnt[i]>1)
					flg[i]=2;
				else
				{
					flg[i]=1;
					ans[i]=tmp1[i][j];
				}
			}
		
		}	
			
	}
	
	opf<<"\nCase #"<<i<<": ";

	if(flg[i]==0)
		opf<<"Volunteer cheated!";
	if(flg[i]==1)
		opf<<ans[i];
	if(flg[i]==2)
		opf<<"Bad magician!";

	
}

cout<<"finished";
getch();
}