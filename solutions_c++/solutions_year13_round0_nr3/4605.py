#include<iostream>
#include<cmath>
using namespace std;
/*
Input
The first line of the input gives the number of test cases, T. T lines follow. Each line contains two integers, A and B - the endpoints of the interval 
Little John is looking at.
Output
For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number of fair and square numbers greater than or equal to A and smaller than or equal to B.
Limits
Small dataset
1 ≤ T ≤ 100.
1 ≤ A ≤ B ≤ 1000. 
Input
3
1 4
10 120
100 1000
Output
Case #1: 2
Case #2: 0
Case #3: 2
*/

int A=0,B=0;


int rev(int n)
{
	int reve=0,rem=0;
    	while(n>0)
    	{
        	rem=n%10;
            	reve=reve*10+rem;
              	n=n/10;
    	}
    	return reve;
}

int check_palindrome(int i)
{
	int n=rev(i);
	if(n==i)
		return 1;
	else return 0;	
}

int check_square(int i)
{
	int n=sqrt(i),m=0;
	m=n*n;
	if(m==i)
	     return check_palindrome(n);
	else return 0;
}

int main()
{
	int T=0,j=1,c_palindrm=0,c_prfct_sq=0,count=0;
	cin >> T;
	while(T--)
	{
		cin >> A >> B;
		count=0;
		for(int i=A;i<=B;i++)
		{
			c_palindrm=0;
			c_prfct_sq=0;
			c_palindrm=check_palindrome(i);
			if(c_palindrm)
				c_prfct_sq=check_square(i);
			if(c_prfct_sq==1)
				count++;
		}
		cout << "Case #" << j << ": " <<  count << "\n";
		j++;
	}
	return 0;
}
