#include<iostream>
#define UINT unsigned long long

using namespace std;

char multiply(char a,char b)
{
	if(a=='1')
	{
		switch(b)
		{
			case 'i':return 'i';
			case 'j':return 'j';
			case 'k':return 'k';
			case '1':return '1';
			case '0':return '0';
		}
	}
	
	if(a=='0')
	{
		switch(b)
		{
			case 'i':return 'I';
			case 'j':return 'J';
			case 'k':return 'K';
			case '1':return '0';
			case '0':return '1';
		}
	}

	if(a=='i')
	{
		switch(b)
		{
			case 'i':return '0';
			case 'j':return 'k';
			case 'k':return 'J';
			case '1':return 'i';
			case '0':return 'I';
		}
	}
	
	if(a=='j')
	{
		switch(b)
		{
			case 'i':return 'K';
			case 'j':return '0';
			case 'k':return 'i';
			case '1':return 'j';
			case '0':return 'J';
		}
	}

	if(a=='k')
	{
		switch(b)
		{
			case 'i':return 'j';
			case 'j':return 'I';
			case 'k':return '0';
			case '1':return 'k';
			case '0':return 'K';
		}
	}
	if(a=='I')
	{
		switch(b)
		{
			case 'i':return '1';
			case 'j':return 'K';
			case 'k':return 'j';
			case '1':return 'I';
			case '0':return 'i';
		}
	}
	if(a=='J')
	{
		switch(b)
		{
			case 'i':return 'k';
			case 'j':return '1';
			case 'k':return 'I';
			case '1':return 'J';
			case '0':return 'j';
		}
	}
	if(a=='K')
	{
		switch(b)
		{
			case 'i':return 'J';
			case 'j':return 'i';
			case 'k':return '1';
			case '1':return 'K';
			case '0':return 'k';
		}
	}

	return a;
}

char strMultiply(string str, UINT lower, UINT upper)
{
	UINT elemCount;
	char prod = '1';

	for(elemCount = lower;elemCount<=upper; elemCount++)
	{
		prod = multiply(prod,str[elemCount]);
	}

	return prod;
}

UINT multiCompare(string str, UINT lower, UINT upper, char ch)
{
	UINT elemCount;
	char prod = '1';

	for(elemCount = lower;elemCount<=upper;elemCount++)
	{
		prod = multiply(prod,str[elemCount]);
		if(prod == ch)
			break;
	}

	return elemCount;
}

int main()
{
	UINT testCases,caseCount,l,x,product,elemCount,length;
	string part,full;
	char prod;
	
	ios::sync_with_stdio(false);
	cin>>testCases;
	for(caseCount = 1; caseCount<=testCases;caseCount++)
	{
		cin>>l>>x>>part;
		full="";
		length = l*x;

		if(l*x<3)
		{
			cout<<"Case #"<<caseCount<<": NO"<<endl;
			continue;
		}

		for(elemCount =0 ;elemCount<x;elemCount++)
		{
			full.append(part);
		}

		if(strMultiply(full,0,length-1) != '0')
		{
			cout<<"Case #"<<caseCount<<": NO"<<endl;
			continue;
		}	

		elemCount = multiCompare(full,0,length-1,'i');
		
		if(elemCount>=length)
		{
			cout<<"Case #"<<caseCount<<": NO"<<endl;
			continue;
		}

		elemCount = multiCompare(full,elemCount+1,length - 1,'j');

		if(elemCount>=length)
		{
			cout<<"Case #"<<caseCount<<": NO"<<endl;
			continue;
		}
		
		elemCount = multiCompare(full,elemCount+1,length-1,'k');
		
		if(elemCount >= length)
		{
			cout<<"Case #"<<caseCount<<": NO"<<endl;
			continue;
		}

		cout<<"Case #"<<caseCount<<": YES"<<endl;
	}

	return 0;
}


