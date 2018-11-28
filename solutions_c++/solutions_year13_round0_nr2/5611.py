#include<iostream>
#include<string>
#include<fstream>

using namespace std;
int main()
{
 ifstream in("B-small-attempt2.in");
 ofstream out("output.txt");
 
	int Q,da,db ;
	int f1=0,f2=0;
	in>>Q;
	
	for(int i=1;i<=Q;i++)
	{
	in>>da>>db;
	int D[da][db];
	
	int D2[da][db];
	for(int j=0;j<da;j++)
	 for(int k=0;k<db;k++)
		in>>D[j][k];
	for(int j=0;j<da;j++)
	 for(int k=0;k<db;k++)
		D2[j][k]=2;

	int p1,p2;
	
	for(int j=0;j<da;j++){
		
		for(int k=0;k<db;k++)
				
		if(D[j][k]==1){
			f1=0,f2=0;
			 p1=j;
			 p2=k;
			for(int l1=0;l1<db;l1++)
			
			 if(D[p1][l1]!=1)
			 {f1=1;
			 break;}
			for(int l1=0;l1<da;l1++)
			
			 if(D[l1][p2]!=1)
			 {f2=1;
			 break;} 
			 
			 if(f1==0)
			for(int r=0;r<db;r++)
			
			D2[p1][r]=1;
			if(f2==0)
			for(int r=0;r<da;r++)
			
			D2[r][p2]=1;	
			
		}
		}
		
		int count=0;
	for(int j=0;j<da;j++){
		
		for(int k=0;k<db;k++){

	 		if(D[j][k]!=D2[j][k])
			{count =1;
			break;
			
				}
	   }

	}
 	
	if(count==0)
	out<<"Case #"<<i<<": YES"<<endl;
	else
	out<<"Case #"<<i<<": NO"<<endl;			
	}
}

