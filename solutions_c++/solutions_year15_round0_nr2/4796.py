#include <stdio.h>
#include <vector>
#include <set>
#include <algorithm>

struct DivideInfo
{
	int minuteCost;
	int maxPancakeNum;
	int minimumCost;
	int additionalCost;
};

int GetMaxPancakeNumByDivide(int pancakeNum, int divideValue)
{
	return (pancakeNum / (divideValue + 1)) + (pancakeNum % (divideValue + 1) ? 1 : 0);
}

int GetMinMinuteFromPrev(int pancakeNum, std::vector<DivideInfo>& prevDivideInfoVector)
{
	int result = prevDivideInfoVector[0].maxPancakeNum;
	int len = prevDivideInfoVector.size();

	for (int i = 0; i < len; i++)
	{
		if (pancakeNum >= prevDivideInfoVector[i].maxPancakeNum)
		{
			if (result > prevDivideInfoVector[i].minuteCost + prevDivideInfoVector[i].additionalCost)
			{
				result = prevDivideInfoVector[i].minuteCost + prevDivideInfoVector[i].additionalCost;
			}
		}
	}

	return result;
}

int main()
{
	int testN;
	int tem;
	scanf_s("%d", &testN);

	for (int test = 1; test <= testN; ++test)
	{
		int D = 0;
		int panArr[1001] = {0};
		DivideInfo temDivideInfo;
		std::vector<std::vector<DivideInfo> > divideInfoVectorArr;
		std::vector<DivideInfo> temDivideInfoVector;
		std::set<int> temSet;
		int maxPancake = 0;
		int minMinute = 1000;
		int len = 0;
		int temLen = 0;

		temSet.clear();

		scanf_s("%d", &D);

		for (int i = 0; i < D; i++)
		{
			scanf_s("%d", &tem);
			panArr[tem]++;
			temSet.insert(tem);
			if (tem > maxPancake)
			{
				maxPancake = tem;
			}
		}

		// 최적으로 나눠야 할 값들을 구한다.
		temLen = sqrt(maxPancake) + 1;
		for (int divideValue = 0; divideValue < temLen; divideValue++)
		{
			temSet.insert(GetMaxPancakeNumByDivide(maxPancake, divideValue));
		}
		
		std::vector<int> divideArr(temSet.begin(), temSet.end());
		std::sort(divideArr.begin(), divideArr.end());
		std::reverse(divideArr.begin(), divideArr.end());

		for (int pancakeNum = maxPancake; pancakeNum > 0; pancakeNum--)
		{
			if (panArr[pancakeNum])
			{
				temDivideInfoVector.clear();
				len = sqrt(pancakeNum) + 1;
				int divideArrIdx = 0;
				int temLen = divideArr.size();
				while (divideArrIdx < temLen && divideArr[divideArrIdx] >= pancakeNum) divideArrIdx++;

				for (int divideValue = 0; divideValue < len; divideValue++)
				{
					temDivideInfo.minuteCost = divideValue * panArr[pancakeNum];
					temDivideInfo.maxPancakeNum = GetMaxPancakeNumByDivide(pancakeNum, divideValue);
					temDivideInfo.minimumCost = 1000;
					temDivideInfo.additionalCost = 0;

					if (divideArrIdx < temLen)
					{
						if (divideArr[divideArrIdx] > temDivideInfo.maxPancakeNum)
						{
							int max = temDivideInfo.maxPancakeNum;
							while (divideArrIdx < temLen && divideArr[divideArrIdx] > max)
							{
								temDivideInfo.maxPancakeNum = divideArr[divideArrIdx];
								temDivideInfoVector.push_back(temDivideInfo);
								divideArrIdx++;
							}
							if (divideArr[divideArrIdx] == max) divideArrIdx++;
							temDivideInfo.maxPancakeNum = max;
						}
						else
						{
							while (divideArrIdx < temLen && divideArr[divideArrIdx] >= temDivideInfo.maxPancakeNum) divideArrIdx++;
						}
					}

					temDivideInfoVector.push_back(temDivideInfo);
				}
				divideInfoVectorArr.push_back(temDivideInfoVector);
			}
		}

		// 맨 뒤(배열이 1개라면 맨 앞)의 다이나믹을 계산해준다.
		len = divideInfoVectorArr.size() - 1;
		for (int i = 0; i < divideInfoVectorArr[len].size(); i++)
		{
			divideInfoVectorArr[len][i].minimumCost = divideInfoVectorArr[len][i].minuteCost + divideInfoVectorArr[len][i].maxPancakeNum;
		}

		// 뒤에서부터 다이나믹 계산을 해준다.
		for (int i = divideInfoVectorArr.size() - 2; i >= 0; i--)
		{
			len = divideInfoVectorArr[i].size();
			for (int j = 0; j < len; j++)
			{
				divideInfoVectorArr[i][j].additionalCost = GetMinMinuteFromPrev(divideInfoVectorArr[i][j].maxPancakeNum, divideInfoVectorArr[i + 1]);
				divideInfoVectorArr[i][j].minimumCost = divideInfoVectorArr[i][j].minuteCost + divideInfoVectorArr[i][j].maxPancakeNum + divideInfoVectorArr[i][j].additionalCost;
			}
		}
		
		len = divideInfoVectorArr[0].size();
		for (int i = 0; i < len; i++)
		{
			if (minMinute > divideInfoVectorArr[0][i].minimumCost)
			{
				minMinute = divideInfoVectorArr[0][i].minimumCost;
			}
		}

		printf("Case #%d: %d\n", test, minMinute);
	}
}