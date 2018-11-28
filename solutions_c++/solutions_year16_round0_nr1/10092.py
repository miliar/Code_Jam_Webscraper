#include <bits/stdc++.h>
using namespace std;

int arr[10] = {};
int main() {
	long long n , num , tst,i , k;			cin>>n;
	
	for(long long q=0;q<n;q++)
	{
		cin>>num;			tst = num ;
		if(num == 0)		{cout<<"Case #"<<q+1<<": "<<"INSOMNIA"<<endl;		continue;}
		i=0;
		k=0;
		memset (arr ,0,sizeof(arr));
		while(k != 10)
		{
			i++;			tst = num;
			tst *=i;
			while(tst != 0)
			{
				if(arr[tst%10]==0)			k++;
				arr[tst%10]++;
				tst/=10;
			}
		}
		cout<<"Case #"<<q+1<<": "<<i*num<<endl;
		
		
	}
	
	return 0;
}