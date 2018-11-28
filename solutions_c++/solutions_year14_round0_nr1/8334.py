#include<iostream>
#include<fstream>
#include<string>

void main()
{
std::streambuf *coutbuf = std::cout.rdbuf();
std::streambuf *cinbuf = std::cin.rdbuf();

std::ofstream out("outputfile1.out");
std::ifstream in("A-small-attempt1.in");

//Read from infile.txt using std::std::cin
std::cin.rdbuf(in.rdbuf());

//Write to outfile.txt through std::cout
std::cout.rdbuf(out.rdbuf());

int noOfTestCases, n=0;
std::cin>>noOfTestCases;
while(n!=noOfTestCases)
{
n++;

int A[4][4],B[4][4],C[4],D[4],a,b,i,j,count=0,answer=0;

std::cin>>a;
for(i=0;i<4;i++)
	for(j=0;j<4;j++)
		std::cin>>A[i][j];

std::cin>>b;
for(i=0;i<4;i++)
	for(j=0;j<4;j++)
		std::cin>>B[i][j];
for(j=0;j<4;j++)
		{
		C[j]=A[a-1][j];
		D[j]=B[b-1][j];
		}

for(i=0;i<4;i++)
	{
	for(j=0;j<4;j++)
	{
	if(C[i]==D[j])
		{
			count++;
			answer = C[i];
		}
	}
	}



switch(count)
{
case 1:
    std::cout<<"Case #"<<n<<": "<<answer<<std::endl;
    break;
case 0:
    std::cout<<"Case #"<<n<<": "<<"Volunteer cheated!"<<std::endl;
    break;
default:
    std::cout<<"Case #"<<n<<": "<<"Bad magician!"<<std::endl;
}
}

//Restore back.
std::cin.rdbuf(cinbuf);
std::cout.rdbuf(coutbuf);
}




