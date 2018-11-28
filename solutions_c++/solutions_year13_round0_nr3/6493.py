#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;


bool isPalindrome(long num)
{
	int length=0,i=0;
	bool palFlag=false;
	long tmpNum=num;
	

		while(tmpNum!=0)
		{
			tmpNum=tmpNum/10;
			length++;
			
		}
		
	long *numArr=new long[length-1];
	tmpNum=num;
	while(i<length)
	{
		numArr[(length-1)-i]=tmpNum%10;
		tmpNum/=10;
		i++;
	}
	i=0;
	while(i<length)
	{
		if(!(numArr[i]==numArr[(length-1)-i]))
		{
			
			palFlag=false;
			break;
			
		}else
		{
			palFlag=true;
		}
		i++;
	}

	return palFlag;
}

int main(){

	int TC=0;
	long left=0,right=0;
	ifstream in("C-small-attempt0.in");
	ofstream o("C-small-attempt0.out");
	in>>TC;

	for(int iTmp=1;iTmp<=TC;iTmp++)
	{
		int count=0;
		in>>left;
		in>>right;

		while(left<=right)
		{
			if(isPalindrome(left))
			{
				long tmpRoot=sqrtl(left);
				
				if(tmpRoot==sqrtl(left))
				if(isPalindrome(sqrtf(left)))
				{
					count++;
				}
				
			}

			left++;
		}

		o<<"Case #"<<iTmp<<": "<<count<<endl;

	}

	return 0;

	
}

