// C_Fair And Square_Large.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
#include "fstream"
#include "math.h"
using namespace std;

bool is_palindrome(int i)
{
	long long int temp=0,num;
	num=i;
    while(num>9)
    {
		temp*=10;
        temp+=num%10;
        num/=10;
	}
	temp*=10;
    temp+=num;
    if(temp==i)
    {
		return true;
	}
	return false;
        
}

int main()
{
	long long int t,a,b,count=0,sqr=0,arr[100000],index=0;
    bool sq=false;
    ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small.out");
    fin>>t;
	//----------------------------------------------------------------------
        for(long long int i=1;i<=99999999999999;i++)
        {
			sqr=sqrt(double(i));
			if(sqr*sqr==i)
			{
				sq=true;
			}

            if(sq)
            {
              if(is_palindrome(i) && is_palindrome(sqr))
				  arr[index++]=i;
				 // count++;
            }
			sq=false;
			i=(sqr+1)*(sqr+1)-1;
        }
		//---------------------------------------------------------------------
		int start=0,end=0;
		for(int n=0;n<t;n++)
		{
			fin>>a>>b;
			for(int i=0;i<index;i++)
			{
				if(arr[i]>=a)
				{
					start=i;
					break;
				}
			}
			for(int i=start;i<index;i++)
			{
				if(arr[i]==b)
				{
					end=i;
					break;
				}
				else if(arr[i]>b)
				{
					end=i-1;
					break;
				}
				else if(i==index-1)
				{
					end=i;
					break;
				}
			}
			fout<<"Case #"<<n+1<<": "<<end-start+1<<endl;
		}
    
	return 0;
}

