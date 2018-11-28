// codejam201401.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include <iostream>
#include <tchar.h>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	short nTestcases;
	short nCurrentCase = 0;

	cin >> nTestcases;

	while (nCurrentCase++ < nTestcases)
	{
		double C, F, X;
		double nextFarmTime, finishTimeNotBuy, finishTimeBuy;
		double currentProduce = 2;
		double totalTime = 0;

		cin >> C >> F >> X;

		while (true)
		{
			nextFarmTime = C / currentProduce;
			finishTimeNotBuy = X / currentProduce;
			finishTimeBuy = nextFarmTime + (X / (currentProduce + F));

			if (finishTimeNotBuy <= finishTimeBuy)
			{
				totalTime += finishTimeNotBuy;
				break;
			}

			currentProduce += F;
			totalTime += nextFarmTime;
		}

		cout << "Case #" << nCurrentCase << ": ";
		printf("%.7lf", totalTime);
		cout << endl;
	}


	return 0;
}

