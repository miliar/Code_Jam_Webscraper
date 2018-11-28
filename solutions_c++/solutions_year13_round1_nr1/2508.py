/*
 * main.cpp
 *
 *  Created on: 2013-4-27
 *      Author: chenjd
 */

#include <iostream>
#include <fstream>

#define File

#ifdef File
#define cin fin
#define cout fout
#endif

using namespace std;

int main()
{
#ifdef File
	ifstream fin("in.txt");
	ofstream fout("out.txt");
#endif
	int test_case;
	int test;
	cin >> test_case;
	for (test = 1; test <= test_case; test++)
	{
		long long in_r;
		long long paint;
		cin >> in_r >> paint;
		long long i;
		//		long long used_paint = 0;
		long long num_ring = 0;
		for (i = in_r + 1; paint >= 0; i += 2, num_ring++)
		{
			paint -= i * 2 - 1;
		}
		num_ring--;
		cout << "Case #" << test << ": " << num_ring << endl;
	}
#ifdef File
fin.close();
fout.close();
#endif
	return 0;
}

/*int test_case;
 int test;
 cin >> test_case;
 for (test = 1; test <= test_case; test++)
 {
 long long in_r;
 long long paint;
 cin >> in_r >> paint;
 //		long long first_ring_paint = 2 * in_r + 1;
 long long left = in_r + 1;
 long long right = 2000000000000000000/707106782;
 while ((2 * right - 1) % 4 != (2 * left - 1) % 4)
 right++;
 long long mid;
 while (left < right - 1)
 {
 mid = (left + right) / 2;
 if ((2 * mid - 1) * (mid - in_r) == paint)
 break;
 if ((2 * mid - 1) * (mid - in_r) > paint)
 right = mid - 1;
 else
 left = mid;
 }
 mid = (right + left) / 2;
 cout << "Case #" << test << ": " << mid - in_r << endl;
 }*/


