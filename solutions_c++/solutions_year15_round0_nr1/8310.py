#include<stdio.h>
#include<iostream>
#include <string>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w", stdout);
	int i,j, n,a[1005],t,p,s;
	string inputStr;
	cin >> t;
	for(i=0;i<t;i++)
	{
		cin >> n;
		//scanf("%s",a);
		cin >> inputStr;
		s=0;
		p=0;
		for(j=0;j<=n;j++)
		{
		
			if(s<j)
			{
				s=s+1;
				p=p+1;
			}
			s=s+(inputStr[j] - '0');
		}
		cout << "Case #" <<  i + 1 << ": " << p <<"\n";
	}
	return 0;
}