#include "MatchHead.h"

#ifdef LAWN
#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
using namespace std;


void shift(int a[] , int b[], int i , int m)
{
	int k , t;
	int bt;
    t = a[i];
	bt = b[i];
	k = 2 * i + 1;
    while (k < m)
    {
		if ((k < m - 1) && (a[k] < a[k+1])) k ++;
		if (t < a[k])
		{
			a[i] = a[k];
			b[i] = b[k];
			i = k;
			k = 2 * i + 1;
		}
		else break;
	}
	a[i] = t;
	b[i] = bt;
}

void heap(int a[] , int b[], int n)
{
	int i , k;
	for (i = n/2-1; i >= 0; i --)
		shift(a , b, i , n);
	for (i = n-1; i >= 1; i --)
	{
		k = a[0]; a[0] = a[i]; a[i] = k;
		k = b[0]; b[0] = b[i]; b[i] = k;
		shift(a , b, 0 , i);
	}
}


int main(int argc, char* argv[])
{
	ifstream in;
	ofstream out;
	in.open("B-large.in");
	out.open("B-large.out");

	string snum;
	getline(in,snum);
	int num;
	sscanf(snum.c_str(),"%d", &num);

	int result;

	for(int l = 0; l < num; l ++)
	{
		result = 2;
		string str;
		getline(in, str);
		int ln,lm;
		sscanf(str.c_str(), "%d %d", &ln, & lm);
		int max;
		if(lm > ln)max = lm;
		else max = ln;
		int *not = new int[max];
		int *abd;
		abd = new int[ln*lm];
		int *board;
		board = new int[ln*lm];
		int *idx;
		idx = new int[ln*lm];
		for(int i = 0; i < ln * lm; i ++)
			idx[i] = i;
		for(int i = 0; i < ln; i ++)
		{
			getline(in, str);
			int j = 0;
			int k = 0;
			int p = 0;
			while(j < str.size())
			{
				if(str[j] != ' ')
				{
					k = 10 * k + str[j] - '0';
				}
				else
				{
					abd[i * lm + p] = k;
					board[i * lm + p] = k;
					k = 0;
					p ++;
				}
				j ++;
			}
			abd[i * lm + p] = k;
			board[i * lm + p] = k;
		}

		heap(abd, idx, ln*lm);

		//for(int i = 0; i < ln; i ++)
		//{
		//	for( int j = 0; j < lm; j ++)
		//	{
		//		out << board[i * lm + j] << " ";
		//	}
		//	out << endl;
		//}
		//for(int i = 0; i < ln; i ++)
		//{
		//	for( int j = 0; j < lm; j ++)
		//	{
		//		out << idx[i * lm + j] << " ";
		//	}
		//	out << endl;
		//}

		for(int i = 0; i < ln * lm; i ++)
		{
			result = 2;
			if(abd[idx[i]] == -1)continue;
			int idxn,idxm;
			int cnt = 0;
			idxn = idx[i] / lm;
			idxm = idx[i] % lm;

			for(int j = 0; j < lm; j ++)
			{
				if(board[idxn * lm + j] == board[idx[i]])
				{
					not[cnt ++] = idxn * lm + j;
				}
				if(board[idxn * lm + j] > board[idx[i]])
				{
					result --;
					break;
				}
			}
			if(result == 2)
			{
				for(int j = 0; j < cnt; j ++)
				{
					abd[not[j]] = -1;
				}
			}

			cnt = 0;
			for(int j = 0; j < ln; j ++)
			{
				if(board[j * lm + idxm] == board[idx[i]])
				{
					not[cnt ++] = j * lm + idxm;
				}
				if(board[j * lm + idxm] > board[idx[i]])
				{
					result --;
					break;
				}
			}
			if(result == 1)
			{
				for(int j = 0; j < cnt; j ++)
				{
					abd[not[j]] = -1;
				}
			}

			if(result == 0)break;
		}
		if(result != 0)
			out << "Case #" << l+1 << ": YES" << endl;
		else
			out << "Case #" << l+1 << ": NO" << endl;
		delete not;
		delete abd;
		delete board;
		delete idx;
	}

	in.close();
	out.close();
	return 0;
}


#endif