#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int test,a[16][16],b[4],i,j,row1,row2,k,card,count=0; 
	ofstream fout;
	ifstream fin; 
	fout.open("output.txt");
	fin.open("A-small-attempt1.in");
	k=1;
	fin>>test;
	while(test--)
	{
		fin>>row1;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				fin>>a[i][j];
		for(i=0;i<4;i++)
			b[i]=a[row1-1][i];
		fin>>row2;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				fin>>a[i][j];
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[row2-1][i]==b[j])
				{count++;
				card=b[j];
				}
			}
		}
		if(count>1)
			fout<<"Case"<<" "<<"#"<<k<<":"<<" "<<"Bad magician!"<<"\n";
		else if(count==1)
			fout<<"Case"<<" "<<"#"<<k<<":"<<" "<<card<<"\n";
		else if(count==0)
			fout<<"Case"<<" "<<"#"<<k<<":"<<" "<<"Volunteer cheated!"<<"\n";
	count=0;
	k++;
	}
return 0;
}

		