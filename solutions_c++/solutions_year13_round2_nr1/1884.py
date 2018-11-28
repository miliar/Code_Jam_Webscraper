#include<iostream>
#include<vector>
#include<fstream>
#include<algorithm>
using namespace std;
long total[300];
long generateSteps(long currentSize,long remains[300],long start,long end)
{
	long seedtoadd=0;
	bool consecutive=false;
	long tempSize=currentSize;
	long innersize;
	int currentScannedIndex=start;
	int currentAddTime=0;
	while(1)
	{
		if(currentAddTime>=(end-start+1))
			break;
		for(int index=currentScannedIndex;index<=end;index++)
		{
			if(remains[index]<tempSize)
			{
				if((index-start)>=currentAddTime)
				{
					tempSize+=remains[index];
					return generateSteps(tempSize,remains,index+1,end)+currentAddTime;
				}
				else
				{
					tempSize+=remains[index];
				}
			}
			else
			{
				currentScannedIndex=index;
				break;
			}
		}
		tempSize=tempSize*2-1;
		currentAddTime++;
	}
	return end-start+1;
}
int main()
{
	ifstream in("large.in",ios::in);
	ofstream out("largeoutput.txt",ios::out);
	long T;
	in>>T;
	for(long index=0;index<T;index++)
	{
		long A;
		long size;
		in>>A;
		in>>size;
		for(long index2=0;index2<size;index2++)
		{
			in>>total[index2];
		}
		sort(total,total+size);
		long result=generateSteps(A,total,0,size-1);
		out<<"Case #"<<index+1<<":"<<" "<<result<<endl;
	}
}