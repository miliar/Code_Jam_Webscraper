#include<iostream>
#include<stdio.h>
#include<conio.h>
using namespace std;
double naomiBlocks[1000]={0};
double kenBlocks[1000]={0};
unsigned int N;
void sort()
{
	double temp;
	unsigned int i,j;
	for(i=0;i<N;i++)
		for(j=i+1 ;j< N ;j++)
		{
			if(naomiBlocks[i]<naomiBlocks[j])
			{ 
				temp = naomiBlocks[j];
				naomiBlocks[j]=naomiBlocks[i];
				naomiBlocks[i] = temp;
				
			}
			if(kenBlocks[i]<kenBlocks[j])
			{ 
				temp = kenBlocks[j];
				kenBlocks[j]=kenBlocks[i];
				kenBlocks[i] = temp;
				
				}
				
				
			
			
			
			}
	
	}
int main()
{
		unsigned int T =0,C;
		int i;
		unsigned int warCount, decietfulWarCount;
		unsigned int naomiLoses , kenWins,kenCounter,naomiCounter;
		cin >> T;
		
		for(C = 1 ; C <=T;C++)
		{
			N = -1;
			warCount = 0;
			kenWins=0;
			naomiLoses = 0;
			decietfulWarCount = 0;
			cin >>N;
			for(i=0;i<N;i++)
			{
				cin>> naomiBlocks[i];
			}
			for(i=0;i<N;i++)
			{
				cin>> kenBlocks[i];
			}
			sort();
			/*for(i=0; i< N;i++)
			{
				cout <<naomiBlocks[i] << " ";
			}
			cout<<endl;
			for(i=0; i< N;i++)
			{
				cout <<kenBlocks[i] << " ";
			}
			cout<<endl<<"*******************************"<<endl;
			*/
			/*for(i= 0;i < N; i++)
			{
				if(naomiBlocks[0]< kenBlocks[i])
					kenWins++;
					else
						break;
			}
			for(i= N-1;i >=0; i--)
			{
				if(naomiBlocks[i]< kenBlocks[N-1])
					naomiLoses++;
					else
						break;
			}
		*/
		
		    kenCounter = 0;
			naomiCounter = 0;
			for(i=0;i<N;i++)
			{
				if(naomiBlocks[i] > kenBlocks[kenCounter])
				{
					//kenBlocks[N-1-warCount]=0;
					warCount++;
					
					}
					else
					{
						kenCounter++;
					}
					
				if(naomiBlocks[naomiCounter]>kenBlocks[i])
				{
					naomiCounter++;
					decietfulWarCount++;
				}
				
				
				}
			//decietfulWarCount = N - (naomiLoses > kenWins ? naomiLoses : kenWins);
			cout<<"Case #"<<C<<": "<<decietfulWarCount<<" "<<warCount<<endl;
			}
	return 0;
}


