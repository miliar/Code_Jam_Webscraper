#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;
main()
{
	int num[]={1,4,9,121,484},T;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	for(int c=1;c<=T;c++)
	{
		int count=0,a,b,i=0;		
		cin>>a>>b;
		for(i=0;i<5;i++)
		{
			if(num[i]>=a && num[i]<=b)
				count++;
		}
		cout<<"Case #"<<c<<": "<<count<<endl;
	}
    return 0;
}
