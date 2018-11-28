#include<iostream>
#include<fstream>
#include<string>

void main()
{
	std::streambuf *coutbuf = std::cout.rdbuf();
	std::streambuf *cinbuf = std::cin.rdbuf();

	std::ofstream out("Boutputfile0.out");
	std::ifstream in("B-small-attempt0.in");

	//Read from infile.txt using std::std::cin
	std::cin.rdbuf(in.rdbuf());

	//Write to outfile.txt through std::cout
	std::cout.rdbuf(out.rdbuf());

	int noOfTestCases, n=0;
	std::cin>>noOfTestCases;
	while(n!=noOfTestCases)
	{
		n++;
		unsigned int a,b,k;
		int count = 0;
		std::cin>>a>>b>>k;

		for(int i=0; i<a; i++)
		{
			for(int j =0; j<b; j++)
			{
				if( (i & j) < k)
				{
					count++;
				}
			}
		}
		std::cout<<"Case #"<<n<<": "<<count<<std::endl;
	
	}

	//Restore back.
	std::cin.rdbuf(cinbuf);
	std::cout.rdbuf(coutbuf);
}