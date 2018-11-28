#include "stdafx.h"
#include "math.h"
#include <iostream>     // std::cout
#include <algorithm>    // std::sort
#include <vector>       // std::vector

int solve(std::vector<unsigned __int64>& v, unsigned __int64 arman, int numberOfOperations ) {

	if( arman == 1 )
	{
		return v.size();
	}

	// sort
	std::sort (v.begin(), v.end() );  

	unsigned __int64 currentValue = arman;
	for (std::vector<unsigned __int64>::iterator it=v.begin(); it!=v.end(); ++it)
	{
		if( *it < currentValue )
		{
			currentValue += *it;
		}
		else
		{
			numberOfOperations++;

			// add
			int addedResult = 0;
			std::vector<unsigned __int64> addVector (v);
			addVector.push_back( currentValue - 1 );
			addedResult = solve( addVector, arman, numberOfOperations );
			//printf( "%d add result %d \n", numberOfOperations, addedResult );

			// remove
			std::vector<unsigned __int64> removeVector (v);
			removeVector.pop_back();
			int removedResult = solve( removeVector, arman, numberOfOperations );
			
			return std::min( addedResult, removedResult );
		}
	}

	return numberOfOperations;
}

bool myfunction (unsigned __int64 i,unsigned __int64 j) { return (i<j); }

int _tmain(int argc, _TCHAR* argv[])
{
	// Test code.
	////int myints[] = {32,71,12,45,26,80,53,33};
	////std::vector<int> myvector (myints, myints+sizeof(myints)/sizeof(int));
	////// using default comparison (operator <):
	////std::sort (myvector.begin(), myvector.end(), myfunction );  

	////for (std::vector<int>::iterator it=myvector.begin(); it!=myvector.end(); ++it)
	////	printf( "%d\n", *it );

	char  Buffer[ 32 ];
	int  numTestCases;

	// read number of test cases
	scanf( "%d", &numTestCases );

	for( int i = 0; i < numTestCases; ++i )
	{
		unsigned __int64 arman = 0;
		unsigned __int64 numMotes = 0;
		unsigned __int64 motes[ 100 ];

		memset( &motes, 0, sizeof(motes) );

		scanf( "%d", &arman );
		scanf( "%d", &numMotes );

		for( int j = 0; j<numMotes; ++j )
		{
			scanf( "%d", &motes[j] );
		}

		std::vector<unsigned __int64> myvector (motes, motes+numMotes);

		int minOperations = solve( myvector, arman, 0 );
		printf( "Case #%d: %d\n", i + 1, minOperations );

		////int numberOfOperations = 0;
		////while( myvector.size() > 0 )
		////{
		////	int numProcessed = 0;
		////	unsigned __int64 currentValue = arman;
		////	unsigned __int64 lastFailed = 0;
		////	
		////	// sort
		////	std::sort (myvector.begin(), myvector.end(), myfunction );  

		////	for (std::vector<unsigned __int64>::iterator it=myvector.begin(); it!=myvector.end(); ++it)
		////	{
		////		if( *it < currentValue )
		////		{
		////			currentValue += *it;
		////			numProcessed++;
		////		}
		////		else
		////		{
		////			lastFailed = *it;
		////			break;
		////		}
		////	}

		////	// done
		////	if( numProcessed >= myvector.size() )
		////	{
		////		break;
		////	}

		////	// need to add an operation
		////	numberOfOperations++;

		////	unsigned __int64 diff = lastFailed - currentValue;

		////	if( diff < currentValue )
		////	{
		////		if( ( currentValue - 1 + currentValue > lastFailed ) )
		////		{
		////			// add a value
		////			myvector.push_back( currentValue - 1 );
		////		}
		////		else
		////		{
		////			myvector.pop_back();
		////		}
		////	}
		////	else if( currentValue > 1 )
		////	{
		////		int moreTimesToAdd = 0;
		////		unsigned __int64 newCurrentValue = currentValue;

		////		while( diff > 0 )
		////		{
		////			moreTimesToAdd++;
		////			// max we can add
		////			newCurrentValue += newCurrentValue - 1;
		////			if( lastFailed >= newCurrentValue )
		////			{
		////				diff = lastFailed - newCurrentValue;
		////			}
		////			else
		////			{
		////				break;
		////			}
		////		}

		////		int numberLeft = myvector.size() - numProcessed;
		////		int newNumProcessed = 0;
		////		for (std::vector<unsigned __int64>::iterator it=myvector.begin(); it!=myvector.end(); ++it)
		////		{
		////			if( *it < newCurrentValue )
		////			{
		////				newCurrentValue += *it;
		////				newNumProcessed++;
		////			}
		////			else
		////			{
		////				lastFailed = *it;
		////				break;
		////			}
		////		}
		////		
		////		int newNumberLeft = myvector.size() + moreTimesToAdd - newNumProcessed;
		////		if( newNumberLeft < numberLeft )
		////		{
		////			myvector.push_back( currentValue - 1 );
		////		}
		////		else
		////		{
		////			myvector.pop_back();
		////		}
		////	}
		////	else
		////	{
		////		myvector.pop_back();
		////	}
		////}

		//printf( "Case #%d: %d\n", i+1, numberOfOperations );
	}

	return( 0 );
}