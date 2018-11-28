#include <Windows.h>
#include <stdio.h>
#include <string>
#include <vector>

#define FILE_IN

using namespace std;

class InputDataSet
{
public:
	InputDataSet() { m_Smax.resize(4), m_People.resize(1000); }
	string		m_Smax;
	string		m_People;
};
int main()
{
	FILE *pFile = NULL;

	int caseCount = 0;
#ifndef FILE_IN
	scanf_s("%d", &caseCount);
#else
	fopen_s(&pFile, "A-small-attempt2.in", "r");
	fscanf_s(pFile, "%d", &caseCount);
#endif

	vector<InputDataSet> inputData;

	for (int i = 1; i <= caseCount; ++i)
	{
		InputDataSet newData;
#ifndef FILE_IN
		scanf_s("%s %s", &newData.m_Smax[0], newData.m_Smax.length(), &newData.m_People[0], newData.m_People.length());
#else
		fscanf_s(pFile, "%s", &newData.m_Smax[0], newData.m_Smax.length());
		fscanf_s(pFile, "%s", &newData.m_People[0], newData.m_People.length());
#endif
		inputData.push_back(newData);
	}

	fclose(pFile);
	fopen_s(&pFile, "A-small-attempt.out", "wt");

	for (size_t i = 0; i < inputData.size(); ++i)
	{
		const InputDataSet &curData = inputData[i];

		const int maxShyLevel = atoi(curData.m_Smax.c_str());

		int curOvationCount = 0;
		int needFriend = 0;

		//최종 부끄러움 쟁이들을 일으키는데 필요한 친구의 수.
		for (int shyLevel = 0; shyLevel <= maxShyLevel; ++shyLevel)
		{
			char person = curData.m_People[shyLevel];
			person = atoi(&person);

			const int notEnoughCount = shyLevel - (curOvationCount + needFriend);
			if (notEnoughCount > 0)
				needFriend		+= notEnoughCount;

			curOvationCount += person;
		}
#ifndef FILE_IN
		printf("Case #%d : %d\n", i + 1, needFriend);
#else
		fprintf(pFile, "Case #%d: %d\n", i + 1, needFriend);
#endif
	}
	return 0;
}