#include <iostream>
using namespace std;
bool isP(long long a)
{
	int num[20];
	int cnt = 0;
	while(a)
	{
		num[cnt]=a%10;
		a/=10;
		cnt++;
	}
	for (int i=0;i<cnt/2;i++)
		if (num[i]!=num[cnt-1-i])
			return false;
	return true;
}
int main()
{
	int T;
	cin>>T;
	long long valid[1000000];
	int cnt=0;
	for (long long i=1;i<10000000;i++)
	{
		if (isP(i) && isP(i*i))
		{
			//cout<<i<<' '<<i*i<<endl;
			valid[cnt++]=i*i;
		}
	}
	//cout<<cnt<<endl;
	long long A,B;
	int left,right,start,end,middle;
	for (int i=1;i<=T;i++)
	{
		cin>>A>>B;
		left = 0;
		right = cnt-1;
		while(left+1<right)
		{
			middle=(left+right)/2;
			if (valid[middle]<A)
				left = middle;
			else right = middle;
		}
		if (valid[left]>=A)
			start = left;
		else start = right;
		
		left = 0;
		right = cnt-1;
		while(left+1<right)
		{
			middle=(left+right)/2;
			if (valid[middle]<=B)
				left = middle;
			else right = middle;
		}
		if (valid[left]<=B)
			end = left;
		else end = right;

		cout<<"Case #"<<i<<": ";
		if (end<start)
			cout<<0<<endl;
		else cout<<end-start+1<<endl;

	}
	return 0;
}