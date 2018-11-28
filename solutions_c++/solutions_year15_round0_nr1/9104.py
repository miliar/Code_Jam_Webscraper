#include<iostream>
#include<algorithm>
#include<map>
#include<iomanip>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<iostream>
#include<cstring>
#include <fstream>
#include <stack>
#include<fstream>


using namespace std;

unsigned long * toInt(string a)
{
	char temp;
	unsigned long  * Array = new unsigned long [a.size()];
	for(int i=0; i<a.size(); i++)
	{
		temp = a[i];
		if(temp == '0')
		{
			Array[i] = 0;
		}
		if(temp == '1')
		{
			Array[i] = 1;
		}
		if(temp == '2')
		{
			Array[i] = 2;
		}
		if(temp == '3')
		{
			Array[i] = 3;
		}
		if(temp == '4')
		{
			Array[i] = 4;
		}
		if(temp == '5')
		{
			Array[i] = 5;
		}
		if(temp == '6')
		{
			Array[i] = 6;
		}
		if(temp == '7')
		{
			Array[i] = 7;
		}
		if(temp == '8')
		{
			Array[i] = 8;
		}
		if(temp == '9')
		{
			Array[i] = 9;
		}
	}
	return Array;
}


unsigned long  countPerson(unsigned long * Person, unsigned long  size)
{
		unsigned long  sum = 0;
		for(int i=0; i<size; i++)
			sum = Person[i]+sum;
		return sum;
}
int friends(unsigned long * line,unsigned long  size)
{
	unsigned long  int more=0;
	unsigned long int count =0;
	unsigned long  int numberCount;
	bool *temp = new bool[size];
	
	for(int i=0; i<size; i++)
	{
		if(line[i] == 0)
			temp[i] = false;
		else
		{
			temp[i] = true;
		}
	}


	for(int j=0; j<size; j++)
	{
		
		if(temp[j] == false && temp[j+1]== true)
		{
			numberCount = countPerson(line,j+1);
			if(j+1 > numberCount)
			{
				more = j+1-numberCount;
				line[j] = line[j]+more;
				count = count +more;
			}
	//		else if(j+1 == countPerson(line,j+1))
	//			count = 0;
	//		else if( j+1 < countPerson(line,j+1))
	//			count = 0;
		}
	
	}
	
	return count;
}





int main()
{
	
	unsigned long  cases;
	string line;
	unsigned long  size;
	ifstream file;
	ofstream file2;
	unsigned long  a;
	unsigned long  count=1;
	file.open("A-large.in");
	file2.open("A-large.out");
	file>>cases;
	while(!file.eof())
	{
		file>>size;
		file>>line;
	//	cout<<"Case #"<<count<<": "<<friends(toInt(line),size+1)<<endl;
		file2<<"Case #"<<count<<": "<<friends(toInt(line),size+1)<<endl;
		count++;
	}

	return 0;
}