
#if 1
#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

#define ZERO_MEM(x) memset(x, 0, sizeof(x));
#define UINT64  unsigned __int64

void main()
{
	ifstream fin("C-small-attempt0.in");
//	ifstream fin("input.txt");
	int cnt;
	fin >> cnt;

	int min, max;
	char num[128];
	char rnum[128];
	int res;
	ofstream fout("output.txt");
	for(int p=0; p<cnt; p++)
	{
		res = 0;
		fin >> min >> max;

		int start = sqrt((double)min);

		for(int i=sqrt((double)min); i*i<=max; i++)
		{
			if(i*i <min)
				continue;

			sprintf(num, "%d", i);
			sprintf(rnum, "%d", i);
			_strrev(rnum);
			if( _stricmp( num, rnum ) !=0 )
				continue;

			sprintf(num, "%d", i*i);
			sprintf(rnum, "%d", i*i);
			_strrev(rnum);
			if( _stricmp( num, rnum ) ==0 )
			{
				res++;
			}
		}



		cout << "Case #" << p+1 << ": " << res << endl;
		fout << "Case #" << p+1 << ": " << res << endl;
	}
}

#endif
