#include<iostream>
#include <algorithm> 
#include <fstream>
#include <iomanip>
using namespace std;
int main()
{
	ifstream cin;
    ofstream cout;
    cin.open ("D-large.in");
    cout.open("output.txt");
	int t,i,n,j,k,ans1,ans2,x,y;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		float a[n],b[n];
		for(j=0;j<n;j++)
		{
			cin>>a[j];
		}
		for(j=0;j<n;j++)
		{
			cin>>b[j];
		}
		sort(a,a+n);
		sort(b,b+n);
		ans1=n-j;
		x=0;
		y=0;
        ans2=0;
        ans1=0;
        while(1)
		{
			if(a[x]>b[y])
			{
				ans1++;
				x++;
				y++;
			}
			else
			{
				x++;
			}
			if(x==n||y==n)
			{
				break;
			}
		}
		x=0;
		y=0;
		while(1)
		{
			if(a[x]<b[y])
			{
				ans2++;
				x++;
				y++;
			}
			else
			{
				y++;
			}
			if(x==n||y==n)
			{
				break;
			}
		}
		ans2=n-ans2;
		cout<<"Case #"<<i<<":"<<" "<<ans1<<" "<<ans2<<endl;
	}
}
