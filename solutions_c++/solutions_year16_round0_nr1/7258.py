
#include <iostream>
#include <bitset>
#include <fstream>

//****************************************************************************************************
void DisBin(unsigned short int usiVal);
unsigned int GetMax(unsigned int uiIn);

//****************************************************************************************************
int main(int iCntArg, char *apzArg[])
{
	if (iCntArg != 2)
	{
		std::cout << "Please enter input file" << std::endl;
		return 1;
	}
	
	const char *pzFile = apzArg[1];

	std::ifstream oReader(pzFile);
	if ( ! oReader.is_open())
	{
		std::cout << "No such file or directory " << pzFile << std::endl;
		return 1;	
	}

	unsigned short int usiCntCase;
	oReader >> usiCntCase;
	for (unsigned short int usiCase = 1; usiCase <= usiCntCase; usiCase ++)
	{
		unsigned int uiVal;
		oReader >> uiVal;

		unsigned int uiMax = GetMax(uiVal);		
		std::cout << "Case #" << usiCase << ": ";
		if (uiMax == 0)
			std::cout  << "INSOMNIA"; 
		else
			std::cout << uiMax;
		std::cout << std::endl;
	}
	oReader.close();

	return 0;
}

//****************************************************************************************************
unsigned int GetMax(unsigned int uiIn)
{
	if (uiIn == 0)	
		return 0;

	unsigned short int usiDigits = 0b1111111111;
	unsigned int uiIdx = 1;
	for (; usiDigits != 0; ++uiIdx)	
	{
		for (unsigned int uiI = uiIdx * uiIn; uiI > 0; uiI /= 10)
		{
			register unsigned short int usiDigit = uiI % 10;

			usiDigits = usiDigits & ~(unsigned short int)(1 << usiDigit);
		}
	}

	return uiIn * (uiIdx - 1);
}

//****************************************************************************************************
void DisBin(unsigned short int usiVal)
{
	std::bitset<16> oVal(usiVal);
	std::cout << oVal ;
}
