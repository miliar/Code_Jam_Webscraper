#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <limits.h>

using namespace std;

int fairAndSquare(int r1,int r2);
bool isPalindrome(int num);
int main()
{
	int T,i=0,index=0;
	cin>>T;
	for(i=0;i<T;i++)
	{
		int r1,r2;
		cin>>r1>>r2;
		cout<<"Case #"<<i+1<<": "<<fairAndSquare(r1,r2)<<endl;
		//fairAndSquare(r1,r2);
		//cout<<r1<<"  "<<r2<<endl;;
	}
return 0;
}

int fairAndSquare(int r1,int r2)
{
	int count=0,i=r1;
	//cout<<i<<"  "<<r2<<endl;
	while(i<=r2)
	{
		int root=sqrt(i);
		//cout<<root<<endl;
		bool pal=isPalindrome(i);
		bool rpal=isPalindrome(root);
		int sqr=root*root;
		bool perfect=(sqr==i);
		//cout<<root<<"  "<<pal<<"  "<<rpal<<"  "<<perfect<<endl;
		if(pal&&rpal&&perfect)
		{
			count++;
		}
		i++;
	}
return count;
}

bool isPalindrome(int num)
{
	int rev=0,temp=num;
	while(temp!=0)
	{
		rev = (rev*10)+(temp%10);
		temp = temp/10;
	}
	//cout<<num<<endl;
	if(rev==num) return true;
	else return false;
}
