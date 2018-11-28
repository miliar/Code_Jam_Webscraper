#include <fstream>
#include <math.h>
#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <stdlib.h> 
#include <set>
#include <queue>
using namespace std;
#pragma comment(linker, "/STACK:999999999")
#define ll long long
const long long MAXN = 102;
const long double eps=0.00000000001;




int main()
{
	ifstream cin("input.txt");
	ofstream cout("output1.txt");
	int t;
	cin>>t;
	for (int q=0;q<t;q++)
	{
		int n;
		cin>>n;
		vector <long double> a(n),b(n);
		for (int i=0;i<n;i++)
			cin>>a[i];
		for (int i=0;i<n;i++)
			cin>>b[i];
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		int r=0;
		vector <bool> u(n,false);
		for (int i=0;i<n;i++)
		{
			long double c=a[i];
			int j=0;
			int fl=0;
			for (int k=0;k<n;k++)
			{
				if ((u[k]==false)&&(b[k]>c))
				{
					j=k;
					fl=1;
					break;
				}
			}
			if (fl==0)
			{
				r++;
				for (int k=0;k<n;k++)
				{
					if ((u[k]==false))
					{
						j=k;
						break;
					}
				}
			}		
			u[j]=true;
		}
		int r1=0;
		long double z=0;
		for (int i=0;i<n;i++)
		{
			if (b[z]<a[i])
			{
				r1++;
				z++;
			}
		}
		cout<<"Case #"<<q+1<<": "<<r1<<" "<<r<<endl;
	}
					
	return 0;
}