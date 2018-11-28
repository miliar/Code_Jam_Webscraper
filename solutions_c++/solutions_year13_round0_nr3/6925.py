#include<iostream>
#include<list>
#include <fstream>
#include <string>
using namespace std;
//const double long big = 100000000000000;
int numDigits(int num)
{
    int digits = 0;
    while (num) {
        num /= 10;
        digits++;
    }
    return digits;
}
bool ispalindrome(int num)
{

	int dig = pow(10,numDigits(num)-1);
	//for(int i=numDigits(num)/2;i>0;--i)
	while(num)
	{
		if(num/dig != num%10)
		{
			return false;
		}
		num = num%dig;
		dig/=100;
		num=num/10;
	}
	return true;
}
void main(char** argv)
{
	int arr [1001]={0};
	for(int i=1;i<34;++i)
	{
		int a = pow(i,2);
		if(ispalindrome(i) && ispalindrome(a))
		{
			arr[a]=1;
		}
	}
	int linecount = 0 ;
   string line ;
   ifstream *infile = new ifstream("C:\\Users\\Amichai\\Desktop\\a.txt");
   ofstream *outfile = new ofstream("C:\\Users\\Amichai\\Desktop\\b.txt");
   int amount;
   getline(*infile ,line);
   while (getline(*infile , line )) {
		  amount=0;
		  char* tline=new char[100];
		  strcpy(tline, line.c_str());
		  int a = atoi(strtok(tline, " "));
		  int b = atoi(strtok(NULL, " "));
		  for(int i=a;i<=b;++i)
		  {amount+=arr[i];}
		  (*outfile) << "Case #"<<linecount+1 << ": " << amount << '\n' ;
	 linecount++ ;
      }
	system("pause");
}