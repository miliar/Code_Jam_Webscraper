#include <iostream>
#include "stdio.h"
#include "stdlib.h"
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;


ifstream  fin("A-small-attempt2.in");
ofstream fout("A-small-attempt2.out");
 
int N; 
int ans1,ans2;
 
int A[4][4];
 int B[4][4];
int myfunc();

int main()
{
   int T;
	fin>>T;
	int i=0;
	int res;

	 
	int x,y;
	while(i<T)
	{
		fin>>ans1;
		 
		for(x=0;x<4;x++)
		{
			for(y=0;y<4;y++)
			{
				fin>>A[x][y];
			}
		}
		
		fin>>ans2;
		 
		for(x=0;x<4;x++)
		{
			for(y=0;y<4;y++)
			{
				fin>>B[x][y];
			}
		}

		res=myfunc();
		i++;

		fout<<"Case #";
		fout<<i;
		fout<<": ";
		if(res==-1){fout<<"Bad magician!";}
		else if(res==0){fout<<"Volunteer cheated!";}
		else{fout<<res;}
		
		if(i!=T)
		{
			 fout<<"\n";
		}
	}
	return(0);
}
 
int myfunc()
{
	int myArray[16];
 	for(int i=0;i<16;i++){myArray[i]=0;}
 	
	//First Answer
	int rownum=ans1-1;
 	int temp,col;
	for(col=0;col<4;col++)
	{
		temp=A[rownum][col];
 		temp--;
		myArray[temp]+=1;
	}
	
	//Second Answer
	rownum=ans2-1;
  	for(  col=0;col<4;col++)
	{
		temp=B[rownum][col]; 
		temp--;
		myArray[temp]+=1;
	}

	//Result-Check for number of 2's
	int num2=0;
        int pos=-1;
	for(int x=0;x<16;x++)
	{
		//cout<<myArray[x];
		if(myArray[x]==2){num2++;pos=x;}
	}
	if(pos==-1){return(0);}
  	if(num2>1){return(-1);}
        return(pos+1);
	
}

/*
 int u,v;
    for(u=0;u<10001;u++)
    {
                        for(v=0;v<3;v++)
                        {
                                        maxstn[u][v]=0;
                        }
    }
	fin>>L1;
	fin>>L2;
	fin>>L3;
	fin>>C1;
	fin>>C2;
	fin>>C3;
	fin>>N;
	fin>>boardingpt;
	boardingpt--;
	fin>>destination;
	destination--;
	int temp;
	if(boardingpt>destination)
	{
                              temp=boardingpt;
                              boardingpt=destination;
                              destination=temp;
                              
   }

	int p;
	dist[0]=0;
	for(p=1;p<(N);p++)
	{
		fin>>dist[p];
	}
	fout<<func(boardingpt);
	 
	return(0);
*/
