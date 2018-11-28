# include <fstream>
# include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

fstream fpIn,fpOut;

bool checkPalindrome(int n)
{
	int num = n;
	vector<int> orig,rev;
	while(num)
	{
		orig.push_back(num%10);
		num = num/10;
	}

    //copy orig to rev
	rev.resize(orig.size()) ;
	std::copy(orig.begin(), orig.end(), rev.begin()) ;

	//reverse orig
	std::reverse(orig.begin(),orig.end());

	//compare orig and rev
	if( orig == rev )
		return true;
	else
		return false;
}

bool fairAndSquare(int n)
{
	double d_sqrtn = std::sqrt(n);
	int i_sqrtn = d_sqrtn;
	
	if(i_sqrtn != d_sqrtn)
		return false;

	//check if number is a palindrome and check if it's root is a palindrome
	if( checkPalindrome(n) && checkPalindrome(i_sqrtn) )
		return true;
	else
		return false;

}


void readFile()
{
    int numOfTestCases;
	int start=-1,end=-1,count=0;

	fpIn.open("C:\\Users\\pmalik\\Desktop\\C-small-attempt0.in",ios::in);
	fpOut.open("C:\\Users\\pmalik\\Desktop\\fairnsquareout.txt", ios::out);

	fpIn>>numOfTestCases;

	for(int t=1;t<=numOfTestCases;t++)
	{
		fpIn>>start>>end;
		count=0;

		for(int i=start;i<=end;i++)
		{
			if( fairAndSquare(i) )
				count++;
		}

		fpOut<<"Case #"<<t<<": "<<count;
		
		if(t!=numOfTestCases)
		    fpOut<<"\n";

	
	}
    
	//close files
	fpIn.close();
	fpOut.close();
}


int main()
{
	readFile();

	char ch;
	cin>>ch;
	return 0;
}