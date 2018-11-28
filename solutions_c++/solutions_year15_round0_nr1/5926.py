#include <iostream.h>
#include <fstream.h>
#include <conio.h>
void main()
{
	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);
	char ch;
	int array[1010];
	int cases;
	fin>>cases;
	for (int i=0; i<cases; ++i)
	{
		int stand=0, count=0;
		int size;
		fin>>size;
		for (int j=0; j<size+1; ++j)
		{
			fin>>ch;
			if (ch=='0') array[j]=0;
			if (ch=='1') array[j]=1;
			if (ch=='2') array[j]=2;
			if (ch=='3') array[j]=3;
			if (ch=='4') array[j]=4;
			if (ch=='5') array[j]=5;
			if (ch=='6') array[j]=6;
			if (ch=='7') array[j]=7;
			if (ch=='8') array[j]=8;
			if (ch=='9') array[j]=9;
		}
		stand+=array[0];
		for (j=1; j<size+1; ++j)
		{
			 if (array[j]==0) continue;
			 while (stand<j)
			 {
				++stand;
				++count;
			 }
			if (stand>=j) stand+=array[j];
		}
		fout<<"Case #"<<i+1<<": "<<count<<endl;
	}
}


