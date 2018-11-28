#include <iostream>
#include <cstring>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <vector>

using namespace std;

int main( void )
{
	fstream inputfile_fsp;
	fstream outputfile_fsp;
	
	int tcases_i;
	long numOfMush_l;
	long timings_la[1020];
	long tempDiffVal_l;
	long maxDiffVal_l;
	long rate_l;
	long maxEat_l;
	long long diffVal_ll;  // ans to the first part
	long long eatConstRate_ll;  // ans to the second part
	

	inputfile_fsp.open( "A-large.in", ios::in );
	outputfile_fsp.open( "A-large.out", ios::out );
	
	
	inputfile_fsp >> tcases_i;
	
	for( int i = 0; i < tcases_i; i++ )
	{
		inputfile_fsp >> numOfMush_l;
		
		diffVal_ll = 0;
		maxDiffVal_l = 0;
		for( int j = 0; j < numOfMush_l; j++ )
		{
			inputfile_fsp >> timings_la[j];
			if ( j == 0 )
			{
				continue;
			}
			else
			{
				tempDiffVal_l = timings_la[j-1] - timings_la[j];
				if( tempDiffVal_l > 0 )
				{
					diffVal_ll = diffVal_ll + tempDiffVal_l;
					if( tempDiffVal_l > maxDiffVal_l )
					{
						maxDiffVal_l =  tempDiffVal_l;
					}
				}
			}
		}
		
		rate_l = maxDiffVal_l / 10;
		//maxEat_l = rate_l * 10;
		maxEat_l = maxDiffVal_l;
		eatConstRate_ll = 0;
		
		cout << "maxEat_l = " << maxEat_l << endl;
		
		for( int j = 0; j < numOfMush_l; j++ )
		{
			if ( j == (numOfMush_l - 1) )
			{
				continue;
			}
			else
			{
				if( timings_la[j] < maxEat_l )
				{
					eatConstRate_ll = eatConstRate_ll + timings_la[j];
				}
				else
				{
					eatConstRate_ll = eatConstRate_ll + maxEat_l;
				}
			}
		}
		
		cout << "Case #" << i+1 << ": " << diffVal_ll << " " << eatConstRate_ll << endl;
		outputfile_fsp << "Case #" << i+1 << ": " << diffVal_ll << " " << eatConstRate_ll << endl;
		
	}
}
