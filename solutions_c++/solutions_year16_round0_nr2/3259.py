// prob1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <cassert>
#include <string>
using namespace std;
#define _CRT_SECURE_NO_WARNINGS
bool pan_cakes[102] = { 0 };
unsigned int total_pan_cakes = 0;

void clear_db()
{
	unsigned int maxT = sizeof(pan_cakes) / sizeof(pan_cakes[0]);
	for (unsigned int i = 0; i < maxT; ++i)
	{
		pan_cakes[i] = false;
	}
	total_pan_cakes = 0;
}

void init_pc(string pc_string)
{
	clear_db();

	total_pan_cakes = pc_string.length();
	for (unsigned int i = 0; i < total_pan_cakes; ++i)
	{
		if (pc_string[i] == '+')
		{
			pan_cakes[i] = true;
		}
	}
}

void flip(int start, int end)
{
	bool temp;
	int start1 = start;
	int end1 = end;
	while (start1 < end1)
	{
		temp = pan_cakes[start1];
		pan_cakes[start1] = pan_cakes[end1];
		pan_cakes[end1] = temp;
		start1++;
		end1--;
	}
	for (unsigned int i = start; i <= end; ++i)
	{
		pan_cakes[i] = !pan_cakes[i];
	}
}

unsigned int get_end()
{

	for (unsigned int i = total_pan_cakes - 1; i >= 0; --i)
	{
		if (false == pan_cakes[i])
		{
			return i;
		}
	}
	return 0;
}

bool is_ok()
{
	for (unsigned int i = 0; i < total_pan_cakes; ++i)
	{
		if (false == pan_cakes[i])
		{
			return false;
		}
	}
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* in = NULL;
	FILE* out = NULL;
	errno_t fin = freopen_s(&in, "B-large.in", "r", stdin);
	assert(0x0 == fin);
	errno_t fout = freopen_s(&out, "B-large.out", "w", stdout);
	assert(0x0 == fout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		string pc_status;
		cin >> pc_status;
		init_pc(pc_status);
		unsigned long long result = 0;
		while (false == is_ok())
		{
			switch (pan_cakes[0])
			{
				case false:
					{
						unsigned int end = get_end();
						flip(0, end);
					}
					break;

				case true:
					{
						unsigned int i;
						for (i = 1; i < total_pan_cakes; i++)
						{
							if (false == pan_cakes[i])
							{
								break;
							}
						}
						flip(0, i - 1);
					}
					break;
			}
			result++;
		}
		cout << "Case #" << t << ": " << result << endl;
	}
	return 0;
}

