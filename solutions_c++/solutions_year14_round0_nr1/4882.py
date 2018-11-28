#include<iostream>
#include<fstream.h>
using namespace std;
int main()
{
int t,cnt,index;
	ifstream fin;
	fin.open("asmallattem.txt");
	ofstream fout;
	fout.open("outattempt.txt");
	fin>>t;
	int arr[4],row1,row2;
	int *res = new int[t];
	int *res1 = new int[t];
	for(int i =0;i<t;i++)
	{
		cnt=0;
		fin>>row1;
		for(int l=0;l<row1;l++)for(int k=0;k<4;k++)fin>>arr[k];	
		for(int l=row1;l<4;l++)for(int k=0;k<4;k++)fin>>row2;	
		fin>>row2;
		for(int l=0;l<row2-1;l++)for(int k=0;k<4;k++)fin>>row1;
		for(int k =0 ;k<4;k++)
		{
			fin>>row1;
			for(int j=0;j<4;j++)
			{
				if(row1==arr[j]){cnt++;res1[i]=arr[j];}
			}
		}
		for(int l=row2;l<4;l++)for(int k=0;k<4;k++)fin>>row1;
		res[i]=cnt;
		
	}
	for(int i=0;i<t;i++)
	{
		cnt = res[i];
		if(cnt==1)fout<<"Case #"<<i+1<<": "<<res1[i]<<"\n";
		else if(cnt==0)fout<<"Case #"<<i+1<<": Volunteer cheated!\n";
		else fout<<"Case #"<<i+1<<": Bad magician!\n";
	}
	//system("pause");
	return 0;
}