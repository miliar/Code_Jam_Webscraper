#include<iostream>
#include<fstream>
#include<string>
using namespace std;

main()
{
	ifstream input("B-large.in");
    ofstream out("output.txt");
	
	string N;
	int c=0;
	//input>>N;
	int x;
	input>>x;
	
	for(int y=0;y<x;y++)
	{ 
	int counter=0;
		
		input>>N;
		
		for(int i=0;i<N.size();i++)
		{
			if(i==N.size() - 1  &&  N[i]=='-')
			counter++;
			
			if(i>0 &&  N[i-1]=='-'  && N[i]=='+')
			counter++;
			
			if(i>0  &&  N[i-1]=='+' && N[i]=='-')
			counter++;
			
			
			
			
			
			
		}
		c++;
		out<<"Case #"<<c<<": "<<counter<<endl;
		
		
		
		
	}//end of first while loop
	
	
	
}
