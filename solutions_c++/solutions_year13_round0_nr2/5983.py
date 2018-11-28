#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
 ifstream inn("B-small-attempt0.in");
 ofstream cc("raww.txt");
	int T,d1,d2,flag1=0,flag2=0;
	inn>>T;
	for(int i=1;i<=T;i++)
	{
	inn>>d1>>d2;
	int D[d1][d2];
	int D2[d1][d2];
	for(int j=0;j<d1;j++)
	 for(int k=0;k<d2;k++)
		inn>>D[j][k];
	for(int j=0;j<d1;j++)
	 for(int k=0;k<d2;k++)
		D2[j][k]=2;

	int p1,p2;
	
	for(int j=0;j<d1;j++){
		for(int k=0;k<d2;k++)		
		if(D[j][k]==1){
			flag1=0,flag2=0;
			 p1=j;
			 p2=k;
			for(int l1=0;l1<d2;l1++)
			 if(D[p1][l1]!=1)
			 {flag1=1;
			 break;}
			for(int l1=0;l1<d1;l1++)
			 if(D[l1][p2]!=1)
			 {flag2=1;
			 break;} 
			 
			 if(flag1==0)
			for(int r=0;r<d2;r++)
			D2[p1][r]=1;
			if(flag2==0)
			for(int r=0;r<d1;r++)
			D2[r][p2]=1;	
		}
		}
		int c=0;
	for(int j=0;j<d1;j++){
		for(int k=0;k<d2;k++){
	//	 	cout << D2[j][k] << " ";
	 		if(D[j][k]!=D2[j][k])
				{c=1;
				break;}
	   }
//	   cout << endl;
	}
 	
	if(c==0)
	cc<<"Case #"<<i<<": YES"<<endl;
	else
	cc<<"Case #"<<i<<": NO"<<endl;			
	}
}
