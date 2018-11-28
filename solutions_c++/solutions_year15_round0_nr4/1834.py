#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>

using namespace std;

int main()
{
	int a,b,c,i,j,k,n,m,t,r,x;
	cin >> t;
	for(i=0;i<t;i++)
	{
		cout << "Case #" << i+1 << ": ";
		cin >> x >> r >> c;
		if(x==1)
		{
			cout << "GABRIEL" << endl;
			continue;
		}
		if(x==2)
		{
			if(r%2==0 || c%2==0)
			{
				cout << "GABRIEL" << endl;
				continue;
			}
		}
		if(x==3)
		{
			if((r==2 && c==3) || (r==3 && c==2) || (r==3 && c==3) || (r==3 && c==4) || (r==4 && c==3))
			{
				cout << "GABRIEL" << endl;
				continue;
			}
		}
		if(x==4)
		{
			if((r==3 && c==4) || (r==4 && c==3) || (r==4 && c==4))
			{
				cout << "GABRIEL" << endl;
				continue;
			}
		}
		cout << "RICHARD" << endl;
	}
	return 0;
}
