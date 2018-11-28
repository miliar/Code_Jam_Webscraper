#include "StdAfx.h"
#include "FairAndSquare.h"

CFairAndSquare::CFairAndSquare(void)
{
}

CFairAndSquare::~CFairAndSquare(void)
{
}
void CFairAndSquare::Run()
{
	int start,end;
	string input;
	int count=0;
	while( (input=m_oInput.ReadLine()).length())
	{
		sscanf(input.c_str(),"%d %d",&start,&end);
		count=0;
		for(int i=start;i<=end;i++)
		{
			int square;
			if(isSquare(i,square) && isFair(i))
			{
				if(isFair(square))
					count++;
			}
		}
		Write(count);
	}
}
bool CFairAndSquare::isSquare(int num,int &i)
{
	if( num == 1)
	{
		i=num;	
		return (true);
	}
	for(i=2;i<num;i++)
	{
		if( (i*i) == num )
			return true;
		else if( (i*i) > num)
			return false;
	}
	return(false);
}
bool CFairAndSquare::isFair(int n)
{
	int num = n;
	int rev=0;
	while(num >0)
	{
		int d=num%10;
		if( rev == 0)
			rev = d;
		else
			rev = rev*10 + d;
		num = num/10;
	}
	return( n == rev);
}

void CFairAndSquare::Write(int ret)
{
	char temp[100];
	static int casenumber=1;
	sprintf(temp,"Case #%d: %d\n",casenumber++,ret);
	m_oOutput.Writer(temp);
}