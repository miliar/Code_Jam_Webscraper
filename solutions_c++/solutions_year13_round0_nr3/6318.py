#include <iostream>
#include <cmath>
#include <sstream>
#include<fstream>

using namespace std;

bool isPalindrom(unsigned long long num)
{
	if(num>0 && num<10)
		return true;
	int len;
	stringstream ss;
	ss << num;
	string strNum	= ss.str();
	len			=  strNum.length();
	for(int i = 0 ; i< len/2 ; i++)
	{
		if(strNum[i] != strNum[len-1-i])
			return false;
	}
	return true;
}

int main()
{

	unsigned long long a,b;
	int count=0,iterate;
	ifstream in("in.txt");
	ofstream myfile;
	myfile.open ("out.txt");
	in>> iterate;
	in.get();
	int *out	= new int [iterate];
	for(int it = 0 ; it<iterate ; it++)
	{
		in>>a>>b;
		unsigned long long begin = sqrt(a);

		for(unsigned long long i = begin ; i*i<=b ; i++)
		{
			if(i*i>=a && i*i<=b && isPalindrom(i) == true && isPalindrom(i*i)==true)
			{
				count++;
				cout<<"case"<<it+1<<" :: "<<i<<" ---->  "<<i*i<<endl;
			}
		}

		myfile<<"Case #"<<it+1<<": "<<count<<endl;
		count=0;
	}
	system("pause");
	return 0 ;
}