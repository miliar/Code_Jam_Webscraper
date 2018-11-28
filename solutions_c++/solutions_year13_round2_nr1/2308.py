#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <math.h>

using namespace std;

void mote_sort (int *mote, int amount)
{
	for (int j = amount; j > 1; --j)
	{
		for (int i = 0; i < j - 1; ++i)
		{
			if (mote[i] > mote [i+1])
			{
				int temp = mote[i];
				mote[i] = mote[i+1];
				mote[i+1] = temp;
			}
		}
	}
}

bool can_eat_next (int msize, int next)
{
	if (msize > next)
		return true;
	return false;
}

int inc_oper (int &msize, int next)
{
	int ocount = 0;

	while (msize <= next)
	{
		msize += msize-1;
		ocount++;
	}


	return ocount;
}

void print_mote (int mote[100], int amount)
{
	for (int i = 0; i < amount; ++i)
	{
		cout << mote[i] << " ";
	}
	cout << endl;
}


int oper_count (ifstream &fin, int msize, int amount)
{
	int mote[100];
	int ocount = 0, i, inc_count;

	for (i = 0; i < amount; ++i)
	{
		fin >> mote[i];
	}

	if (msize <= 1)
	{
		//getchar();
		return amount;
	}
	cout << "mote :";
	print_mote (mote, amount);

	mote_sort (mote, amount);
	cout << "mote :";
	print_mote (mote, amount);

	for (i = 0; i < amount; ++i)
	{
		if (can_eat_next (msize, mote[i]))
		{
			cout << "can eat next" << endl;
			msize += mote[i];
			cout << "msize " << msize << endl;
		}
		else
		{
			inc_count = inc_oper(msize, mote[i]);

			if (inc_count >= (amount - i))
			{
				//getchar();
				return ocount + (amount - i);
			}
			else
			{
				msize += mote[i];
				ocount += inc_count;
			}
			cout << "msize " << msize << endl;
		}
		cout << "ocount : " << ocount << endl;
	}


	//getchar();
	return ocount;
}

int main ()
{
	int tn, msize, amount;
	ifstream fin("testcase.txt");
	ofstream fout("result.txt");

	fin >> tn;
	cout << "tn: " << tn << endl;

	for (double i = 0; i < tn; ++i)
	{
		cout << "tn: " << tn << endl;
		fin >> msize;
		cout << "msize: " << msize <<endl;
		fin >> amount;
		cout << "amount: " << amount << endl;
		cout << "case " << i+1 <<endl;
		fout << "Case #" << i+1 << ": " << oper_count (fin, msize, amount) << endl;
		cout << endl;
	}

	fin.close();
	fout.close();

	cout << "test";
	//getchar();
	return 0;
}
