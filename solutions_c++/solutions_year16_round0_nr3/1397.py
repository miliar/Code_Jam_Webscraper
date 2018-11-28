#include<iostream>
#include<string>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<math.h>
using namespace std;
int main()
{
	freopen("Primelist.txt","w",stdout);
	int N=14;
	vector<unsigned long long>Plist;
	unsigned long long Topnum = 3.4e7;
	Plist.push_back(2);
	cout<<endl<<2<<" ";
	for(int trynum=3; trynum<Topnum; trynum++)
	{
		int flag=1;
		for(int trydiv=0; trydiv<Plist.size(); trydiv++)
		{
			if(trynum % Plist[trydiv] == 0) {flag=0;break;}
		}
		if(flag==1) 
		{
			Plist.push_back(trynum);
			cout<<trynum<<" ";
		}
	}
	return 0;
}
