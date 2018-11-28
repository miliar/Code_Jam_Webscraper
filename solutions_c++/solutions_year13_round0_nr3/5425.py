#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;


bool ispalin(long long N)
{
long long s = 0, a=N,r;
	
	while(N>0)
	{
	r=N%10;
	s=s*10+r;
	N=N/10;
	}
	if(s==a)
	return true;
	else
	return false;
}


int main()
{

	ifstream infile("C-small-attempt0.in");
	ofstream fout("C-small.out");
	string line;
	vector<int> v;

	while (std::getline(infile, line))
	{	
	istringstream iss(line);
	int n;

 	 while (iss >> n)
  	{
   	 v.push_back(n);
  	}
	}	
	
	long long i,A,B,Ait,Bit,count=0;
	vector<long> cnt;

	for(i=0;i<v[0];i++)
	{
	count=0;
	A=v[2*i+1];
	B=v[2*i+2];
	Ait=sqrtf(A);
	Bit=pow(Ait,2);
	while(Bit<=B)
	{
	if(ispalin(Bit)&&ispalin(Ait)&&(Bit>=A))
	count++;
	++Ait;
	Bit=pow(Ait,2);
	}
	cnt.push_back(count);
	fout<<"Case #"<<(i+1)<<": "<<count<<endl;
	}
}
