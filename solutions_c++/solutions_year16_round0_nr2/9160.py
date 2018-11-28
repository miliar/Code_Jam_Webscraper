#include<iostream>
#include<map>
using namespace std;

map<int, int> digitlist;


static long long numOfTry=1;

long long FindNoOfTry(long long number)
{
	
	if(number==0)
		return -1;

	long long tempNo=number;

	while(tempNo)
	{
		std::map<int,int>::iterator it;
		int digit=tempNo%10;
		it=digitlist.find(digit);
		if(it!=digitlist.end())
		{
			digitlist.erase(it);
			if(digitlist.size()==0)
				return number;
		}
		tempNo=tempNo/10;
	}
	number=number/numOfTry;
	numOfTry+=1;
	number=numOfTry*number;
	return FindNoOfTry(number);
}



int main()
{
	int tc;
	scanf("%d",&tc);
	for(int i=1;i<=tc;i++)
	{
		char name[100];		
		scanf("%s",name);
		int flipcount=0;
		char currentstate=name[0];
		int length=strlen(name);
		for(int c=1; c<length;c++)
		{
			
			if(currentstate!=name[c])
			{
				currentstate=name[c];
				flipcount++;
			}
		}
		if(currentstate=='-')
			flipcount++;

		printf("Case #%d: %d\n",i,flipcount);
	}

	return 0;
}