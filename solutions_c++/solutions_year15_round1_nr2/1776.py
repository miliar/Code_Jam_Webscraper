#include <algorithm>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

#define ul unsigned long
#define ull unsigned long long

using namespace std;

int compare_long (const void *a, const void *b)
{
	if (*((long*)a) < *((long*)b)) return -1;
	return 1;
}

int compare_int (const void *a, const void *b)
{
	if (*((int*)a) < *((int*)b)) return -1;
	return 1;
}

ul GCD(ul a, ul b)
{
	ul temp;
	if(a<b)
	{
		temp = a;
		a = b;
		b = temp;
	}
	if(b==0)
		return a;
	while(b != 0)
	{
		temp = b;
		b = a%b;
		a = temp;
	}
	return a;
}

template <typename T>
T exp(T a, T b)
{
    if(b==0)    return 1;
    else if(b==1)   return a;
    else if((b&1)==0)
        return exp(a*a, b/2);
    return a*exp(a, b-1);
}

//-----------------------------------------------------------

long M[1010], M_[1010];

long find_min (int B)
{
	long minn = 100010;
	for (int i=1 ; i<=B ; ++i)
		if (M[i] < minn)
			minn = M[i];
	return minn;
}

long LCM (long a, long b)
{
	return (a*b/GCD(a, b));
}

int lowest_pos (int B)
{
	long minn = 100010;
	int j=-1;
	for (int i=1 ; i<=B ; ++i)
		if (M[i] <= minn)
		{
			minn = M[i];
			j=i;
		}
	return j;
}

int main(int argc, char const *argv[])
{
	int T, t, B, i;
	long N, count, minn, lcm, summ, lp;
	bool done;
	ifstream fin;
	ofstream fout;

	fin.open("input.txt");
	fout.open("output.txt");

	t=0;
	fin >> T; cout << T;
	
	while (++t <= T)
	{
		fin >> B >> N;
		for (i=1 ; i<=B ; ++i)
		{
			fin >> M[i];
			M_[i] = M[i];	// save original
		}
		if (N<=B)
		{
			fout << "Case #" << t << ": " << N << "\n";
			cout << "Case #" << t << ": " << N << "\n";
			continue;
		}

		lp = lowest_pos (B);

		lcm = M[1];
		for (i=2 ; i<=B ; ++i)
		{
			lcm = LCM (lcm, M[i]);
		}
		cout << "lcm = " << lcm << "\n";
		summ = 0;
		for (i=1 ; i<=B ; ++i)
		{
			summ += lcm/M[i];
		}
		cout << "summ = " << summ << "\n";
		N = N%summ;
		
		if (N == 0)
		{
			fout << "Case #" << t << ": " << lp << "\n";
			cout << "Case #" << t << ": " << lp << "\n";
			continue;
		}
		if (N<=B)
		{
			fout << "Case #" << t << ": " << N << "\n";
			cout << "Case #" << t << ": " << N << "\n";
			continue;
		}
		//cout << "here\n";
		done = false;
		count = B;
		while (!done)
		{
		minn = find_min(B);
		for (i=1 ; i<=B ; ++i)
		{
			M[i] -= minn;
			if (M[i] == 0)
			{
				count++;
				M[i] = M_[i];
				if (count == N)
				{
					fout << "Case #" << t << ": " << i << "\n";
					cout << "Case #" << t << ": " << i << "\n";
					done = true;
					break;
				}
			}
		}
		}
	}
	// fout << "Case #" << t << ": " << N-maxx << "\n";
	fin.close();
	fout.close();
	return 0;
}