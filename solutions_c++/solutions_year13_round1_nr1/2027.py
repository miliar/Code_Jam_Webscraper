#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
	fstream file;

	file.open(argv[1], ios_base::in);

	if(file.is_open())
	{
		int itest_count = 0;
		file>>itest_count;
		char buffer[1024] = {0};
		file.getline(buffer, 1024);

		for(int itest=1; itest <= itest_count; itest++)
		{
			__int64 istart = 0;
			__int64 ipaint = 0;
			memset(buffer, 0, 1024);
			file.getline(buffer, 1024);
			char *ptemp = strchr(buffer, ' ');

			istart = _atoi64(buffer);
			ipaint = _atoi64(++ptemp);

			__int64 i = istart;
			__int64 icircles = 0;
			__int64 paint_req = 0;
			while(true)
			{
				__int64 inext = i+1;

				paint_req += (inext*inext - i*i);

				if(ipaint <= paint_req)
				{
					if(ipaint == paint_req)
					{
						icircles++;
					}
					break;
				}

				icircles++;
				i+=2;
			}

			printf("Case #%d: %I64u\n", itest, icircles);
		}
		file.close();
	}
	return 0;
}