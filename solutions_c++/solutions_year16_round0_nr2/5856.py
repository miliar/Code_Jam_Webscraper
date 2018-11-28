#include<iostream>
#include<fstream>
#include<string>
using namespace std;

main()
{
	ifstream inn("B-large.in");
    ofstream out("output.txt");
	
	string non;
	long long coun1=0;

	long long T;
	inn>>T;
	
	for(int y=0;y<T;y++)
	{ 
	long long coun=0;
		
		inn>>non;
		
		for(int i=0;i<non.size();i++)
		{
			if(i==(non.size()-1)  and  non[i]=='-')
			coun++;
			
			if(i>0 and  non[i-1]=='-'  and non[i]=='+')
			coun++;
			
			if(i>0  and  non[i-1]=='+' and non[i]=='-')
			coun++;
			
			
			
			
			
			
		}
		coun1++;
		out<<"Case #"<<coun1<<": "<<coun<<endl;
		
		
		
		
	}
	
	
	
}
