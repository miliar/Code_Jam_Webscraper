#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <cmath>
#include <vector>



using namespace std;




unsigned int numdigits(unsigned long long num)
{
	unsigned int result=1;
	while(num/10 != 0){
		num = num/10;
		result += 1;
	}
	return result;
}

unsigned long long mypower10(unsigned int n)
{
	unsigned long long result=1;
	for(unsigned int i=1;i<=n;i++)
			result *= 10;

	return result;

}

bool is_perfect_square(unsigned long long n, unsigned long long & root) {
    if (n < 0)
        return false;

    root=floor(sqrt(n));

    return n == root * root;
}

bool IsPalindrom(unsigned long long testnum)
{
	bool result = true;
	unsigned long long root = 0;
	stringstream tempsstream;
	string strtestnum;
	tempsstream << testnum;
	tempsstream >> strtestnum;
	unsigned int len = strtestnum.length();

	//check whether it is a palindrom
	for(unsigned int i=0;i<len/2;i++)
	{
		if(strtestnum[i]!=strtestnum[len-i-1])
		{
			result = false;
			break;
		}
	}
	
	return result;
}


bool IsFairSqaurePalindrom(unsigned long long testnum)
{
	bool result = true;
	bool IsSquarePalindrom = true;
	string endDigitInSquarePalindrom="14569";
	unsigned long long root = 0;
	stringstream tempsstream;
	string strtestnum;
	tempsstream << testnum;
	tempsstream >> strtestnum;
	unsigned int len = strtestnum.length();
	bool IsSquare = is_perfect_square(testnum, root);
	if(IsSquare) 	//is testnum a squared num?
	{
		//is testnum a palindrom?
		if(strtestnum[0]==strtestnum[len-1])
		{
			if(endDigitInSquarePalindrom.find(strtestnum[0])!=std::string::npos)
				{
					//check whether it is a palindrom
					for(unsigned int i=0;i<len/2;i++)
					{
						if(strtestnum[i]!=strtestnum[len-i-1])
						{
							IsSquarePalindrom = false;
							break;
						}
					}
				}
			else
			{
				IsSquarePalindrom = false;
			}

		}
		else
		{
			IsSquarePalindrom = false;
		}
	}
	else
		IsSquarePalindrom = false;

	if(IsSquarePalindrom)
		result = IsPalindrom(root);
	else
		result = false;

	return result;
}

unsigned long long check(unsigned long long A, unsigned long long B)
{
	unsigned long long numFairSquares = 0;
	
	unsigned long long testnum=A;
	for(;testnum<=B;testnum++)
	{
		if(IsFairSqaurePalindrom(testnum))
			numFairSquares++;
	}


	//unsigned int lnumdigits=numdigits(A);
	//unsigned int unumdigits=numdigits(B);
	//for(unsigned int digits=lnumdigits;digits<=unumdigits;digits++)
	//{
	//	if(digits!=2 && digits!=4 && digits!=8 && digits!=10 && digits!=14 && digits!=18 && digits!=20 && digits!=24 && digits!=30 && digits!=38 && digits!=40)
	//	{
	//		unsigned long long lower, upper;
	//		if(digits==lnumdigits)
	//			lower=A;
	//		else
	//			lower=mypower10(digits);
	//		if(digits==unumdigits)
	//			upper=B;
	//		else
	//			upper=mypower10(digits)-1;
	//		unsigned long long testnum=lower;
	//		for(;testnum<=upper;testnum++)
	//		{
	//			if(IsFairSqaurePalindrom(testnum))
	//				numFairSquares++;
	//		}
	//	}
	//}

		return numFairSquares;

}


int main()
{
	//ifstream infile1, infile2;
	//infile1.open("D:\C-small-attempt0-1.out");
	//infile2.open("D:\C-small-attempt0-0.out");

	//string line1, line2;
	//unsigned int totalline = 0;
	//vector<unsigned int> differentlines;
	//while(infile1.good() && infile2.good())
	//{
	//	totalline++;
	//	getline(infile1,line1);
	//	getline(infile2,line2);
	//	if(line1.compare(line2)!=0)
	//		differentlines.push_back(totalline);

	//}
	//cout<<"totalline: "<<totalline<<endl;
	////cout<<"The same: "<<differentlines.empty()<<endl;
	//if(!differentlines.empty())
	//	cout<<"Different lines:"<<endl;
	//{
	//	for(unsigned int i=0;i<differentlines.size();i++)
	//	{
	//		cout<<"line #: "<<differentlines[i]<<endl;
	//	}
	//}

	ifstream infile;
	ofstream outfile; 
	infile.open("D:\C-small-attempt1.in");
	outfile.open("D:\C-small-attempt1.out");

	if(!infile.is_open())
		cout<<"can not open input file"<<endl;
	if(!outfile.is_open())
		cout<<"can not open output file"<<endl;

	long numCases = 0;
	string aline;
	//get the number of cases
	getline(infile, aline);
	numCases = ::atol(aline.c_str());

	for(unsigned int i=1;i<=numCases;i++)
	{
		getline(infile, aline);
		stringstream alinestream;
		unsigned long long A;
		unsigned long long B;
		unsigned long long numFairSquares;
		string temp;
		alinestream << aline;
		alinestream >> temp;
		A=_strtoui64(temp.c_str(),NULL,10);
		alinestream >> temp;
		B=_strtoui64(temp.c_str(),NULL,10);
		
		numFairSquares=check(A,B);
		outfile<<"Case #"<<i<<": "<<numFairSquares<<endl;
		
	}

	infile.close();
	outfile.close();
	return 0;
}