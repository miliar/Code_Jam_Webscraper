#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
#include<functional>
#include<numeric>

using namespace std;

int main()
{
	int cases;
	cin >> cases;

	for(int i=1; i<=cases; i++)
	{
		long long size, complex, students;
		cin >> size >> complex >> students;

		long long total = size;
		for(int j=0; j<complex; j++)
		{
			total *= size;
		}
		total /= size;
		long long offset = total / size;

		cout << "Case #" << i << ": ";
		cerr << "(Total: " << total << ", offset:" << offset << ")";
		cerr << "K(" << size << ") complex(" << complex << ") students(" << students << ")";
		if(students < size)
		{
			cout << "IMPOSSIBLE";
		}
		else
		{
			cout << 1;
			for(int j=2; (j<=students) && (j<=size); j++)
			{
				cout << " " << j;
			}
/*			long long at = 1;
			cout << at;
			at += offset;
			long long suboffset = 1;
			at += suboffset;
			for(int j=1; (j<students) && (at <= total); j++)
			{
				cout << " " << at;
				at += offset;
				at += suboffset++;
			}
*/
		}
		cout << endl;

	}

	return 0;
}
