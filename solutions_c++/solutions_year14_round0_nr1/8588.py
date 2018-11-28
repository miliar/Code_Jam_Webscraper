#include<iostream>
#include<fstream>
#include<string>

void main()
{
	std::cout<<"testing compilation";
	std::streambuf *coutbuf = std::cout.rdbuf();
	std::streambuf *cinbuf = std::cin.rdbuf(); 

	std::ofstream out("outfile.out");
	std::ifstream in("A-small-attempt0.in");

	//Read from infile.txt using std::cin
	std::cin.rdbuf(in.rdbuf());

	//Write to outfile.txt through std::cout 
	std::cout.rdbuf(out.rdbuf());   

	int noOfTestCases, n=0;
	std::cin>>noOfTestCases;

	while(n!=noOfTestCases)
	{
		n++;
		int a[4][4], b[4][4], c[4],d[4], i, j, row1, row2;
		int count=0, val=0;

		std::cin>>row1;
		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
			{
				std::cin>>a[i][j];
			}
		}
		std::cin>>row2;
		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
			{
				std::cin>>b[i][j];
			}
		}

		for(i = 0; i < 4; i++)
		{
			c[i]=a[row1-1][i];
			d[i]=b[row2-1][i];
		}

		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
			{
				if(c[i] == d[j])
				{
					val = c[i];
					count++;
				}
			}
		}

		switch(count)
		{
		case 1:
			std::cout<<"Case #"<<n<<": "<<val<<std::endl;
			break;
		case 0:
			std::cout<<"Case #"<<n<<": Volunteer cheated!"<<std::endl;
			break;
		default:
			std::cout<<"Case #"<<n<<": Bad magician!"<<std::endl;
		}
	}

    //Restore back.
    std::cin.rdbuf(cinbuf);   
    std::cout.rdbuf(coutbuf); 

}