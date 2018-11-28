#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std;

void main()
{
	int testCases, noOfblocks, first=0 , second=0, casecount=0 , kenwincount=0;
	double  naomiblocks[1000],kenblocks[1000]  , max , secondmax , lowest , naomicall ;
	ifstream fin("D-large.in");
	ofstream fout("outputfile.txt");

	fin>>testCases;

	while(testCases>0)
	{
		casecount++;
		fin>>noOfblocks;

		for(int i=0;i<noOfblocks;i++)
		{
			fin>>naomiblocks[i];
		}

		for(int i=0;i<noOfblocks;i++)
		{
			fin>>kenblocks[i];
		}

		double hold;
		for(int i=0; i<noOfblocks-1; i++)
			{
				for(int j=0; j<noOfblocks-1; j++)
				{
					if(naomiblocks[j]>naomiblocks[j+1])
					{
					  hold=naomiblocks[j];
					  naomiblocks[j]=naomiblocks[j+1];
					  naomiblocks[j+1]=hold;        
					 }
					if(kenblocks[j]>kenblocks[j+1])
					{
					  hold=kenblocks[j];
					  kenblocks[j]=kenblocks[j+1];
					  kenblocks[j+1]=hold;        
					 }
			   }         
			}

		if(noOfblocks==1)
		{
			if(naomiblocks[noOfblocks-1]>kenblocks[noOfblocks-1])
			{
				first++;
				second++;
				fout<<"Case #"<<casecount<<": "<<first<<" "<<second<<endl;
			}
			else
				fout<<"Case #"<<casecount<<": "<<first<<" "<<second<<endl;
		}
		else
		{
		
			for(int i=0,j=0;i<noOfblocks && j<noOfblocks;i++,j++)
			{
check_again:	if(naomiblocks[i]>kenblocks[j])
				{
					first++;
				}
				else
				{
					i++;
					if(i==noOfblocks)
						break;
					goto check_again;
				}
			}

			for(int i=0,j=0;i<noOfblocks && j<noOfblocks;i++,j++)
			{
checkit:		if(naomiblocks[i]>kenblocks[j])
				{
					j++;
					if(j==noOfblocks)
						break;
					goto checkit;
				}
				else
				{
					kenwincount++;
				}
			}
		
			second=noOfblocks-kenwincount;
		fout<<"Case #"<<casecount<<": "<<first<<" "<<second<<endl;
		}
		first=0;
		second=0;
		kenwincount=0;
		testCases--;
	}


	
}