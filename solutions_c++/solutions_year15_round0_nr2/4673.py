#include <iostream>
#include <typeinfo>
#include <fstream>
#include <functional>
#include <utility>
#include <vector>
#include <list>
#include <atomic>
#include <string>
#include <algorithm>

using namespace std;

#define MAX_CAKES_COUNT 9
#define MAX_CHOPS_COUNT	(9)

typedef vector<uint16_t> PlatesList;


static uint16_t chopValue(uint16_t val, uint16_t *chopsCount)
{
	uint16_t chunkSize = val; // / 2 + ((val % 2) ? 1 : 0);
	for (int i = chunkSize; i > 0; --i)
	{
		chopsCount[i - 1] = val / i - ((val % i == 0) ? 1 : 0);
	}
	return chunkSize;
}

uint16_t chopsCount[6][MAX_CHOPS_COUNT] = { 0 };
uint16_t chopValues[6] = { 0 };
uint16_t origValues[6] = { 0 };

static int getEatingTime(PlatesList &plates)
{
	// Index: cakesCount, Value: tablesCount

	int platesCount = 0;

	PlatesList uniqueCakesList;

	memset( chopsCount, 0, sizeof(chopsCount)/sizeof(chopsCount[0]) );

	int addedTime = 0,
		standed = 0;

	uint16_t *cakesCountFreq = new uint16_t[MAX_CAKES_COUNT];

	PlatesList::iterator begin = plates.begin(),
		end = plates.end();

	while (begin != end)
	{
		chopValues[platesCount] = chopValue(*begin, chopsCount[platesCount]);
		origValues[platesCount] = *begin;
		++platesCount;
		
		++begin;
	}

	begin = plates.begin();
	uint16_t minTime = *max_element( begin, end );
	uint16_t noMoreThen = minTime;

	uint16_t maxVal = 0,
			 totalTime = 0;
	int currCount = 0;
	for (int i1 = 0; i1 < chopValues[0];  ++i1)
	{
		maxVal =  1 + (i1);
		totalTime += chopsCount[0][i1];
		++currCount;
		if (currCount == platesCount)
		if (minTime > (totalTime + maxVal)) {
			minTime = (totalTime + maxVal); cout << minTime << endl;
		}

		for (int i2 = 0; i2 < chopValues[1]; ++i2)
		{
			maxVal = 1 + max(i1, i2);
			totalTime += chopsCount[1][i2];
			++currCount;
			if (currCount == platesCount)
			if (minTime > (totalTime + maxVal)) {
				minTime = (totalTime + maxVal); cout << minTime << endl;
			}

			for (int i3 = 0; i3 < chopValues[2] ; ++i3)
			{
				maxVal = 1 + max(max(i1, i2), i3);
				totalTime += chopsCount[2][i3];
				++currCount;
				if (currCount == platesCount)
				if (minTime > (totalTime + maxVal)) {
					minTime = (totalTime + maxVal); cout << minTime << endl;
				}
				for (int i4 = 0; i4 < chopValues[3]; ++i4)
				{
					maxVal = 1 + max(max(max(i1, i2), i3), i4);
					totalTime += chopsCount[3][i4];
					++currCount;
					if (currCount == platesCount)
					if (minTime > (totalTime + maxVal)) {
						minTime = (totalTime + maxVal); cout << minTime << endl;
					}
					for (int i5 = 0; i5 < chopValues[4]; ++i5)
					{
						maxVal = 1 + max(max(max(max(i1, i2), i3), i4), i5);
						totalTime += chopsCount[4][i5];
						++currCount;
						if (currCount == platesCount)
						if (minTime > (totalTime + maxVal)) {
							minTime = (totalTime + maxVal); cout << minTime << endl;
						}
						for (int i6 = 0; i6 < chopValues[5]; ++i6)
						{
							maxVal = 1 + max(max(max(max(max(i1, i2), i3), i4), i5), i6);
							totalTime += chopsCount[5][i6];
							++currCount;
							if (currCount == platesCount)
								if (minTime > (totalTime + maxVal)) {
									minTime = (totalTime + maxVal); cout << minTime << endl;
								}
							
							--currCount;
							totalTime -= chopsCount[5][i6];
						}

						--currCount;
						totalTime -= chopsCount[4][i5];
					}

					--currCount;
					totalTime -= chopsCount[3][i4];
				}

				--currCount;
				totalTime -= chopsCount[2][i3];
			}

			--currCount;
			totalTime -= chopsCount[1][i2];
		}		

		--currCount;
		totalTime -= chopsCount[0][i1];
	}

	if( minTime > noMoreThen)
	{
		cout <<" Error time calc: " << minTime << "is bigger then " << noMoreThen << endl;
	}

	return minTime;

#if 0
	// Clear the memory
	memset(cakesCountFreq, 0, sizeof(cakesCountFreq[0]) * MAX_CAKES_COUNT);

	// build a histogram of the cakes and unique cakes list
	while (begin != end)
	{
		if (cakesCountFreq[*begin] == 0)
			uniqueCakesList.push_back(*begin);

		++cakesCountFreq[*begin];
		++begin;
	}


	while (1)
	{
		begin = uniqueCakesList.begin();
		end = uniqueCakesList.end();

		// sort the list of cakes count
		sort(begin, end, greater<uint16_t>());

		// get new item
		begin = uniqueCakesList.begin();

		uint16_t dividedPartsCount = 1;
		uint16_t dividersTable[] = { 2, 3 };

		uint16_t tablesCount = 0;// cakesCountFreq[*begin];
		uint16_t partToMove = 0;// *begin / 2;
		uint16_t remainPart = 0;// partToMove + (*begin % 2);

		uint16_t minValue = 65535;

		bool isMovesFound = false;

		for (int i = 0; i < (sizeof(dividersTable) / sizeof(dividersTable[0])); ++i)
		{
			uint16_t tablesCount2 = cakesCountFreq[*begin];
			uint16_t divRemainPart = (*begin % dividersTable[i]);

			uint16_t partToMove2 = *begin / dividersTable[i];
			uint16_t remainPart2 = partToMove2 + divRemainPart;

			if (partToMove2 == 0) continue;

			uint16_t movesAmongAllTables = tablesCount2 * (dividersTable[i] - 1);
			// If Bonus from moving some cakes worth it
			if (((*begin) - remainPart2) > movesAmongAllTables)
			{
				uint16_t totCount = remainPart2 + movesAmongAllTables;
				if (minValue > totCount)
				{
					minValue = totCount;
					tablesCount = tablesCount2;
					partToMove = partToMove2;
					remainPart = remainPart2;
					dividedPartsCount = dividersTable[i] - 1;
					isMovesFound = true;
				}
			}
		}

		if (isMovesFound)
		{
			addedTime += tablesCount * dividedPartsCount;

			// Remove *begin from the frequencies table
			cakesCountFreq[*begin] = 0;

			// Remove *begin from the list
			uniqueCakesList.erase(begin);

			// Add created parts to the unique list
			if (cakesCountFreq[partToMove] == 0) {
				// create a unique item in the list
				uniqueCakesList.push_back(partToMove);
			}
			cakesCountFreq[partToMove] += tablesCount * dividedPartsCount;


			if (cakesCountFreq[remainPart] == 0) {
				// create a unique item in the list
				uniqueCakesList.push_back(remainPart);
			}
			cakesCountFreq[remainPart] += tablesCount;

		}
		else
			break;
	}

	delete[] cakesCountFreq;

	return *uniqueCakesList.begin() + addedTime;
#endif
}




int main()
{
	PlatesList platesList;
	
	ifstream file("D:\\B-small-attempt16.in");
	ofstream outF("D:\\out.txt");

	if (!file.is_open())
		cout << " Error open " << endl;

	uint32_t count;
	file >> count;

	for (uint32_t i = 0; i < count; ++i)
	{
		uint16_t platesCount;
		file >> platesCount;

		platesList.clear();

		for (uint16_t j = 0; j < platesCount; ++j)
		{
			uint16_t piesCount;

			file >> piesCount;

			platesList.push_back(piesCount);
		}

		// cout << "process " << str.c_str() << endl;

		int count = getEatingTime(platesList);
		outF << "Case #" << (i + 1) << ": " << count << '\n';
	}

	file.close();
	outF.close();

	return 0;
}