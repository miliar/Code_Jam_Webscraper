#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("C-small-attempt0.in");
ofstream fout("C-small-attempt0.out");

int cases;
int lower;
int upper;
int compute(int ,int);
int checkSquare(int ,int );
int checkPalindrome(int ,int);
int compute(int a,int b)
{
	int temp,count=0;
	for( ;a<=b;a++)
	{
		temp=(int)sqrt(a);
		if(checkSquare(temp,a))
			if(checkPalindrome(a,temp))
				count++;
    }
	return(count);
}
int checkPalindrome(int a,int b)
{
	int copya,copyb,rema=0,remb=0;
	copya=a;
	copyb=b;
	while(a!=0)
	{
		rema=rema*10;
		rema=rema+a%10;
		a=a/10;
	}
	while(b!=0)
	{
		remb=remb*10;
		remb=remb+b%10;
		b=b/10;
	}
	if((copya==rema)&&(copyb==remb))
		return(1);
	else
		return(0);
}
int checkSquare(int temp,int a)
{
	if((temp*temp)==a){return(1);}
	return(0);
}
int main()
{
	int i=0;
	fin>>cases;
	while(i<cases)
	{
		fin>>lower;
		fin>>upper;
		fout<<"Case #";
		fout<<(i+1);
		fout<<": ";
		fout<<compute(lower,upper);
		i++;
		if(i!=cases){fout<<"\n";}
	}
	return 0;
}
