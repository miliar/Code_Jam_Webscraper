#include<iostream>
#include<fstream>
#include<string>
#include<stdlib.h>

void main()
{
		std::streambuf *coutbuf = std::cout.rdbuf();
	std::streambuf *cinbuf = std::cin.rdbuf();
	
	std::ofstream out("outputfile_large.out");
	std::ifstream in("A-large.in");
	
	//Read from infile.txt using std::std::cin
	std::cin.rdbuf(in.rdbuf());
	
	//Write to outfile.txt through std::cout
	std::cout.rdbuf(out.rdbuf());

	int noOfTestCases, num=0;
	std::cin>>noOfTestCases;
	while(num!=noOfTestCases)
	{
		num++;
		int n, i, eaten1 = 0, eaten2 = 0, curDiff = 0, maxDiff = 0;
		std::cin >> n;
		int *array = new int [n];

		for(i=0; i<n; i++)
		{
			std::cin>>array[i];
			if(i > 0)
			{
				if(array[i] < array[i-1])
				{
					curDiff = array[i-1] - array[i];
					eaten1+= curDiff;
					if(curDiff > maxDiff)
					{
						maxDiff = curDiff;
					}
				}
			}
		}
		int now = array[0];
		int carryover = 0;

		for(i=1; i<n; i++)
		{
			if (now <= maxDiff)
			{
				eaten2 += now;
				carryover = 0;
			}
			else
			{
				eaten2 += maxDiff;
				carryover = now-maxDiff ;
			}
			now = array[i];
		}

		delete [] array;

		std::cout<<"Case #"<<num<<": "<<eaten1<<" "<<eaten2<<std::endl;
	}

	//Restore back.
	std::cin.rdbuf(cinbuf);
	std::cout.rdbuf(coutbuf);


}