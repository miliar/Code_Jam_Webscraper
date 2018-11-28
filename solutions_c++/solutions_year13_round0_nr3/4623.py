#include<iostream>
#include<cmath>
#include<cstdlib>
using namespace std;
bool ispalindrome(int a);
int main()
{
int t;
cin>>t;


for(int k=0;k<t;k++)
{
	int counter=0;
	double a,b;
	cin>>a>>b;

	for(double i=a;i<=b;i++)
	{
		double sqrt=pow(i,0.5);
		if(sqrt==floor(sqrt))
		{
	//		cout<<i;
			if(ispalindrome(i) && ispalindrome(sqrt)) 
				counter++;
		}
	
	}
	cout<<"Case #"<<k+1<<": "<<counter<<endl;

}
return 0;
}

bool ispalindrome(int a)
{
int no_digits=log10(a)+1;
char *eq=new char[no_digits];

for(int i=0;i<no_digits;i++)
	{
	eq[no_digits-i-1]=a%10;
	a=a/10;
	}

int length=no_digits;
int len2=length/2;
for(int i=0;i<len2;i++)
{
	if(eq[i]!=eq[length-i-1])
		return false;
}
return true;

}
