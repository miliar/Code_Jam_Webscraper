#include <iostream>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include <iomanip>
#include <fstream>
#include<bitset>
 using namespace std;
int main()
{
	ifstream inFile;  
	 ofstream outFile;  
	 inFile.open("B-large.in");  
	 outFile.open("outData.out");
	 int T,N,M;
	 bool isover;
	 vector<int> v1;
	 int a[100][100];
	 int h[100],w[100];
	 inFile>>T;
	 for(int icases=1;icases<=T;icases++)
	 {
		 inFile>>N>>M;
		 isover=0;
		 //memset(a,0,10000*4);
		 for(int i=0;i<N;i++)
		 {
			 for(int j=0;j<M;j++)
				 inFile>>a[i][j];
		 }
		
		 for(int i=0;i<N;i++)
		 {
			  int max=-1;
			  for(int j=0;j<M;j++)
			  {
				  if(a[i][j]>max)
				  {
					  max=a[i][j];
				  }
			  }
			 h[i]=max;
		 }
		   for(int i=0;i<M;i++)
		 {
			  int max=-1;
			  for(int j=0;j<N;j++)
			  {
				  if(a[j][i]>max)
				  {
					  max=a[j][i];
				  }
			  }
			 w[i]=max;
		 }
		 for(int i=0;i<N;i++)
		 {
			 for(int j=0;j<M;j++)
			 {
				 if(a[i][j]<w[j]&&a[i][j]<h[i])
				 {
					 outFile<<"Case #"<<icases<<": NO"<<endl;
					 isover=1;
					 break;
				 }
			 }
			 if(isover)break;
		 }
		 if(!isover)outFile<<"Case #"<<icases<<": YES"<<endl;;
	 }
	  inFile.close();  
	  outFile.close();
	 return 0;
}