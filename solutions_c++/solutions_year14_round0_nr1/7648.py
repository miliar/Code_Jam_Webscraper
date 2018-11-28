#include <cstdio>
#include <set>
using namespace std;

int main()
{
	int T;

	scanf("%d", &T);

	for(int tCase = 0; tCase < T; tCase++)
	{
		int DummyArray[4];
		int FirstQuestionAns;
		int SecondQuestionAns;
		set<int> FirstSet;
		set<int> SecondSet;
		int CommonCount = 0;
		int CommonVal;

		FirstSet.clear();
		SecondSet.clear();

		scanf("%d", &FirstQuestionAns);

		for(int RowIndex = 1; RowIndex <= 4; RowIndex++)
		{
			for(int ColIndex = 0; ColIndex < 4; ColIndex++)
				scanf("%d", &DummyArray[ColIndex]);

			if(RowIndex == FirstQuestionAns)
			{
				FirstSet.insert(DummyArray[0]);
				FirstSet.insert(DummyArray[1]);
				FirstSet.insert(DummyArray[2]);
				FirstSet.insert(DummyArray[3]);
			}
		}

		scanf("%d", &SecondQuestionAns);

		for(int RowIndex = 1; RowIndex <= 4; RowIndex++)
		{
			for(int ColIndex = 0; ColIndex < 4; ColIndex++)
				scanf("%d", &DummyArray[ColIndex]);

			if(RowIndex == SecondQuestionAns)
			{
				SecondSet.insert(DummyArray[0]);
				SecondSet.insert(DummyArray[1]);
				SecondSet.insert(DummyArray[2]);
				SecondSet.insert(DummyArray[3]);
			}
		}

		for(set<int>::iterator FirstSetPtr = FirstSet.begin();
			FirstSetPtr != FirstSet.end();
			FirstSetPtr++)
		{
			if(SecondSet.find(*FirstSetPtr) != SecondSet.end())
			{
				CommonVal = *FirstSetPtr;
				CommonCount++;
			}
		}

		printf("Case #%d: ", tCase + 1);

		if(CommonCount == 0)
		{
			printf("Volunteer cheated!\n");
		}
		else if(CommonCount == 1)
		{
			printf("%d\n", CommonVal);
		}
		else
		{
			printf("Bad magician!\n");
		}
	}

	return 0;
}