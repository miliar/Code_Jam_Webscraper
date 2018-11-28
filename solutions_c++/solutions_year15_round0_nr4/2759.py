#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <bitset>
using namespace std;

bool solve(long Xi, long Ri, long Ci)
{
	if (Ri == 1 && Ci == 1)
	{
		if (Xi == 1) return true;
	}

	if ((Ri == 1 && Ci == 2) || (Ri == 2 && Ci == 1))
	{
		if (Xi <= 2)	return true;
	}

	if (Xi * 2 > Ri*Ci)		return false;
	if (Ri*Ci % Xi != 0)	return false;

	if (Ri == 1 || Ci == 1)
	{
		if (Xi > 3)
			return false;
		else
			return true;
	}
	else	if (Ri == 2 || Ci == 2)
	{
		if (Xi == 4)
			return false;
		else
			return true;
	}
	return true;
	/*
	else	if (Ri == 3 || Ci == 3)
	{
		if (Ri == 4 || Ci == 4)
		{
			if (Xi == 4)
				return false;
			else
				return true;
		}
		return true;//3*3
	}
	else//4*4
	{
		if (Xi == 4)
			return false;
		else
			return true;
	}
	*/
}
int main()
{
	long T; cin >> T;
	vector<long> X(T);
	vector<long> R(T);
	vector<long> C(T);

	for (long i = 0; i < T; i++)
	{
		cin >> X[i] >> R[i] >> C[i];
	}

	for (long i = 0; i < T; i++)
	{
		if (solve(X[i], R[i], C[i]))
			cout << "Case #" << (i + 1) << ": " << "GABRIEL" << endl;
		else
			cout << "Case #" << (i + 1) << ": " << "RICHARD" << endl;

	}
	return 0;
}
