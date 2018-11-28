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
		digitlist[0]=0;
		digitlist[1]=1;
		digitlist[2]=2;
		digitlist[3]=3;
		digitlist[4]=4;
		digitlist[5]=5;
		digitlist[6]=6;
		digitlist[7]=7;
		digitlist[8]=8;
		digitlist[9]=9;

		numOfTry=1;
		long long number;
		scanf("%lld",&number);
		long long Answer=FindNoOfTry(number);
		if(Answer==-1)
		{
			printf("Case #%d: INSOMNIA\n",i);
		}
		else
		{
			printf("Case #%d: %lld\n",i,Answer);
		}
	}

	return 0;
}