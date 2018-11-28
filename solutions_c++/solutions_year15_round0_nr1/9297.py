#include"iostream"
#include"fstream"
#include"vector"
using namespace std;

typedef int int32;
typedef unsigned char uint8;
typedef unsigned int uint32;

unsigned int CalcNumOfAudienceNeeded(const vector<uint32>& SArray)
{
	const uint32 ArraySize = SArray.size();

	uint32 CCount = 0; // Current audience
	uint32 NCount = 0; // audience needed

	for (uint32 seek = 0; seek<ArraySize; seek = seek + 1)
	{
		if (SArray[seek] == 0){ continue; }

		int32 Offset = seek - CCount;

		Offset = Offset > 0 ? Offset : 0;

		NCount = NCount + Offset;
		CCount = CCount + SArray[seek] + Offset;
	}

	return NCount;
}

int main()
{
	freopen("output.txt","w",stdout);
	
	uint32 CaseCount = 0;
	::cin >> CaseCount;

	for (uint32 seek = 0; seek<CaseCount; seek = seek + 1)
	{
		uint32 Smax = 0;
		::cin >> Smax;

		vector<uint32> SArray(Smax + 1);

		//InitArray
		for (uint32 seek_shy = 0; seek_shy <= Smax; seek_shy = seek_shy + 1)
		{
			char Num;
			::cin >> Num;

			SArray[seek_shy] = Num - '0';
		}

		//Calc
		::cout << "Case #" << seek + 1<< ": " << CalcNumOfAudienceNeeded(SArray) << endl;
	}

	return 0;
}