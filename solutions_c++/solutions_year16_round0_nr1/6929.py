#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>

using namespace std;

int lastNumber(int N);
bool listCheck(int list[10]);


int main()
{
	
	ifstream c;
	c.open("A-large.in");
	
	if (c.fail())
		cout<<"Input Failed"<<endl;
	
	
	ofstream s("output.txt");
	
	int T;
	c>>T;
	
	int N[T];
	for (int i=0;i<T;i++)
		c>>N[i];
	
	c.close();
	
	for (int i=0;i<T;i++)
	{
		s<<"Case #"<<i+1<<": ";
		
		int number;
		number = lastNumber(N[i]);
		
		if (number == -1)
			s<<"INSOMNIA"<<endl;
		else
			s<<number<<endl;
		
		
	}
	
	s.close();
}

int lastNumber(int N)
{
	if (N==0)
		return -1;
		
	
	int list[10] = {0,0,0,0,0,0,0,0,0,0};
	
	int i = 1;
	int number;
	
	while ( listCheck(list) != true)
	{
		number = i*N;
		
		int temp = number;
		while (temp != 0)
		{
			int t;
			t = temp%10;
			if (list[t] != 1)
				list[t] = 1;
			
			temp = temp/10;
			
		}
	
		i++;
		
	}
	
	return number;
	
	
}

bool listCheck(int list[10])
{
	int check = 1;
	
	for (int i=0;i<10;i++)
	{
		if (list[i] == 0)
			check = 0;
	}
	
	if (check == 0)
		return false;
	else
		return true;
}






















