#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;
#define LL long long int
int main()
{
	fstream cin1;
	cin1.open ("A-large.in");			// A-small-attempt1.in");
  	
  	fstream cout1;
  	cout1.open("Problem1sol.txt");
  	
	int t;
	cin1>>t;
	for(int tt=1;tt<=t;tt++)
	{
		int n;
		cin1>>n;
		char c; int ci;
		int curr; 
		int xtra=0;
		cin1>>c; curr=(int)(c-'0');
		for(int i=1;i<=n;i++)
		{
			cin1>>c; ci=(int)(c-'0');
			if(ci==0) continue;
			if(i<=curr) curr+=ci;
			else
			{
				xtra+=i-curr;
				curr=i;
				curr+=ci;
			}
		}
		cout1<<"Case #"<<tt<<": "<<xtra<<endl;
	}
	cout1.close();
  	cin1.close();
}
