//finding a perfect square and samce time palindrome number
#include<iostream>
#include<math.h>
using namespace std;

int check_palindrome(long num)
{
	long n,rev,r;
	n = num;
	rev = 0;
	while (num > 0)
	{
		  r = num % 10;
		  rev = rev * 10 + r;
		  num = num / 10;
	}
	if(n == rev){
		return 1;
	}else{
		return 0;
	}
}



int check_square(long num)
{
	long result;
	result = sqrt(num);
	if (((result * result)== num) && (check_palindrome(result)))
	{
		return 1;
	}
	else{
		return 0;
	}
}


int main(){
long num;
int T;
int count;
long start,end;
cin>>T;
int number=T;
do{
	cin>>start>>end;
	cout<<endl;
	for(long i=start;i<=end;i++)
	{
		if((check_palindrome(i) && check_square(i))==1)
		{
			count++;
		}
	}
	cout<<"Case #"<<number-(T-1)<<": "<<count;
	count=0;
	T--;
}while(T!=0);
return 0;
}
