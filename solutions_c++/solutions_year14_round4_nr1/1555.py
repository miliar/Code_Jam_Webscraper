#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <iomanip> 
#include <string>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <stdlib.h> 
#include <set>
#include <queue>
using namespace std;




int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int qq;
	cin>>qq;
	for (int qqq=0;qqq<qq;qqq++)
	{
		cout<<"Case #"<<qqq+1<<": ";
		int n,x;
		cin>>n>>x;
		vector <int> a(n);
		for (int i=0;i<n;i++)
		{
			cin>>a[i];
		}
		sort(a.begin(),a.end());
		int k=0,r=0;
		int p=n-1;
		int pl=0;
		while (k!=n)
		{
				r++;
				k++;
				int q=x-a[p];
				if ((k!=n)&&(a[pl]<=q))
				{
					k++;
					pl++;
				}
				p--;
		}
		cout<<r<<endl;
	}

	return 0;
}