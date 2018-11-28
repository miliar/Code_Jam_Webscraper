#include<iostream>
#include<cstdio>
#include<algorithm>
#include<numeric>
#include<cstring>
#include<set>
#include<utility>
#include<vector>
using namespace std;
//int a[101],b[101];
int main()
{
	int ar[]={1,4,9,121,484};
	int k,t,a,b,cnt;
	cin >> t;
	while(k<=t)
	{
		cnt=0;
		cin >>a >>b;
		for(int i=0;i<5;i++)
		{
			if(ar[i]>=a && ar[i]<=b)
				cnt++;
		}
		cout<<"Case #"<<k<<": "<<cnt<<endl;
		k++;
	}
	return 0;
}
