#include "TaskProcessor.h"
#include <map>

std::string CTaskProcessor::findPlan( const vector<int>& partiesCounts )
{
	vector<int> counts;
	counts.assign( partiesCounts.begin(), partiesCounts.end() );
	const int n = counts.size();

	string plan = "";
	do {
		int maxIndex = -1;
		int secondMaxIndex = -1;
		int maxValue = -1;
		int secondMaxValue = -1;
		int totalCount = 0;
		for( int i = 0; i < n; i++ ) {
			assert( counts[i] >= 0 );
			totalCount += counts[i];
			if( counts[i] > maxValue ) {
				secondMaxValue = maxValue;
				secondMaxIndex = maxIndex;
				maxValue = counts[i];
				maxIndex = i;
			} else if( counts[i] > secondMaxValue ) {
				secondMaxValue = counts[i];
				secondMaxIndex = i;
			}
		}
		if( totalCount == 0 ) {
			break;
		}
		assert( maxValue <= totalCount / 2 );

		if( !plan.empty() ) {
			plan += " ";
		}
		if( secondMaxValue > (totalCount - 1) / 2 ) {
			plan += 'A' + maxIndex;
			plan += 'A' + secondMaxIndex;
			counts[maxIndex]--;
			counts[secondMaxIndex]--;
		} else {
			plan += 'A' + maxIndex;
			counts[maxIndex]--;
		}
		
	} while( 1 == 1 );

	return plan;
}
