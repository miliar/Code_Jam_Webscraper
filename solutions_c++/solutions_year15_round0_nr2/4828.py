#include <Windows.h>
#include <string>
#include <vector>
#include <algorithm>

#define FILE_IN

#define INPUT_FILENAME		"B-small-attempt7.in"
#define OUTPUT_FILENAME		"Result.out"

using namespace std;

class InputDataSet
{
public:
	InputDataSet() { m_Diner = 1, m_Pancake.reserve(1000); }
	int			m_Diner;
	vector<int>	m_Pancake;
};
int main()
{
	FILE *pFile = NULL;

	int caseCount = 0;
#ifndef FILE_IN
	scanf_s("%d", &caseCount);
#else
	fopen_s(&pFile, INPUT_FILENAME, "r");
	fscanf_s(pFile, "%d", &caseCount);
#endif

	vector<InputDataSet> inputData;

	for (int i = 1; i <= caseCount; ++i)
	{
		InputDataSet newData;
#ifndef FILE_IN
		scanf_s("%d", &newData.m_Diner);
		
		for (int i = 0; i < newData.m_Diner; ++i)
		{
			int newValue = 1;
			scanf_s("%d", &newValue);
			newData.m_Pancake.push_back(newValue);
		}
#else
		fscanf_s(pFile, "%d", &newData.m_Diner);

		for (int j = 0; j < newData.m_Diner; ++j)
		{
			int newValue = 1;
			fscanf_s(pFile, "%d", &newValue);
			newData.m_Pancake.push_back(newValue);
		}
#endif
		inputData.push_back(newData);
	}

#ifdef FILE_IN
	fclose(pFile);
	fopen_s(&pFile, OUTPUT_FILENAME, "wt");
#endif

	for (size_t i = 0; i < inputData.size(); ++i)
	{
		InputDataSet &curData = inputData[i];

		sort(curData.m_Pancake.begin(), curData.m_Pancake.end());

		int maxCakeCount	= curData.m_Pancake[curData.m_Pancake.size() - 1];
		int eatingTurn		= maxCakeCount;

		//�� ���..2 �� �ƴ϶� 3, 4�ε� try �غ��� �ȴ�...
		for (int moveCakeCount = 1; moveCakeCount < maxCakeCount; ++moveCakeCount)
		{
			//diner �� cake �� �й�����.
			for (int divCake = 0; divCake < maxCakeCount; ++divCake)
			{
				vector<int> tempCakePlates = curData.m_Pancake;
				int useTurn = 0;

				//���������� ������... �׳� ��ü�� ������ ���� �۰� ���� ���� ã�ƺ���..����
				for (;;)
				{
					sort(tempCakePlates.begin(), tempCakePlates.end());
					int &maxCake = tempCakePlates[tempCakePlates.size() - 1];

					//����� Ÿ�� - �й�� ���� �� ���� ���
					if (moveCakeCount < maxCake && maxCake > divCake + 1)
					{
						const int value = maxCake;
						maxCake = value - moveCakeCount;
						tempCakePlates.push_back(static_cast<int>(value - maxCake));
						++useTurn;
						continue;
					}
					useTurn += maxCake;
					break;
				}

				eatingTurn = min(eatingTurn, useTurn);
			}
		}

#ifndef FILE_IN
		printf("Case #%d: %d\n", i + 1, eatingTurn);
#else
		fprintf(pFile, "Case #%d: %d\n", i + 1, eatingTurn);
#endif
	}

#ifdef FILE_IN
	fclose(pFile);
#endif
	return 0;
}