#include<iostream>
#include<stdlib.h>
#include<fstream>

using namespace std;

int c;
int check(int num[],int size)
{
	int friends = 0,sum=0,ctr=0,i;
	while (ctr<1005)
	{
		sum = friends + num[0];
		for (i = 1; i < size; i++)
		{
			if (i>sum)
			{
				friends++;
				break;
			}
			sum += num[i];
		}
		ctr++;
	}
	return friends;
}

void main()
{
	ifstream filin("input.in", ios::in);
	ofstream filout("output.txt", ios::out);
	int number,size,j,ctr=0;
	int aud[2500];
	char *ch,cha;
	filin >> number;
	cout << number << endl;
	for (int i = 0; i < number; i++)
	{
		filin >> size;
		size++;
		for (j = 0; j < size; j++)
		{
			filin >> cha;
			ch = &cha;
			aud[j] = atoi(ch);
		}
		filout << "Case #" << ++c << ": " << check(aud,size)<<endl;
	}
	filin.close();
	filout.close();
}