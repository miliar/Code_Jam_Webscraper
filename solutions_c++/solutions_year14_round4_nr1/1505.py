#include<iostream>
#include<algorithm>
#define SIZE 10001
using namespace std;
int a[SIZE];
int main()
{
	int cas,n,c;
	cin>>cas;
for(int q=1;q<=cas;q++)
{
	cin>>n>>c;
	int sol=0;
	for(int i=0;i<n;i++)cin>>a[i];
	sort(a,a+n);
	int j=0;
	for(int i=n-1;i>=j;i--)
	{
		if(a[i]+a[j]<= c)
		{
			sol++;
			j++;
		}
		else sol++;
	}
	cout<<"Case #"<<q<<": "<<sol<<endl;
}
	return 0;
}
