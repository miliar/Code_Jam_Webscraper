#include <iostream>
#include <string>
#include <bits/stdc++.h>

#define dig_len(x) (x ? (int)(log10((double)(abs(x)))) + 1 : 1)

using namespace std;

int arr[1000];

void int_to_array(int num,int n)
{
	int l=1,h=10;
	for(int k=0;k<n-1;k++) l = l*h;
	for(int i=0;i<n;i++)
	{
		arr[i] = num/l;
		num = num%l;
		l /= 10;
	}
	for(int i=0;i<n;i++) cout<<arr[i]<<" ";
}

int main()
{
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	
	int t;
	cin>>t;
	while(t--)
	{
		int n,p,x,ans=0,sum=0;
		cin>>n>>p;
		int num = dig_len(p);
		int_to_array(p,num);
		for(int i=0;i<num;i++)
		{
			sum += arr[i];
			if(i+1 <= sum) continue;
			else
			{
				x = (i-sum);
				ans += (i-sum);
				sum += x;
			}
		}
		cout<<ans<<endl;
	}
}
