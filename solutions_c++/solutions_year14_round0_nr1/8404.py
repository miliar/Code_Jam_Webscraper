#include <iostream>
#include <fstream>

void MagicTrickFunc(int nCaseNum, std::ifstream& file, std::ofstream& fileOut);
int main(void)
{
	// 테스트 케이스 수만큼 반복해야한다.
	// 2번을 섞어줘야 한다
	// 카드 배치를 저장할 2차원 배열이 필요하다
	// 선택된 행의 수를 저장할 배열이 필요하다
	// 답을 찾으러 고고~
	// 답이 몇개인지 카운트 한다
	// 답이 0개면 발룬티어 칫티드! 답이 2개 이상이면 밷 매지션! 하면 돼.

	int nTestCase = 0;
	char strTestCase[4];
	std::ifstream fileSmallIn;
	std::ofstream fileOut;
	fileOut.open("A-small-attempt2.out");
	fileSmallIn.open("A-small-attempt2.in");
	fileSmallIn>> strTestCase;
	nTestCase = atoi(strTestCase);

	for (int i=0; i<nTestCase; i++)
	{
		MagicTrickFunc(i+1, fileSmallIn, fileOut);
	}

	fileSmallIn.close();
	fileOut.close();
	return (0);
}

void MagicTrickFunc(int nCaseNum, std::ifstream& file, std::ofstream& fileOut)
{
	int arrCard[4][4];
	int arrRowOfFirstArrangement[4];
	int nRowOfFirstArrangement = 0;
	int nRowOfSecondArrangement = 0;
	int nAnswerCount = 0;
	int nAnswer = 0;
	int row, col;
	std::string strManyAnsMsg = "Bad magician!";
	std::string str0AnsMsg = "Volunteer cheated!";
	char strRowOfFirstArrangement[2];
	char strRowOfSecondArrangement[2];
	char strCard[4];
	char ch;

	file>> strRowOfFirstArrangement;
	nRowOfFirstArrangement = atoi(strRowOfFirstArrangement);
	for (row=0; row<4; row++)
	{
		for (col=0; col<4; col++)
		{
			file>> strCard;
			arrCard[row][col] = atoi(strCard);
			if (row+1 == nRowOfFirstArrangement)
				arrRowOfFirstArrangement[col] = arrCard[row][col];
		}
		
	}

	file>> strRowOfSecondArrangement;
	nRowOfSecondArrangement = atoi(strRowOfSecondArrangement);
	for (row=0; row<4; row++)
	{
		for (col=0; col<4; col++)
		{
			file>> strCard;
			arrCard[row][col] = atoi(strCard);
		}
		
	}

	// 첫번째 정렬의 선택된 행과
	// 두번째 정렬의 선택된 행을 비교!!
	for (col=0; col<4; col++)
	{
		for (row=0; row<4; row++)
		{
			if (arrCard[nRowOfSecondArrangement-1][col] == arrRowOfFirstArrangement[row])
			{
				nAnswerCount++;
				nAnswer = arrRowOfFirstArrangement[row];
			}
		}
	}

	//std::cout<< "Case #"<< nCaseNum<< ": ";
	fileOut<< "Case #"<< nCaseNum<< ": ";
	if (nAnswerCount == 0)
	{
		//std::cout<< str0AnsMsg.c_str();
		fileOut<< str0AnsMsg.c_str();
	}
	else if(nAnswerCount > 1)
	{
		//std::cout<< strManyAnsMsg.c_str();
		fileOut<< strManyAnsMsg.c_str();
	}
	else
	{
		fileOut<< nAnswer;
	}
	fileOut<< std::endl;
}