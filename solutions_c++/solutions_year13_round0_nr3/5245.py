#include<iostream>
#include<fstream>
#include<cmath>
#include<string>
using namespace std;
bool check(int x);
ofstream fout("Out.txt"); 
ifstream fin("C-small-attempt0.in");
int main()
{
	int Iterator;
	fin>>Iterator;
	for(int j=0 ; j<Iterator ; j++)
	{
		int start , end , counter=0;
		fin>>start>>end;
		for(int i=start ; i<=end ; i++)
		{
			if(check(i))
				counter++;
		}
		fout<<"Case #"<<j+1<<": "<<counter<<endl;
	}
	return 0;
}

bool check(int x)
{
	string line = "          ";
	sprintf(&line[0] , "%d" , x);
	int size = 0;
	while(line[size] != '\0')
		size++;
	for(int i=0 ; i<(size/2) ; i++)
		if(line[i] != line[size-1-i])
			return false;

	line = "          ";
	double y = sqrt(x);
	if(int(y) == y)
	{
		sprintf(&line[0] , "%d" , int(y));
		size=0;
		while(line[size] != '\0')
			size++;
		for(int i=0 ; i<(size/2) ; i++)
			if(line[i] != line[size-1-i])
				return false;
	}
	else return false;

	return true;
}