
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

#define ARR_SZ 4

using namespace std;

int testcases = 0;
char ***arr = NULL;

void readfile(const char* filename)
{
	int idx = 0;
	FILE *file = fopen ( filename, "r" );

	if ( file != NULL )
	{
		char line [ 128 ]; /* or other suitable maximum line size */
		if ( fgets ( line, sizeof line, file ) == NULL ) /* read a line */
		{
			perror("End of File");
		}
		sscanf(line,"%d",&testcases);
		//printf("Test Cases: %d\n",testcases);
		//getchar();
		
		arr = (char***) malloc(sizeof(char**)*testcases);
		if(arr == NULL )
		{
			printf("allocation failure\n");
			exit(1);
		}
		
		for(idx=0;idx<testcases;idx++)
		{
			arr[idx] = (char**) malloc(sizeof(char*)*ARR_SZ);
		}

		for(idx=0;idx<testcases;idx++)
		{
			for(int kdx=0;kdx<ARR_SZ;kdx++)
			{
				arr[idx][kdx] = (char*) malloc(sizeof(char)*ARR_SZ);
			}
		}



		idx = 0;
		int caseid = 0;
		char a,b,c,d;
		while ( fgets ( line, sizeof line, file ) != NULL ) /* read a line */
		{
			if(strlen(line)<5)
			{
				//cout << endl;
				++caseid;
				idx = 0;
				continue;
			}
			sscanf(line,"%c %c %c %c",&a,&b,&c,&d);
			//cout << a << b << c << d << endl;
			arr[caseid][idx][0] = a;
			arr[caseid][idx][1] = b;
			arr[caseid][idx][2] = c;
			arr[caseid][idx][3] = d;
			++idx;
		}
		fclose ( file );
	}
	else
	{
	perror ( filename ); /* why didn't the file open? */
	}
}

void display()
{

	for(int tid=0;tid<testcases;tid++)
	{
		cout << "Case:" << tid+1 << endl;

		for(int idx=0;idx<ARR_SZ;idx++)
		{
			for(int kdx=0;kdx<ARR_SZ;kdx++)
			{
				cout << arr[tid][idx][kdx];
			}
			cout << endl;
		}

	}
}

void tttt()
{
	int fail1 = 0;
	int fail2 = 0;
	int fail3 = 0;
	int fail4 = 0;

	for(int tid=0;tid<testcases;tid++)
	{
		fail1 = 0;
		fail2 = 0;
		fail3 = 0;
		fail4 = 0;

		cout << "Case #" << tid+1 << ": " << flush;
		//cout << "row loop" << endl;
		for(int idx=0;idx<ARR_SZ;idx++)
		{
			fail1 = 0;
			for(int kdx=1;kdx<ARR_SZ;kdx++)
			{
				//cout << "arr[" << tid << "][" << idx << "][0]:" << arr[tid][idx][0] << "  ";
				//cout << "arr[" << tid << "][" << idx << "][" << kdx << "]:" << arr[tid][idx][kdx] << endl;
				if( arr[tid][idx][0] != arr[tid][idx][kdx] && arr[tid][0][kdx] != 'T')
				{
					//cout << "fail1" << endl;
					fail1 = 1;
					break;
				}

			}
			if(fail1 == 0 && arr[tid][idx][0] == '.')
			{
				fail1 = 1;
			}

			if(fail1 == 0 && arr[tid][idx][0] != '.')
			{
				//cout << "1" << endl;
				cout << arr[tid][idx][0] << " won" << endl;
				break;
			}
		}

		if(fail1 == 1)
		{
			//cout << "column loop" << endl;
			for(int idx=0;idx<ARR_SZ;idx++)
			{
				fail2 = 0;
				for(int kdx=1;kdx<ARR_SZ;kdx++)
				{
					//cout << "arr[" << tid << "][0][" << idx << "]:" << arr[tid][0][idx] << "  ";
					//cout << "arr[" << tid << "][" << kdx << "][" << idx << "]:" << arr[tid][kdx][idx] << endl;
					if( arr[tid][0][idx] != arr[tid][kdx][idx] && arr[tid][kdx][idx] != 'T' )
					{
						fail2 = 1;
						break;
					}
				}
				if(fail2 == 0 && arr[tid][0][idx] == '.')
				{
					fail2 = 1;
				}
				if(fail2 == 0 && arr[tid][0][idx] != '.')
				{
					//cout << "2" << endl;
					cout << arr[tid][0][idx] << " won" << endl;
					break;
				}
			}
		}

		if(fail2 == 1)
		{

			//cout << "first diagonal loop" << endl;
			for(int idx=1;idx<ARR_SZ;idx++)
			{
				//cout << "arr[" << tid << "][" << idx << "][" << idx << "]:" << arr[tid][idx][idx] << endl;
				if(arr[tid][idx][idx] != arr[tid][0][0] && arr[tid][idx][idx] != 'T')
				{
					fail3 = 1;
					break;
				}
			}
			if(fail3 == 0 && arr[tid][0][0] == '.')
			{
				fail3 = 1;
			}

			if(fail3 == 0 && arr[tid][0][0] != '.')
			{
				//cout << "3" << endl;
				cout << arr[tid][0][0] << " won" << endl;
				//break;
			}
		}
		
		if(fail3 == 1)
		{
			//cout << "second diagonal loop" << endl;
			//cout << "arr[" << tid << "][0][3]:" << arr[tid][0][3] << endl;
			for(int idx=1,kdx=ARR_SZ-2;idx<ARR_SZ;idx++,kdx--)
			{
				//cout << "arr[" << tid << "][" << idx << "][" << kdx << "]:" << arr[tid][idx][kdx] << endl;
				if(arr[tid][idx][kdx] != arr[tid][0][3] && arr[tid][idx][kdx] != 'T')
				{
					fail4 = 1;
					break;
				}
			}
			if(fail4 == 0 && arr[tid][0][3] == '.')
			{
				fail4 = 1;
			}
			if(fail4 == 0 && arr[tid][0][3] != '.')
			{
				//cout << "4" << endl;
				cout << arr[tid][0][3] << " won" << endl;
			}
		}

		if(fail1 == 1 && fail2 == 1 && fail3 == 1 && fail4 == 1)
		{

			//cout << "all fail loop" << endl;
			int dot = 0;
			for(int idx=0;idx<ARR_SZ;idx++)
			{
				for(int kdx=0;kdx<ARR_SZ;kdx++)
				{
					if(arr[tid][idx][kdx] == '.')
					{
						dot = 1;
						cout << "Game has not completed" << endl;
						break;
					}
				}
				if(dot)
				{
					break;
				}
			}
			if(dot == 0)
			{
				cout << "Draw" << endl;
			}
		}
	}
}

int main( int argc, char** argv)
{
	char* filename = NULL;
	
	if(argc != 2)
	{
		printf("File not specified.\n");
		exit(1);
	}

	filename = argv[1];
	readfile(filename);
	//display();	
	tttt();

	return 0;
}

