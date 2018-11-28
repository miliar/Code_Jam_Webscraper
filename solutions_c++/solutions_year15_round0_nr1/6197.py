#include<iostream>
#include<fstream>
#include<string>
#include<stdlib.h>

void main()
{
	std::streambuf *coutbuf = std::cout.rdbuf();
	std::streambuf *cinbuf = std::cin.rdbuf();
	
	std::ofstream out("outputfile.out");
	std::ifstream in("A-large.in");
	
	//Read from infile.txt using std::std::cin
	std::cin.rdbuf(in.rdbuf());
	
	//Write to outfile.txt through std::cout
	std::cout.rdbuf(out.rdbuf());

	int noOfTestCases, n=0;
	std::cin>>noOfTestCases;
	while(n!=noOfTestCases)
	{
		n++;

		int shyMax = 0, count=0, newAdd = 0;
		int i;
		std::string str;

		std::cin>>shyMax;
		std::cin>>str;

		for(i=0; (i<=shyMax) && (count < shyMax); i++)
		{
			int a = str.at(i) - '0';
			if(count < i && a > 0)
			{
				newAdd += i - count;
				count += (i - count);
			}
			count += a;
		}

		std::cout<<"Case #"<<n<<": "<<newAdd<<std::endl;
	}

	//Restore back.
	std::cin.rdbuf(cinbuf);
	std::cout.rdbuf(coutbuf);
}




