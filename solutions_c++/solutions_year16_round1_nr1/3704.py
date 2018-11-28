#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int T = t;
	while(t--)
	{
		string s;
		cin>>s;
		int n = s.length();
		char a[2*n + 4];
		int counter1 = n+2;
		int counter2 = n+2;
		a[counter1] = s[0];
		for(int i=1;i<n;i++)
		{
			if(a[counter1] <= s[i])
			{
				a[--counter1] = s[i];
			}
			else
			{
				a[++counter2] = s[i];
			}
		}
		cout<<"Case #"<<T-t<<": ";
		for(int i = counter1 ;i<= counter2;i++)
		{
			cout<<a[i];
		}
		cout<<"\n";

	}
}
