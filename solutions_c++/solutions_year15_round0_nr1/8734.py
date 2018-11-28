#include <iostream>
#include <stdio.h>

using namespace std;


int main()
{
	int t,i,s,ppl,sum;
	short int arr[1000];
	cin>>t;
	char ch;
	for (i = 0; i < t; ++i)
	{
		cin>>s;
		getchar();
		sum=0;
		for(int j=0;j<=s;++j){
			arr[j]=0;
			cin>>ch;
			arr[j]=ch-'0';
			sum+=arr[j];
		}
		ppl=0;
		for(int j=0;j<=s;++j){
			if(ppl<j&&arr[j]>0)
				ppl+=(j-ppl);
			ppl+=arr[j];
		}
		cout<<"Case #"<<i+1<<": "<<ppl-sum<<endl;
	}
	return 0;
}