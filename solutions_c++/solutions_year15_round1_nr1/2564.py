#include <iostream.h>
#include <fstream.h>
#include <conio.h>
void main()
{
	clrscr();
	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);
	int cases;
	fin>>cases;
	int array[1000], size;
	for (int i=0; i<cases; ++i)
	{
		fin>>size;
		for (int j=0; j<size; ++j)
		{
			fin>>array[j];
		}
		int highest=array[0]-array[1];
		for (int k=1; k<size-1; ++k)
		{
			if ((array[k]-array[k+1])>highest)
			{
				highest=array[k]-array[k+1];
			}
		}
		long count1=0;
		for (k=0; k<size-1; ++k)
		{
			if (array[k]<highest) count1+=array[k];
			else count1+=highest;
		}
		long count=0;
		for (int l=0; l<size-1; ++l)
		{
			if ((array[l]-array[l+1])>0)
			{
				count=count+(array[l]-array[l+1]);
			}
		}
		fout<<"Case #"<<i+1<<": "<<count<<" "<<count1<<endl;
}
}