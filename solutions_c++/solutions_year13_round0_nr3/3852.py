/* sqrt example */
#include <stdio.h>
#include <math.h>
#include <iostream>
using namespace std;
int isPalindrome(int n)
{
	int dig,rev=0,num;
	num=n;
	do{
  			dig=num%10;
  			rev=(rev*10)+dig;
  			num=num/10;
  		}while(num!=0);
  		if (n==rev)
  		{
  			//cout<<"palindrome"<<n<<endl;
  			return true;
  			
  		}
  		else
  		{
  			//cout<<"not"<<n<<endl;
  			return false;
  		}
}
int isSquare(int n)
{
	double result;
	result = sqrt(n);
	if((int)result==result)
		return true;
	else
		return false;
	//cout<<result<<endl;
}

int main ()
{
	freopen("in.in","r",stdin);
	freopen("output","w",stdout);
  //double param, result;
  //int n,dig,rev=0;
  int t;
  int a,b,count=0;
  //cin>>t;
  int res;
  //cout<<"\n";
  cin>>t;
  //cin>>a;
  //cin>>b;
  //cout<<a<<b<<t<<endl;

  for (int i = 1; i <= t; i++)
  {
  	cin>>a;
  	cin>>b;
  	res=0;
  	for (int j = a; j <= b; j++)
  	{	
  		//isalindrome(j);
  		if(isPalindrome(j)==1)
  		{
  			//res[i]+=1;
  			if(isSquare(j)==1)
  			{
  				if(isPalindrome((int)sqrt(j))==1)
  					res+=1;
  				else
  					res+=0;
  			}
  				
  			else
  				res+=0;
  		}
  		else
  			res+=0;
  	}
  	cout<<"Case #"<<i<<": "<<res<<endl;
  }
  //for (int i = 1; i <=t; i++)
  //{
  	//cout<<"Case #"<<i<<": "<<res[i]<<endl;
  //}
  return 0;
 }