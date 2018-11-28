#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;


int main()
{

	ifstream infile("A.in");
	ofstream fout("A.out");
	string line;
	vector<long long int> v;

	while (std::getline(infile, line))
	{	
	istringstream iss(line);
	long long int n;

 	 while (iss >> n)
  	{
   	 v.push_back(n);
  	}
	}	
	
	long long int T=v[0],cases,r,t,k,test;
	cout<<"Test cases ="<<T<<endl;
	for(cases=0;cases<T;cases++)
	{
		r = v[(cases*2)+1];
		t = v[(cases*2)+2];
		for(k=1;;k++)
		{
		test= (2*k*k)+((2*r+3)*k)+(2*r+1);
		if(test>t)
		break;
		}
		
		cout<<"Case #"<<(cases+1)<<": "<<k<<endl;
              	fout<<"Case #"<<(cases+1)<<": "<<k<<endl;

	}	
}
