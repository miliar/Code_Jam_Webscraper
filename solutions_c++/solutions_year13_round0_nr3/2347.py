#include <stdio.h>
#include <string.h>
#include <math.h>

char A[101], B[101];
int Alen, Blen, strLen;
bool twoCheck;

void charPlus(char* str)
{
	int len = strLen;
	bool allCheck = true;

	if (len % 2 == 1)
	{
		str[len / 2] += 1;
		for (int i = len / 2; i < len - 1; i++)
		{
			if (str[i] > 1)
			{
				str[i] = str[len - i - 1] = 0;
				str[i + 1] += 1;
				str[len - i - 2] += 1;
			}
			else
				return;
		}
	}
	else
	{
		str[len / 2] += 1;
		str[len / 2 - 1] += 1;
		for (int i = len / 2; i < len - 1; i++)
		{
			if (str[i] > 1)
			{
				str[i] = str[len - i - 1] = 0;
				str[i + 1] += 1;
				str[len - i - 2] += 1;
			}
			else
				return;
		}

	}

	if (str[0] == 2)
	{
		strLen++;
		memset(str, 0, strLen + 1);
		str[0] = 1;
		str[len] = 1;
	}

	/*
	str[0] += 1;
	for (int i = 0; i < len; i++)
	{
		if (str[i] > 1)
		{
			str[i] = 0;
			if (i == 0)
			{
				str[i] = 1;
			}
			str[i + 1] += 1;
			if (i == len - 1)
			{
				strLen++;
			}
		}
	}
	*/
}

bool charPow(char* str, char* result)
{
	memset(result, 0, strLen * 2 + 1);

	int len = strLen;
	int i, j;
	//int maxLen;

	for (i = 0; i < len; i++)
	{
		if (str[i] == 0)
		{
			continue;
		}
		for (j = 0; j < len; j++)
		{
			result[i + j] += str[j] * str[i];
			if (result[i + j] >= 10)
			{
				return false;
			}
		}
	}

	return true;
}

int charCom(char *str1, int num)
{
	int len1 = strLen * 2 - 1;
	int len2;
	char* comStr;
	if (twoCheck)
	{
		len1 -= 2;
	}
	if (num == 1)
	{
		len2 = Alen;
		comStr = A;
	}
	else if (num == 2)
	{
		len2 = Blen;
		comStr = B;
	}

	if (len1 > len2)
	{
		return 1;
	}
	else if (len1 < len2)
	{
		return -1;
	}
	else
	{
		for (int i = len1 - 1; i >= 0; i--)
		{
			if (str1[i] > comStr[i])
			{
				return 1;
			}
			else if (str1[i] < comStr[i])
			{
				return -1;
			}
		}
		return 0;
	}
}
/*
bool isPalin(char* str, int num)
{
	int len;
	if (num == 1)
	{
		len = strLen;
	}
	else if (num == 2)
	{
		len = strLen * 2 - 1;
	}
	for (int i = 0; i < len / 2; i++)
	{
		if (str[i] != str[len - i - 1])
		{
			return false;
		}
	}

	return true;
}
*/
int main()
{
	int maxTest;
	scanf("%d", &maxTest);
	for (int testN = 1; testN <= maxTest; testN++)
	{
		int count = 0;
		char num[101] = {1};
		char powNum[201] = "";
		int len = 0;
		int beforeLen = 2;
		scanf("%s%s", A, B);
		strLen = 1;

		Alen = strlen(A);
		strcpy(powNum, A);
		for (int i = Alen - 1; i >= 0; i--)
		{
			A[Alen - i - 1] = powNum[i] - 48;
		}
		Blen = strlen(B);
		strcpy(powNum, B);
		for (int i = Blen - 1; i >= 0; i--)
		{
			B[Blen - i - 1] = powNum[i] - 48;
		}

		if (Alen == 1)
		{
			if (A[0] <= 9)
			{
				if (Blen == 1 && B[0] < 9)
				{
					count--;
				}
				count++;
			}
		}
		
		charPow(num,powNum);
		while (charCom(powNum, 2) <= 0)
		{
			/*
			for (int i = 0; i < strLen; i++)
			{
				num[i] += 48;
			}
			printf("%s\n", num);
			for (int i = 0; i < strLen; i++)
			{
				num[i] -= 48;
			}
			*/

			
			if (beforeLen < strLen)
			{
				//printf("%d\n", beforeLen);
				twoCheck = true;
				char str[101] = "";
				str[0] = 2;
				str[beforeLen - 1] = 2;
				//charPow(str, powNum);
				if (charPow(str, powNum) && charCom(powNum, 1) >= 0 && charCom(powNum, 2) <= 0)
				{
							/*for (int i = 0; i < beforeLen * 2 - 1; i++)
							{
								powNum[i] += 48;
							}*/
					//printf("%s %s %d %d\n", str, powNum, strLen, count);
					//printf("\"%s\",\n", powNum);
							/*for (int i = 0; i < beforeLen; i++)
							{
								str[i] -= 48;
							}*/
					count++;
					if (beforeLen % 2 == 1)
					{
						str[beforeLen / 2] = 1;
						//charPow(str, powNum);
						if (charPow(str, powNum) && charCom(powNum, 2) <= 0)
						{
							/*for (int i = 0; i < beforeLen * 2 - 1; i++)
							{
								powNum[i] += 48;
							}*/
							//printf("%s %s %d %d\n", str, powNum, strLen, count);
					//printf("\"%s\",\n", powNum);
							/*for (int i = 0; i < beforeLen; i++)
							{
								str[i] -= 48;
							}*/
							count++;
						}
					}
				}
				beforeLen = strLen;
				twoCheck = false;
			}

			//charPow(num, powNum);
			if (charPow(num, powNum) && charCom(powNum, 1) >= 0 && charCom(powNum, 2) <= 0)
			{
				//if (isPalin(powNum, 2))
				//{
				/*for (int i = 0; i < strLen * 2 - 1; i++)
				{
				powNum[i] += 48;
				}*/
				//printf("%s %s %d %d\n", num, powNum, strLen, count);
				//printf("\"%s\",\n", powNum);
				/*for (int i = 0; i < strLen; i++)
				{
				num[i] -= 48;
				}*/
				count++;
				//}
			}
			if (strLen % 2 == 1 && num[strLen / 2] == 1)
			{
				num[strLen / 2] = 2;
				//charPow(num, powNum);
				if (charPow(num, powNum) && charCom(powNum, 1) >= 0 && charCom(powNum, 2) <= 0)
				{
					//if (isPalin(powNum, 2))
					//{
					/*for (int i = 0; i < strLen * 2 - 1; i++)
					{
					powNum[i] += 48;
					}*/
					//printf("%s %s %d %d\n", num, powNum, strLen, count);
				//printf("\"%s\",\n", powNum);
					/*for (int i = 0; i < strLen; i++)
					{
					num[i] -= 48;
					}*/
					count++;
					//}
				}
				num[strLen / 2] = 1;
			}
				

			charPlus(num);
		}
			if (beforeLen < strLen)
			{
				//printf("%d\n", beforeLen);
				twoCheck = true;
				char str[101] = "";
				str[0] = 2;
				str[beforeLen - 1] = 2;
				//charPow(str, powNum);
				if (charPow(str, powNum) && charCom(powNum, 1) >= 0 && charCom(powNum, 2) <= 0)
				{
							/*for (int i = 0; i < beforeLen * 2 - 1; i++)
							{
								powNum[i] += 48;
							}*/
					//printf("%s %s %d %d\n", str, powNum, strLen, count);
					//printf("\"%s\",\n", powNum);
							/*for (int i = 0; i < beforeLen; i++)
							{
								str[i] -= 48;
							}*/
					count++;
					if (beforeLen % 2 == 1)
					{
						str[beforeLen / 2] = 1;
						//charPow(str, powNum);
						if (charPow(str, powNum) && charCom(powNum, 2) <= 0)
						{
							/*for (int i = 0; i < beforeLen * 2 - 1; i++)
							{
								powNum[i] += 48;
							}*/
					//printf("%s %s %d %d\n", str, powNum, strLen, count);
					//printf("\"%s\",\n", powNum);
							/*for (int i = 0; i < beforeLen; i++)
							{
								str[i] -= 48;
							}*/
							count++;
						}
					}
				}
				beforeLen = strLen;
				twoCheck = false;
			}


		printf("Case #%d: %d\n", testN, count);
	}
}