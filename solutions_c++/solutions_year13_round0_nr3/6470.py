// C_Fair And Square.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
#include "fstream"
#include "math.h"
using namespace std;

bool is_palindrome(int i)
{
	int temp=0,num;
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
	int t,a,b,count=0,sqr=0;
    bool sq=false;
    ifstream fin("C-small-attempt1.in");
	ofstream fout("C-small.out");
    fin>>t;
    for(int n=0;n<t;n++)
    {
        fin>>a>>b;
        for(int i=a;i<=b;i++)
        {
			sqr=sqrt(double(i));
            for(int j=1;j<=sqr;j++)
            {
                if(j*j==i)
                {
                    sq=true;
                    break;
                }
            }
            if(sq)
            {
              if(is_palindrome(i) && is_palindrome(sqr))
				  count++;
            }
			sq=false;
        }
        fout<<"Case #"<<n+1<<": "<<count<<endl;
        count=0;
    }
    
	return 0;
}

