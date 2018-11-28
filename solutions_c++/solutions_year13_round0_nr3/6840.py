#include<cstdio>
#include<cmath>
#include <sstream> 
#include<iostream>

using namespace std;

int check_palindrome(int num)
{
	string str;
	stringstream ss;
	int n,res;
	ss << num;
	str=ss.str();
	n=str.length();	
	if(str.length()%2==1)
		n--;
	for(int i=0;i<=n/2;i++)
	{
		if(str.length()==1)
		{
			n=1;
			return n;
			break;
		}
		if(str[i]!=str[str.length()-1-i])
		{
			n=0;
			return n;
			break;
		}
		else
		{
			n=1;
			return n;
			break;
		}		
	}
}

int check_root(int A,int B)
{
	int n=0;
	int Ac,Numc;
	float num;
	for(A;A<=B;A++)
	{
		num=sqrt(A);
		if(num==int(num))
		{	
			Ac=check_palindrome(A);
			Numc=check_palindrome(int(num));
			if(Ac==1)
				if(Numc==1)
				n++;
		}
	}
	return n;
}

int main()
{
		int T,A[1000],B[1000],tCase[1000];
		scanf("%d",&T);
		for(int i=1; i<=T;i++)
			scanf("%d %d",&A[i],&B[i]);
		for(int i=1; i<=T;i++)
		{
			tCase[i]=check_root(A[i],B[i]);
		}
		for(int i=1; i<=T;i++)
		{
			printf("Case #%d: %d\n",i,tCase[i]);
		}
		return 0;	
}	
