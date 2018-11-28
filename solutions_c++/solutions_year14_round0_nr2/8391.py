#include <iostream>
#include <fstream>
#include <iomanip>

void main()
{
std::streambuf *coutbuf = std::cout.rdbuf();
std::streambuf *cinbuf = std::cin.rdbuf();

std::ofstream out("B-large.out");
std::ifstream in("B-large.in");

//Read from infile.txt using std::std::cin
std::cin.rdbuf(in.rdbuf());

//Write to outfile.txt through std::cout
std::cout.rdbuf(out.rdbuf());

int noOfTestCases, n=0;
std::cin>>noOfTestCases;
while(n!=noOfTestCases)
{
	n++;
	double P,Q,a=2,C,F,X,s,sum=0.0, time=0.0;
	std::cin>>C>>F>>X;
	s=X/C;
	sum=C/a;
	do
	{
		P=C/a;
		Q=C/(F+a);
		sum+=Q;
		a+=F;
		if((P*s) <= ((Q*s)+P))
		{	
			time=sum+((P*(s-1))-Q);
			break;  
		}
	}while((P*s)>((Q*s)+P));

	std::cout<<"Case #"<<n<<": "<< std::setprecision (7) << std::fixed<< time <<std::endl;
}

//Restore back.
std::cin.rdbuf(cinbuf);
std::cout.rdbuf(coutbuf);
}