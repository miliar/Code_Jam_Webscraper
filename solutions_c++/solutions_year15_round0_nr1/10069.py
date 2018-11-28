#include <iostream>
#include <string.h>
using namespace std;
 
int main() {
	// your code goes here
	int test,len,i,min1,min,sum,k;
	cin>>test;
	k=test;
	string alg;
	while(test--)
	{
		min=0,min1=0,sum=0;
		cin>>len;
		cin>>alg;
 
		for(i=0;i<len;i++)
		{
			sum=sum+alg[i]-48;
			if(sum<i+1)
			min=i+1-sum;
 
			if(min>min1)
			min1=min;
		}
 
		cout<<"Case #"<<k-test<<": "<<min1<<endl;
	}
	return 0;
}