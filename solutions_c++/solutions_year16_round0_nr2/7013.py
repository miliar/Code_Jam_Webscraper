#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream myIn;
	myIn.open("C:\\Users\\Simeon\\Downloads\\B-large.in");
	ofstream MyOut;
	MyOut.open("C:\\Users\\Simeon\\Desktop\\PANCAKESTESTLARGEE.txt");


	int length = 0;
	myIn >> length;
	int temp = 0;
	string s = "";

	for(int l = 0; l < length; l++)
	{
		
		int chicken = 0;
		myIn >> s;
		int lenn = s.length();
		
		
	
	for(int k = 1; k < (lenn); k++)
	{

		if(s[k-1] != s[k])
			chicken++;
		

		temp = lenn;
		
	}

	if(s.length() == 1)
	{
		int dinasour = 1;
		if( s == "+")
			dinasour = 0;
		MyOut << "Case #" << l+1 << ": " << dinasour << endl;
	}
	else if(s[temp-1] == '+' )
		MyOut << "Case #" << l+1 << ": " << (chicken) << endl;
	else
		MyOut << "Case #" << l+1 << ": " << chicken+1 << endl;

	chicken = 0;
	string s = "";
	}
	return 0;
}
