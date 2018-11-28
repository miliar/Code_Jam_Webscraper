#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main() 
{
	int t;
	scanf("%d\n", &t);
	for (int i = 1; i <= t; i++) 
	{
		char str[110];
		scanf("%s", str);
		int n = strlen(str);
		int left = 0;
		int right = n;
		while ((right > 0) && (str[right - 1] == '+')) { right--; }
		int count = 0;
		bool flipped = 0;
		while (left < right) 
		{
			if (!flipped) 
			{
				int ptr = left;
				bool flippedTopPlusPancakes = false;
				while ((ptr < right) && (str[ptr] == '+')) 
				{
					ptr++;
					flippedTopPlusPancakes = true;
				}
				while ((ptr < right) && (str[ptr] == '-')) 
				{
					ptr++;
				}
				left = ptr;
				if (flippedTopPlusPancakes) 
				{
					count++; 
				}
				count++;
				flipped = true;
			} 
			else 
			{
				int ptr = right - 1;
				bool flippedTopPlusPancakes = false;
				while ((ptr >= left) && (str[ptr] == '-')) 
				{
					ptr--;
					flippedTopPlusPancakes = true;
				}
				while ((ptr >= left) && (str[ptr] == '+')) 
				{
					ptr--;
				}
				right = ptr + 1;
				if (flippedTopPlusPancakes) 
				{
					count++; 
				}
				count++;
				flipped = false;
			}
		}
		printf("Case #%d: %d\n", i, count);
	}
	return 0;
}