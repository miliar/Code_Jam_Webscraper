// q1.cpp : Defines the entry point for the console application.
//



#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <fstream>

using namespace std;




int main()
{
	int t;





	ifstream fp;
	ofstream fout;

	fp.open("input.txt",ios::beg);

	fout.open("output.txt",ios::beg);

	fp >> t;
	
	int mote;
	int *moteArray=new int[101];
	int *moves=new int[101];
	int numMote;




	for(int T=0;T<t;++T)
	{
		fp>>mote;
		fp>>numMote;
		
		for(int iMoteArray=0;iMoteArray<numMote;++iMoteArray)
			fp>>moteArray[iMoteArray];
				

		int i,j;
		for(i=0;i<numMote;i++)
		{
			for(j=0;j<i;j++)
			{
				if(moteArray[i]<moteArray[j])
				{
					int temp=moteArray[i];  
					moteArray[i]=moteArray[j];
					moteArray[j]=temp;
				}

			}

		}

		int breaker=0;
		for(int iMoteArray=0;(iMoteArray<numMote) && (breaker==0);++iMoteArray)
		{
			if (iMoteArray==0)
				moves[iMoteArray]=0;
			else			
				moves[iMoteArray]=moves[iMoteArray-1];

			while(1){

				if(mote>moteArray[iMoteArray])
				{
					mote=mote + moteArray[iMoteArray];
					break;

				}
				else if(mote <= moteArray[iMoteArray])
				{
					if(mote==1){
						fout<<"Case #"<<T+1<<": "<<numMote<<endl; 
						breaker=1;
						break;

					}
					else if(mote>1)
					{
						mote=2*mote-1;
						moves[iMoteArray]=moves[iMoteArray]+1;
					}
				}
			}


		}
		
		for(int iMoteArray=0;(iMoteArray<numMote) && (breaker==0);++iMoteArray)
		{
			
				int prvVal;
				if(iMoteArray==0)
					prvVal = 0;
				else 
					prvVal =  moves[iMoteArray-1] ;

			
				if( ( moves[iMoteArray] )>( numMote - iMoteArray + prvVal )  )
				{
					fout<<"Case #"<<T+1<<": "<<(numMote - iMoteArray  + prvVal)<<endl;
					break;
				}
				else if(iMoteArray==(numMote-1))
				{
					fout<<"Case #"<<T+1<<": "<<moves[iMoteArray]<<endl;
					break;
				}
		}


	}

	fp.close();
	fout.close();

}







