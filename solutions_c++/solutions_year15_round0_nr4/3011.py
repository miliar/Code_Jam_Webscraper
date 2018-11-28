#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string>

void main()
{
	std::streambuf *coutbuf = std::cout.rdbuf();
	std::streambuf *cinbuf = std::cin.rdbuf();
	
	std::ofstream out("outputfile.out");
	std::ifstream in("D-small-attempt1.in");
	
	//Read from infile.txt using std::std::cin
	std::cin.rdbuf(in.rdbuf());
	
	//Write to outfile.txt through std::cout
	std::cout.rdbuf(out.rdbuf());

	int noOfTestCases, n=0;
	std::cin>>noOfTestCases;
	while(n!=noOfTestCases)
	{
		int X,R,C;
		n++;

		std::cin>>X;
		std::cin>>R>>C;
		std::cout<<"Case #"<<n<<": ";

		switch(X)
		{
		case 1:
				std::cout<<"GABRIEL";
				break;
		case 2:
				if( (R==1 && C==1) || (R==3 && C==3) || (R==1 && C==3) || (R==3 && C==1) )
						std::cout<<"RICHARD";
				else 
						std::cout<<"GABRIEL";
				break;
		case 3:
				if( (R==1 && C==1) || (R==2 && C==2) || (R==1 && C==2) ||  (R==2 && C==1)|| (R==4 && C==4) || (R==2 && C==4) || (R==4 && C==2) || (R==1 && C==4) || (R==4 && C==1) || (R==1 &&C==3) || (R==3 && C==1))
						std::cout<<"RICHARD";
				else
						std::cout<<"GABRIEL";
				break;
		case 4:
				if(  ( (R==3 && C==4) || (R==4 && C==3) )|| (R==4 &&C==4))
						std::cout<<"GABRIEL";
				else
						std::cout<<"RICHARD";
				break;
		}
		std::cout<<std::endl;
	}

	//Restore back.
	std::cin.rdbuf(cinbuf);
	std::cout.rdbuf(coutbuf);

}
		
