// code_jam_3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string.h>
#include <malloc.h>

char file_input[] = "C-small-attempt0.in";
char file_output[] = "output.ou";

FILE *fin, *fout;

int testcase_number;

char under_bound[201];
char upper_bound[201];

char temp_multiplier[201];

char result[201];

void add_string(char *a, char *b, char *tong);

int mul(char a, int b)
{

	return (a-0x30)*b;
}

void multi(char *a, char b, char *tich)
{
	int int_b = b - 0x30;
	int size_a = strlen(a);
	int remainder = 0;
	int temp = 0;

	for(int i = 0; i < size_a; i++)
	{
		temp = mul(a[i], int_b) + remainder; 
		remainder = temp / 10;
		temp = temp % 10;
		tich[i] = temp + 0x30;
	}

	if (remainder != 0)
	{
		tich[size_a] = remainder + 0x30;
	}
}

void pow2(char *a, char *tich)
{
	int size_a = strlen(a);
	char temp_string_1[201];
	char temp_string_2[201];
	
	memset(temp_string_2, 0x0, 201);
	memset(temp_string_1, 0x0, 201);

	for (int i = 0; i < size_a; i++)
	{
		multi(a, a[i], temp_string_1);
		memset(temp_string_2, 0x0, 201);
		memset(temp_string_2, 0x30, i);
		memcpy(temp_string_2 + i, temp_string_1, strlen(temp_string_1));
		add_string(tich, temp_string_2, tich);
	}

}


bool IsPando(char *a)
{
	int size_a = strlen(a);

	for (int i = 0; i < size_a/2; i++)
	{
		if (a[i] != a[size_a - i - 1])
		{
			return false;
		}
	}
	return true;
}
int add_char(char a, char b)
{
	char temp_a, temp_b;

	if (a < 0x30) 
	{
		temp_a = 0x30;
	}
	else
	{
		temp_a = a;
	}
	if (b < 0x30) temp_b = 0x30;
	else
	{
		temp_b = b;
	}

	return (temp_a - 0x30) + (temp_b - 0x30);
}

void add_string(char *a, char *b, char *tong)
{
	int temp = 0;
	int size_a = strlen(a);
	int size_b = strlen(b);
	char *b1 = NULL;
	int remainder = 0;
	int k = size_a >= size_b ? size_a : size_b;

	b1 = (char *)malloc(k);
	memset(b1, 0x30, k);
	if (size_a >= size_b)
	{
		memcpy(b1, a, size_a);
		
		for (int i = 0; i < k; i++)
		{
			temp = add_char(b1[i], b[i]) + remainder;
			remainder = temp / 10;
			temp = temp % 10;
			tong[i] = temp + 0x30;
		}

		if (remainder != 0)
		{
			tong[k] = remainder + 0x30;
		}
	}
	else
	{
		memcpy(b1, b, size_b);
		for (int i = 0; i < k; i++)
		{
			temp = add_char(b1[i], a[i]) + remainder;
			remainder = temp / 10;
			temp = temp % 10;
			tong[i] = temp + 0x30;
		}

		if (remainder != 0)
		{
			tong[k] = remainder + 0x30;
		}
	}
	free(b1);
	
}

void add(char *a, int b)
{
	int size_a = strlen(a);
	int remainder = 0;
	
	if (a[0] == 0x00)
	{
		a[0] = 0x30;
	}
	int temp_int = a[0] - 0x30;

	temp_int = temp_int + b;

	remainder = temp_int / 10;
	temp_int = temp_int % 10;

	a[0] = temp_int + 0x30;
	
	for (int i = 1; i < size_a; i++)
	{
		temp_int = a[i] - 0x30;

		temp_int = temp_int + remainder;

		remainder = temp_int / 10;

		temp_int = temp_int % 10;

		a[i] = temp_int + 0x30;
	}

	if (remainder != 0)
	{
		if (a[size_a] < 0x30)
		{
			a[size_a] = 0x30;
		}
		temp_int = a[size_a] - 0x30;

		temp_int = temp_int + remainder;

		a[size_a] = temp_int + 0x30;
	}

}

// a > b ????
int greater(char *a, char *b)
{
	int size_a = strlen(a);
	int size_b = strlen(b);

	if (strlen(a) > strlen(b)) 
	{
		return 1;
	}
	else if (strlen(a) < strlen(b)) 
	{
		return -1;
	}
	else
	{
		for (int i = 0; i < size_a; i++)
		{
			if (a[size_a - i - 1] > b[size_a - i - 1])
			{
				return 1;
			}
			else if (a[size_a - i - 1] < b[size_a - i - 1])
			{
				return -1;
			}
		}
	}

	return 0;		// 2 so bang nhau
}

void reverse_string(char *a)
{
	int size_a = strlen(a);
	int size = strlen(a) / 2;
	char temp;

	for (int i = 0; i < size; i++)
	{
		temp = a[i];
		a[i] = a[size_a - i - 1];
		a[size_a - i - 1] = temp;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	int i, j, ii = 0;
	int max_height = 0;

	fin = fopen(file_input, "r");
	fout = fopen(file_output, "w");

	if ( (fin == NULL) || (fout == NULL) )
	{
		printf("ERROR in open file!");
		return 0;
	}

	fscanf(fin, "%d \n", &testcase_number);
	
	char count_var[201];
	bool out_bound = false;
	char square[201];
	for (ii = 0; ii < testcase_number; ii++)
	{
		memset(under_bound, 0x0, sizeof(under_bound));
		memset(upper_bound, 0x0, sizeof(upper_bound));

		fscanf(fin, "%s %s \n", under_bound, upper_bound);

		reverse_string(under_bound);
		reverse_string(upper_bound);

		memset(result, 0x0, sizeof(result));
		memset(count_var, 0x0, sizeof(count_var));
		out_bound = false;

		while (!out_bound)
		{
			add(count_var, 1);
			if (IsPando(count_var))
			{
				memset(square, 0, 201);
				pow2(count_var, square);
				if (greater(upper_bound, square) < 0)
				{
					out_bound = true;
				}
				else if ((IsPando(square)) && (greater(square, under_bound) >= 0) && (greater(upper_bound, square) >= 0) )
				{
					add(result, 1);
				}
			}
			
		}
		
		reverse_string(result);
		if (strlen(result) == 0)
		{
			fprintf(fout, "Case #%d: %s \n", ii+1, "0");
		}
		else
		{
			fprintf(fout, "Case #%d: %s \n", ii+1, result);
		}
		
	}
	
	fclose(fin);
	fclose(fout);
	return 0;
}

