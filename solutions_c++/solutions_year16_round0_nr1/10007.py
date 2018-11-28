#include "CountingSheep.h"


void cCountingSheep::processTestCases()
{
	m_fileIO.openInputFile("Input");
	m_fileIO.openOutputFile("Output");
	m_fileIO.getNumOfTestCases(&m_numTestCases);
	
	unsigned long inputNum = 0;
	for (int i = 0; i < m_numTestCases; i++)
	{
		m_fileIO.getInputNumber(inputNum);
		resetDigitMap();
		executeTestCase(inputNum, i + 1);
	}
}




void cCountingSheep::executeTestCase(unsigned long inputNumber, int caseNum)
{
	unsigned long currentCount = inputNumber;
	for (int i = 1; i <= 99; i++)
	{
		findDigits(currentCount);
		if (checkDigitMap())
		{
			char outputString[35];
			sprintf(outputString, "Case #%d: %lu\n", caseNum, currentCount);
			m_fileIO.outputToFile(outputString);
			return;
		}
		currentCount = inputNumber * i;
	}
	char outputString[35];
	sprintf(outputString, "Case #%d: INSOMNIA\n", caseNum);
	m_fileIO.outputToFile(outputString);

}

void cCountingSheep::findDigits(unsigned long inputNum)
{
	do {
		int digit = inputNum % 10;
		m_digitMap[digit] = 1;
		inputNum /= 10;
	} while (inputNum > 0);
}

bool cCountingSheep::checkDigitMap()
{
	for (int i = 0; i < 10; i++)
	{
		if (m_digitMap[i] == 0)
		{
			return false;
		}
	}
	return true;
}

void cCountingSheep::resetDigitMap()
{
	for (int i = 0; i < 10; i++)
	{
		m_digitMap[i] = 0;
	}
}