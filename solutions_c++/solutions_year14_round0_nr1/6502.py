// cj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<string>
using namespace std;

#include<vector>
#include<algorithm>
#include<functional>

#define res(i) cout<<"Case #"<<i<<": "
#define fo(c)for(int i=0;i<c;i++)
int _tmain(int argc, _TCHAR* argv[])
{
	int n;
	cin>>n;

	for(int a=1;a<=n;a++)
	{
		int arr[8]={0};
		int c,d;
		cin>>c;
		int t;
		fo(c-1)
			fo(4)
				cin>>t;
		fo(4)
			cin>>arr[i];
		fo(4-c)
			fo(4)
				cin>>t;
		
		cin>>d;
		fo(d-1)
			fo(4)
				cin>>t;
		fo(4)
			cin>>arr[i+4];

		fo(4-d)
			fo(4)
				cin>>t;
		
		int count=0;
		int ans=0;
		fo(4)
			for(int j=4;j<8;j++)
				if (arr[i]==arr[j])
				{
					count++;
					ans=arr[i];
				}
		if (count==0)
			res(a)<<"Volunteer cheated!"<<endl;
		else if (count==1)
			res(a)<<ans<<endl;
		else if (count > 1)
			res(a)<<"Bad magician!"<<endl;
	}
	return 0;
}

