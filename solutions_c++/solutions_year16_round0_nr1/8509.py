#include <iostream>
#include <algorithm>
#include<set>
#include<vector>
#include<cstdio>
//priyansh chutiya h
//priyansh chutiya h
//priyansh chutiya h
//priyansh chutiya h
//pjfdbkgdklg;ldfkg;ldriyansh chutiya h
//priyansh chutiy.gjdfhkgjdfa h
//priyansh chutiyfnkjghkjdfngkldfsa h
//priyansh chutiya h
//priyansh chutiya h
//priyansh chutikhfuifgjdgijdfsklguidshfgfdslya h
//priyansh chutiya h
//priyansh chhgrkhgjksdfhkutiya h
using namespace std;
set <long long int> this_set;
long long int plg=0;
void numbe(long long int num)
{
	while(num)
	{
		this_set.insert(num%10);
		num=num/10;
	}
	if(this_set.size()==10)
	plg=1;
}
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	long long int numberr,test,j;
cin>>test;
j=test;
while(test--)
{
	cin>>numberr;
	if(numberr==0)
	cout<<"Case #"<<j-test<<": INSOMNIA\n";
	else
	{
		long long int i=1;
		plg=0;
		while(1)
		{
			numbe(numberr*i);
			i++;
			if(plg==1)
			break;
		}
		cout<<"Case #"<<j-test<<": "<<numberr*(i-1)<<endl;
	}
	this_set.clear();
}
	return 0;
}
