// gcj2015_qual.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"

char multiply(char a, char b)
{
	switch (a)
	{
	case '1':
		switch (b)
		{
		case '1':
			return '1';
			break;
		case 'i':
			return 'i';
			break;
		case 'j':
			return 'j';
			break;
		case 'k':
			return 'k';
			break;
		case '0'://-1
			return '0';
			break;
		case '!'://-i
			return '!';
			break;
		case '?'://-j
			return '?';
			break;
		case '3'://-k
			return '3';
			break;
		}
		break;
	case 'i':
		switch (b)
		{
		case '1':
			return 'i';
			break;
		case 'i':
			return '0';
			break;
		case 'j':
			return 'k';
			break;
		case 'k':
			return '?';
			break;
		case '0'://-1
			return '!';
			break;
		case '!'://-i
			return '1';
			break;
		case '?'://-j
			return '3';
			break;
		case '3'://-k
			return 'i';
			break;
		}
		break;
	case 'j':
		switch (b)
		{
		case '1':
			return 'j';
			break;
		case 'i':
			return '3';
			break;
		case 'j':
			return '0';
			break;
		case 'k':
			return 'i';
			break;
		case '0'://-1
			return '?';
			break;
		case '!'://-i
			return 'k';
			break;
		case '?'://-j
			return '1';
			break;
		case '3'://-k
			return '!';
			break;
		}
		break;
	case 'k':
		switch (b)
		{
		case '1':
			return 'k';
			break;
		case 'i':
			return 'j';
			break;
		case 'j':
			return '!';
			break;
		case 'k':
			return '0';
			break;
		case '0'://-1
			return '3';
			break;
		case '!'://-i
			return '?';
			break;
		case '?'://-j
			return 'i';
			break;
		case '3'://-k
			return '1';
			break;
		}
		break;
	case '0'://-1
		switch (b)
		{
		case '1':
			return '0';
			break;
		case 'i':
			return '!';
			break;
		case 'j':
			return '?';
			break;
		case 'k':
			return '3';
			break;
		case '0'://-1
			return '1';
			break;
		case '!'://-i
			return 'i';
			break;
		case '?'://-j
			return 'j';
			break;
		case '3'://-k
			return 'k';
			break;
		}
		break;
	case '!'://-i
		switch (b)
		{
		case '1':
			return '!';
			break;
		case 'i':
			return '1';
			break;
		case 'j':
			return '3';
			break;
		case 'k':
			return 'j';
			break;
		case '0'://-1
			return 'i';
			break;
		case '!'://-i
			return '0';
			break;
		case '?'://-j
			return 'k';
			break;
		case '3'://-k
			return '?';
			break;
		}
		break;
	case '?'://-j
		switch (b)
		{
		case '1':
			return '?';
			break;
		case 'i':
			return 'k';
			break;
		case 'j':
			return '1';
			break;
		case 'k':
			return '!';
			break;
		case '0'://-1
			return 'j';
			break;
		case '!'://-i
			return '3';
			break;
		case '?'://-j
			return '0';
			break;
		case '3'://-k
			return 'i';
			break;
		}
		break;
	case '3'://-k
		switch (b)
		{
		case '1':
			return '3';
			break;
		case 'i':
			return '?';
			break;
		case 'j':
			return 'i';
			break;
		case 'k':
			return '1';
			break;
		case '0'://-1
			return 'k';
			break;
		case '!'://-i
			return 'j';
			break;
		case '?'://-j
			return '!';
			break;
		case '3'://-k
			return '0';
			break;
		}
		break;
	}
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *pFileIn, *pFileOut;
	char readLine[10000] = {0}, bSplit[4] = "NO";
	int nCases = 0, isSplit, nLen, nRepeat, nOffset;
	pFileIn = fopen("data.in", "r");
	int ret = fopen_s(&pFileOut, "data.out", "wb");
	fgets(readLine, 10, pFileIn);
	sscanf(readLine, "%d", &nCases);
	for (int i = 0; i < nCases; i++)
	{		
		nOffset = 0;
		fgets(readLine, 20, pFileIn);
		sscanf(readLine, "%d", &nLen);
		if (nLen >= 10000)
			nOffset += 6;
			else if (nLen >= 1000)
				nOffset += 5;
				else if (nLen >= 100)
					nOffset += 4;
					else if (nLen >= 10)
						nOffset += 3;
						else
							nOffset += 2;
		sscanf(readLine + nOffset, "%d", &nRepeat);
		fread(readLine, 1, nLen, pFileIn);
		//fgets(readLine, nLen, pFileIn);
		isSplit = 0;
		char x,y;
		int nChar = 1;
		x = readLine[0];
		for (int j = 1; j < nRepeat*nLen; j++)
		{
			if ((x == 'i') && (isSplit == 0))
			{
				isSplit++;
				x = readLine[nChar];
				nChar++;
				if (nChar >= nLen)
					nChar = 0;
				continue;
			}
			if ((x == 'j') && (isSplit == 1))
			{
				isSplit++;
				x = readLine[nChar];
				nChar++;
				if (nChar >= nLen)
					nChar = 0;
				continue;
			}
			y = readLine[nChar];
			x = multiply(x, y);
			nChar++;
			if (nChar >= nLen)
				nChar = 0;			
				
		}
		if ((x == 'k')&&(isSplit == 2))
		{
			bSplit[0] = 'Y';
			bSplit[1] = 'E';
			bSplit[2] = 'S';
		}
		else
		{
			bSplit[0] = 'N';
			bSplit[1] = 'O';
			bSplit[2] = 0;
		}
		fprintf(pFileOut, "Case #%d: %s\n", i+1, bSplit);
		fread(readLine, 1, 1, pFileIn);
	}
	fcloseall();	
	return 0;
}

