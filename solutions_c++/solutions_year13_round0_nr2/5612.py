#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
 ifstream input("B-small-attempt0.in");
 ofstream cc("output.txt");
	int C,d1,d2,g1=0,g2=0;
	input>>C;
	for(int i=1;i<=C;i++)
	{
	input>>d1>>d2;
	int D[d1][d2];
	int A[d1][d2];
	for(int j=0;j<d1;j++)
	 for(int k=0;k<d2;k++)
		input>>D[j][k];
	for(int j=0;j<d1;j++)
	 for(int k=0;k<d2;k++)
		A[j][k]=2;

	int p1,p2;
	
	for(int j=0;j<d1;j++){
		for(int k=0;k<d2;k++)		
		if(D[j][k]==1){
			g1=0,g2=0;
			 p1=j;
			 p2=k;
			for(int l1=0;l1<d2;l1++)
			 if(D[p1][l1]!=1)
			 {g1=1;
			 break;}
			for(int l1=0;l1<d1;l1++)
			 if(D[l1][p2]!=1)
			 {g2=1;
			 break;} 
			 
			 if(g1==0)
			for(int r=0;r<d2;r++)
			A[p1][r]=1;
			if(g2==0)
			for(int r=0;r<d1;r++)
			A[r][p2]=1;	
		}
		}
		int c=0;
	for(int j=0;j<d1;j++){
		for(int m=0;m<d2;m++){
	 		if(D[j][m]!=A[j][m])
				{c=1;
				break;}
	   }

	}
 	
	if(c==0)
	cc<<"Case #"<<i<<": YES"<<endl;
	else
	cc<<"Case #"<<i<<": NO"<<endl;			
	}
}