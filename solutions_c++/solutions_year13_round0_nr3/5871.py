#include <iostream>
#include <fstream>
#include <sstream>
#include "strutils.h"

using namespace std;


bool isPalindrome(int sq)
{
	string check=itoa(sq);
	int len=check.length()+1;
	for(int i=0; i<(len/2); i++)
	{
		if(check[i]!=check[len-i-2])
			return false;
	}
	return true;
}

long int sqr(int num)
{
	return (num*num);
}

int main()
{
	ifstream input;
	ofstream output;
	input.open("C-small-attempt0.in");
	output.open("aglaya_output.in");
	
	cin.clear();
	input.seekg(0);

	string casenum;
	getline(input,casenum);
	int caseno=atoi(casenum);
	
	int keep[6]={1,4,9,121,484,7744};

	for(int cn=1; cn<=caseno; cn++)
	{
		string line;
		getline(input,line);
		istringstream nums(line);
		int count=0;
		long int min, max;
		nums >> min >> max;
		if(max<=10000 || min<=10000)
		{
			if(min==1)
			{
				for (int i=0; i<6; i++)
				{
					if(max>=keep[i])
						count++;
				}
			}
			else if(min>1 && min<=4)
			{
				for (int i=1; i<6; i++)
				{
					if(max>=keep[i])
						count++;
				}
			}
			else if(min>4 && min<=9)
			{
				for (int i=2; i<6; i++)
				{
					if(max>=keep[i])
						count++;
				}
			}
			else if(min>9 && min<=121)
			{
				for (int i=3; i<6; i++)
				{
					if(max>=keep[i])
						count++;
				}
			}
			else if(min>121 && min<=484)
			{
				for (int i=4; i<6; i++)
				{
					if(max>=keep[i])
						count++;
				}
			}
			else if(min>484 && min<=7744)
			{				
				if(max>=keep[5])
					count++;
			}
		}
		else if(min<1000000 || max>10000 && max<=1000000)
		{
			int newnum=0;
			for(int b=1; b<10; b++)
			{
				for(int o=0; o<10; o++)
				{
					newnum=b*100 + o*10 +b;
					if(newnum>=min)
					{
						if(isPalindrome(sqr(newnum)))
							count++;
					}
				}
			}
		}
		else if(min<=10000000000 || max>1000000 && max<=10000000000)
		{
			int newnum=0;
			for(int b=1; b<10; b++)
			{
				for(int o=0; o<10; o++)
				{
					newnum=b*1000 + o*100 + o*10 +b;
					if(newnum>=min)
					{
						if(isPalindrome(sqr(newnum)))
							count++;
					}
				}
			}
		}
		else if (min<=100000000000000 || max>10000000000 && max <=100000000000000)
		{
			for(int b=0; b<10; b++)
			{
				for (int i=0; i<10; i++)
				{
					for (int u=0; u<10; u++)
					{
						int newnum=b*10000 + i*1000 + u*100 + i*10 + b;
						if(newnum>=min)
						{
						if(isPalindrome(sqr(newnum)))
							count++;
						}
					}
				}
			}
		}
		output << "Case #" << cn << ": " << count << endl;
	}

	return 0;
}