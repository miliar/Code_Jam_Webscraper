
#include <fstream>
#include <iostream>

#include <errno.h>
#include <string.h>

//****************************************************************************************************
unsigned int GetCnt(std::string &rsStack);
void Flip(bool *pbStack, unsigned int uiI);
void Dis(bool *pbStack, unsigned int uiLen);

//****************************************************************************************************
int main(int iCntArg, char *apzArgp[])
{
	if (iCntArg != 2)
	{
		std::cout << "Please enter input file " << std::endl;
		return 1;	
	}

	const char *pzFile = apzArgp[1];
	std::ifstream oReader(pzFile);	
	if ( ! oReader.is_open())
	{
		std::cout << "Unable to open file (" << pzFile << ") [" << strerror(errno) << "]" << std::endl;
		return 1;
	}

	unsigned short int usiCntCase;
	oReader >> usiCntCase;

	for (unsigned short int usiCase = 1; usiCase <= usiCntCase; usiCase ++)
	{
		std::string sStack;
		oReader >> sStack;	

		unsigned int uiCnt = GetCnt(sStack);
		std::cout << "Case #" << usiCase << ": "<< uiCnt << std::endl;
	}

	oReader.close();
	
	return 0;
}

//****************************************************************************************************
unsigned int GetCnt(std::string &rsStack)
{
	unsigned int uiLen = rsStack.length(); 
	bool abStack[uiLen + 1];	

	for (unsigned int uiIdx = 0; uiIdx < uiLen; uiIdx ++)	
	{
		abStack[uiIdx] = rsStack[uiIdx] == '+' ? true : false;
	}

	unsigned int uiRet = 0;
	unsigned int uiI = uiLen - 1;
	do
	{
		while (abStack[uiI] && uiI != 0)	
			uiI --;

		if (uiI == 0 && *abStack == true)
			break;
	
		if (abStack[0])
		{
			unsigned int uiJ = 0;
			for (; abStack[uiJ] && uiJ < uiLen; uiJ ++);	
			
			Flip(abStack, uiJ);
		}
		else 
			Flip(abStack, uiI + 1);	

		uiRet ++;
	}
	while (uiI != 0);

	return uiRet;
}

//****************************************************************************************************
void Flip(bool *pbStack, unsigned int uiI)
{

	for (unsigned int uiIdx = 0; uiIdx < (uiI + 1) / 2; uiIdx ++)
	{
		bool bTmp = pbStack[uiIdx];
		pbStack[uiIdx] = !pbStack[uiI - uiIdx - 1]; 
		pbStack[uiI - uiIdx - 1] = !bTmp;
	}
}

//****************************************************************************************************
void Dis(bool *pbStack, unsigned int uiLen)
{
	for (unsigned int uiIdx = 0; uiIdx < uiLen; uiIdx ++)
		std::cout << (pbStack[uiIdx] ? "+" : "-");

	std::cout << std::endl;
}
