#include <iostream>
#include <fstream>

using namespace std;


int main()
{
	int iT;			// 케이스의 수
	

	ifstream inputText;
	inputText.open("A-small-attempt3.in");

	ofstream outputText;
	outputText.open("Solve.txt");


	if (!inputText)
	{
		cout << "Cannot Open" << endl;

		return 0;
	}

	
	inputText >> iT;
	//cout << iT << endl;


	
	for (int i = 0; i < iT; i++ )
	{
		int audience;	// 청중의 숫자
		inputText >> audience;

		int standAudience  = 0; // 일어선 청중의 숫자
		int inviteAudience = 0; // 동원해야 할 청중의 숫자

		int calcString;	// 문제에서 제시된 문자열
		inputText >> calcString;

		int temp = 1; // 계산을위한 임시 숫자
		for (int k = 0; k < audience; k++ )
		{
			temp *= 10;
		}

		
		standAudience += calcString / temp;	//바로 일어서는 관객을 먼저 구한다.
		calcString -= calcString / temp * temp;


		for (int j = 1; j <= audience; j++ )
		{
			temp /= 10;

			int temp2 = calcString / temp;

			if ( temp2 > 0 )
			{
				if (standAudience >= j) // 조건이 충족되면 바로 관객이 일어섰다는 의미이다.
				{
					standAudience += calcString / temp;	//바로 일어서는 관객을 구한다.
				}
				else // 조건이 충족되지 않았으므로 조건을 충족시킨다.
				{
					inviteAudience += j - standAudience;
					standAudience += inviteAudience;
					standAudience += calcString / temp;
				}
			}

			calcString -= calcString / temp * temp;
		}

		//cout << "Case #" << i+1 << ": " << inviteAudience << endl;
		outputText << "Case #" << i + 1 << ": " << inviteAudience << endl;
	}
	
	
	inputText.close();
	outputText.close();


	return 0;
}


