//2013 GCJ Qualification round Problem B. Lawnmower
#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;


string check(int N, int M, int** a)
{
	int i,j;
	string result="YES";

	int* rowmax=new int[N];
	int* colmax=new int[M];
	vector<int> row(M);
	vector<int> col(N);
	for (i=0;i<N;i++)
		{
			for (j=0;j<M;j++)
			row.at(j)=a[i][j];
			sort(row.begin(),row.end());
			//vector <int>::iterator it=row.end();
			rowmax[i]=row.at(M-1);
	   }
	    
	    for (j=0;j<M;j++)
		{
			for (i=0;i<N;i++)
			col.at(i)=a[i][j];
			sort(col.begin(),col.end());
			//vector <int>::iterator it1=col.end();
			colmax[j]=col.at(N-1);
	    }
    for (i=0;i<N;i++) 
      {
		  for (j=0;j<M;j++)
		  if (a[i][j]<rowmax[i] && a[i][j]<colmax[j])
			 {
				 result="NO";
		   break;
		  }
	 }

	
	delete []rowmax;
	delete []colmax;
	return result;
}
int main()
{   
	
	
	ifstream fin("B-large.in");
	//ifstream fin("B-small-attempt0.in");
	//ifstream fin("B-large.in");
	int T;
	fin>>T;
	//cout<<T;
	ofstream fout("B-large.out");
	//ofstream fout("B-small-attempt0.out");
	//ofstream fout("B-large.out");	
	
	

	int N,M;
	


	for (int n=1;n<=T;n++)
	{
		fin>>N>>M;
		int ** a=new int*[N];
		for (int t1=0;t1<N;t1++)
		{
			a[t1]=new int[M];
		     for (int t2=0;t2<M;t2++)
		       fin>>a[t1][t2];
		}
		
			
			
		string num=check(N,M,a);
	    	
		fout<<"Case #"<<n<<": ";
	
		fout<<num<<endl;
		for (int t1=0;t1<N;t1++)
		delete [] a[t1];
		num="";
	}
	
	
	
	return 0;
}