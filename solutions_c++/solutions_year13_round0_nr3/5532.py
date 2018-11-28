#include<iostream>
#include<string>
#include<fstream>
#include<sstream>
#include<cmath>
using namespace std ;



#define SIZE 100

inline string convert(double number )
{
	std::ostringstream oss;
	string the_original_one , number_reflected ;
	number_reflected="";
	int temp ; bool test = true ; int i = 0 ;
	temp=number;
	if(number/temp!=1)
		return "";

		oss<<number ;
		number_reflected += oss.str();
	return number_reflected;
	
}bool check(double number )
{
	string temp , number1="" ; int n ; bool test = true ; int i = 0 ;
	number1="" ;
	number1 = convert(number);
	temp=number1 ;
	n = number1.length();
	if(n==0)
		return false;
	while(test)
	{
		temp[n-1]=number1[i];
		i++; n--;
		if((i==number1.length()) || n==0)
			test=false ;
	}
	if(number1==temp)
		return true;
	else return false;
}
int main()
{
	int base =10 , T , S , E , Counter=0; string number,squared_number; bool test;
	ifstream filein("C-small-attempt0.in");
	ofstream fileout("output.txt");
	filein>>T;
	for (int i = 0; i < T; i++)
	{
		filein>>S>>E;
		for(float j = S; j<=E; j++)
		{
			if(check(j))
				if(check(sqrt(j)))
					Counter++;
		}
		fileout<<"Case #"<<i+1<<": "<<Counter<<endl;
		Counter=0;
	}
	return 0 ;
}