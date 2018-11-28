#include <bits/stdc++.h>
using namespace std;
int main()
{
int t,len,i,min1,min,sum,k;
	cin>>t;
	int c=1;
	string inp;
	while(t--)
	{
		min=0,min1=0,sum=0;
		cin>>len;
		cin>>inp;

		for(i=0;i<len;i++)
		{
			sum=sum+inp[i]-'0';
			if(sum<i+1)
                min=i+1-sum;

			if(min>min1)
			min1=min;
		}

		cout<<"Case #"<<c++<<": "<<min1<<endl;
	}
return 0;
}
