#include<iostream>
#include<fstream>
#include<string>
#include<stdlib.h>

void main()
{
	std::streambuf *coutbuf = std::cout.rdbuf();
	std::streambuf *cinbuf = std::cin.rdbuf();
	
	std::ofstream out("outputfile.out");
	std::ifstream in("D-small-attempt0.in");
	
	//Read from infile.txt using std::std::cin
	std::cin.rdbuf(in.rdbuf());
	
	//Write to outfile.txt through std::cout
	std::cout.rdbuf(out.rdbuf());

	int nTotal, n=0;
	std::cin>>nTotal;
	while(n!=nTotal)
	{
		n++;

		std::cout<<"Case #"<<n<<": ";

		int x,r,c;
		std::cin>>x>>r>>c;
		switch(x)
		{
		case 1: std::cout<<"GABRIEL";
			break;
		case 2: switch(r)
				{
			case 1:
				if(c==1||c==3)
						std::cout<<"RICHARD";
				else
						std::cout<<"GABRIEL";
					break;
			case 2: 
					std::cout<<"GABRIEL";
					break;
			case 3: if(c==1||c==3)
						std::cout<<"RICHARD";
					else
						std::cout<<"GABRIEL";
				break;
			case 4: std::cout<<"GABRIEL";
				break;

				}
				break;
			case 3: 
				switch(r)
					{
				case 1: std::cout<<"RICHARD";
						break;
				case 2: if(c==3)
								std::cout<<"GABRIEL";
						else
								std::cout<<"RICHARD";
						break;
				case 3: if(c==1)
								std::cout<<"RICHARD";
						else
								std::cout<<"GABRIEL";
						break;
				case 4: if(c==3)
								std::cout<<"GABRIEL";
						else
								std::cout<<"RICHARD";
						break;
					}
				break;
			case 4:		if(r==1||r==2)
								std::cout<<"RICHARD";
						else
								{
								
								if(r==3&&c==4)
										std::cout<<"GABRIEL";
								else if(r==3)
										std::cout<<"RICHARD";
								else if(r==4&&c==1)
										std::cout<<"RICHARD";
								else if(r==4&&c==2)
										std::cout<<"RICHARD";
								else if(r==4&&c==3)
										std::cout<<"GABRIEL";
								else if(r==4&&c==4)
										std::cout<<"GABRIEL";
								}
						break;
		}
		std::cout<<std::endl;
	}
}
